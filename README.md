# tree-menu-project
=======
# 🌳 Tree Menu Django Application

[![Django Version](https://img.shields.io/badge/Django-5.2-green)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Compose-orange)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Django application provides functionality for creating and displaying tree menus with compliance with the following requirements:

- The menu is implemented via template tag
- Automatic expansion of the active menu branch
- Storing the menu structure in the database
- Editing via the standard Django admin panel
- Determining the active item by the URL of the current page
- Support for multiple independent menus on one page
- Minimum number of queries to the database (exactly 1 query per menu)

## 🚀 Features

- **🌳 Recursive menu** - automatic construction of a tree structure
- **⚡️ Optimized queries** - only 1 SQL query for rendering the menu
- **🧩 Simple integration** - adding a menu via template tag
- **🎛 Admin panel** - convenient management of the menu structure
- **📱 Adaptive design** - Bootstrap 5 for displaying the menu
- **🐳 Docker containerization** - quick launch in an isolated environment

## 📦 Installation

### With Docker (recommended)

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tree-menu-app.git
cd tree-menu-app
```

2. Build and run the containers:
```bash
docker-compose up --build
```

3. Apply database migrations:
```bash
docker-compose exec web python manage.py migrate
```

4. Create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

5. The application will be available at: [http://localhost:8000](http://localhost:8000)

### Without Docker

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up the database in `tree_menu_project/settings.py`

3. Apply migrations:
```bash
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## 🛠 Usage

1. Go to the admin panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)
2. Create a menu, specifying a unique name
3. Add menu items, setting parents if necessary
4. In the Django template, add:

```django
{% load menu_tags %}

{# Render the menu by name #}
{% draw_menu 'main_menu' %}
```

## 🧪 Testing

To run tests, run:

```bash
docker-compose exec web python manage.py test menu
```

Or without Docker:

```bash
python manage.py test menu
```

Test coverage:
- Models
- Admin panel
- Template tags
- Menu display logic

## 🗄 Project structure

```
tree_menu_app/
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
├── menu/
│ ├── admin.py
│ ├── apps.py
│ ├── migrations/
│ ├── models.py
│ ├── templatetags/
│ ├── templates/
│ │ └── menu/
│ │ └── menu_template.html
│ └── tests.py
└── tree_menu_project/ 
├── settings.py 
├── urls.py 
└── wsgi.py
```
>>>>>>> develop
