from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem


class MenuModelTest(TestCase):
    def test_create_menu_item(self):
        item = MenuItem.objects.create(
            name="Home",
            url="/",
            menu_name="main_menu"
        )
        self.assertEqual(str(item), "Home")
        self.assertEqual(item.get_absolute_url(), "/")

    def test_named_url(self):
        item = MenuItem.objects.create(
            name="About",
            named_url="about",
            menu_name="main_menu"
        )
        self.assertEqual(item.get_absolute_url(), reverse("about"))


class MenuTagTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = MenuItem.objects.create(
            name="Home",
            url="/",
            menu_name="main_menu",
            order=1
        )
        self.about = MenuItem.objects.create(
            name="About",
            url="/about/",
            menu_name="main_menu",
            order=2
        )
        self.contact = MenuItem.objects.create(
            name="Contact",
            url="/contact/",
            menu_name="main_menu",
            order=3
        )
        self.history = MenuItem.objects.create(
            name="History",
            url="/about/history/",
            menu_name="main_menu",
            parent=self.about,
            order=1
        )

        # Убираем дублирующий пункт меню
        # self.named_item = MenuItem.objects.create(
        #     name="Named URL",
        #     named_url="about",
        #     menu_name="main_menu",
        #     order=4
        # )

    def test_menu_rendering(self):
        response = self.client.get("/")
        self.assertContains(response, "Home")
        self.assertContains(response, "About")
        self.assertContains(response, "Contact")

    def test_active_item_detection(self):
        response = self.client.get("/about/")
        # Ожидаем 1 активный пункт (About)
        self.assertContains(response, 'class="current"', count=1)
        # Проверяем, что подменю History видно
        self.assertContains(response, "History")

    def test_submenu_expansion(self):
        response = self.client.get("/about/history/")
        # Ожидаем 1 активный пункт (History)
        self.assertContains(response, 'class="current"', count=1)
        # Проверяем, что родительский пункт About активен
        self.assertContains(response, 'menu-item active', count=1)
        # Проверяем, что History отображается
        self.assertContains(response, "History")

    def test_db_query_count(self):
        with self.assertNumQueries(1):
            self.client.get("/")


class MenuAdminTest(TestCase):
    def setUp(self):
        self.admin = Client()
        # Создаем суперпользователя
        self.superuser = User.objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="password"
        )
        self.admin.force_login(self.superuser)

    def test_admin_list(self):
        response = self.admin.get("/admin/menu/menuitem/")
        self.assertEqual(response.status_code, 200)

    def test_admin_add(self):
        response = self.admin.post("/admin/menu/menuitem/add/", {
            "name": "New Item",
            "menu_name": "test_menu",
            "url": "/new-item/",
            "order": 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MenuItem.objects.filter(name="New Item").exists())

    def test_admin_edit(self):
        item = MenuItem.objects.create(
            name="Test Item",
            url="/test/",
            menu_name="test_menu"
        )
        response = self.admin.post(
            f"/admin/menu/menuitem/{item.id}/change/",
            {
                "name": "Updated Item",
                "menu_name": "test_menu",
                "url": "/updated/",
                "order": 1
            }
        )
        self.assertEqual(response.status_code, 302)
        updated = MenuItem.objects.get(id=item.id)
        self.assertEqual(updated.name, "Updated Item")
        self.assertEqual(updated.url, "/updated/")

    def test_admin_delete(self):
        item = MenuItem.objects.create(
            name="Delete Me",
            url="/delete/",
            menu_name="test_menu"
        )
        response = self.admin.post(
            f"/admin/menu/menuitem/{item.id}/delete/",
            {"post": "yes"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertFalse(MenuItem.objects.filter(name="Delete Me").exists())
