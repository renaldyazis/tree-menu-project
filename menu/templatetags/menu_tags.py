from django import template
from ..models import MenuItem
from collections import defaultdict

register = template.Library()


def build_tree(items):
    tree = defaultdict(list)
    item_dict = {}
    for item in items:
        tree[item.parent_id].append(item)
        item_dict[item.id] = item
    return tree, item_dict


def find_active_item(tree, items, current_path):
    for item in items:
        # Сравниваем пути без учета завершающего слэша
        item_url = item.get_absolute_url().rstrip('/')
        clean_current = current_path.rstrip('/')

        if item_url == clean_current:
            return item

        children = tree.get(item.id, [])
        active_child = find_active_item(tree, children, current_path)
        if active_child:
            return active_child

    return None


def mark_active_branch(item_dict, active_item, active_items):
    if active_item:
        active_items.add(active_item.id)
        if active_item.parent_id and active_item.parent_id in item_dict:
            parent = item_dict[active_item.parent_id]
            mark_active_branch(item_dict, parent, active_items)


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    tree, item_dict = build_tree(menu_items)
    root_items = tree.get(None, [])

    active_item = find_active_item(tree, root_items, current_path)

    active_items = set()
    if active_item:
        mark_active_branch(item_dict, active_item, active_items)

    return {
        'menu_tree': tree,
        'root_items': root_items,
        'active_items': active_items,
        'current_path': current_path
    }


@register.filter(name='get_item')
def get_item_filter(dictionary, key):
    return dictionary.get(key, [])
