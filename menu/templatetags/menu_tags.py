from django import template
from django.urls import reverse, NoReverseMatch, resolve
from ..models import MenuItem
from collections import defaultdict
from django.template.defaulttags import register as template_register

register = template.Library()


def build_menu_tree(menu_items):
    tree = defaultdict(list)
    for item in menu_items:
        tree[item.parent_id].append(item)
    return tree


def find_active_item(items, current_path):
    for item in items:
        if item.get_absolute_url() == current_path:
            return item
        active_child = find_active_item(items.get(item.id, []), current_path)
        if active_child:
            return active_child
    return None


def mark_active_branch(tree, active_item, active_items):
    if active_item:
        active_items.add(active_item.id)
        if active_item.parent_id:
            mark_active_branch(tree, active_item.parent, active_items)


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path_info

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    tree = build_menu_tree(menu_items)
    root_items = tree.get(None, [])

    active_item = find_active_item(root_items, current_path)

    active_items = set()
    if active_item:
        mark_active_branch(tree, active_item, active_items)

    return {
        'menu_tree': tree,
        'root_items': root_items,
        'active_items': active_items,
        'current_path': current_path
    }


@template_register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
