from django.test import TestCase, Client
from django.urls import reverse
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

    def test_menu_rendering(self):
        response = self.client.get("/")
        self.assertContains(response, "Home")
        self.assertContains(response, "About")
        self.assertContains(response, "Contact")

    def test_active_item_detection(self):
        response = self.client.get("/about/")
        self.assertContains(response, 'class="current"', count=1)
        self.assertContains(response, "About")
        self.assertContains(response, "History")

    def test_submenu_expansion(self):
        response = self.client.get("/about/history/")
        self.assertContains(response, "History")
        self.assertContains(response, 'class="current"', count=1)

    def test_db_query_count(self):
        with self.assertNumQueries(1):
            self.client.get("/")


class MenuAdminTest(TestCase):
    def setUp(self):
        self.admin = Client()
        self.admin_user = self.admin.force_login(
            self.admin.create_superuser(
                username="admin",
                email="admin@example.com",
                password="password"
            )
        )

    def test_admin_list(self):
        response = self.admin.get("/admin/menu/menuitem/")
        self.assertEqual(response.status_code, 200)

    def test_admin_add(self):
        response = self.admin.post("/admin/menu/menuitem/add/", {
            "name": "New Item",
            "menu_name": "test_menu",
            "url": "/new-item/"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MenuItem.objects.filter(name="New Item").exists())
