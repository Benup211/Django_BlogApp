# Django Project "blanco"

This is a simple README file to guide you through setting up a Django project named "blanco" with a "blog" app. The project includes two models: "Tag" and "Post," and it configures the admin site for managing these models. Follow the steps below to get started:

## Step 1: Create a Django Project

```bash
django-admin startproject blanco
```

## Step 2: Create a Django App

```bash
python manage.py startapp blog
```

After running the above command, add `'blog'` to the `INSTALLED_APPS` list in your `blanco/settings.py` file to include the "blog" app in your project.

## Step 3: Perform Initial Database Migration

```bash
python manage.py migrate
```

## Step 4: Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an administrative user for your project. This user will have access to the Django admin site.

## Step 5: Create Tag and Post Models

Create the "Tag" and "Post" models in the `blog/models.py` file. The "Tag" model should have attributes and values, and the "Post" model should have attributes such as author, created_at, modified_at, published_at, title, slug, summary, content, and tags.

## Step 6: Make Migrations for the Models

```bash
python manage.py makemigrations
```

This command will generate migration files based on the changes you made to the models.

## Step 7: Apply Migrations

```bash
python manage.py migrate
```

Apply the migrations to create the database tables for the "Tag" and "Post" models.

## Step 8: Register Models in the Admin Site

In `blog/admin.py`, register the "Tag" model and customize the "Post" model's admin interface by creating a `PostAdmin` class with prepopulated fields for the "slug" attribute. Then, register the "Post" model using the custom admin class.

```python
from django.contrib import admin
from .models import Tag, Post

admin.site.register(Tag)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} # Slug field is updated when the title is updated
admin.site.register(Post, PostAdmin)
```

## Step 9: Run the Development Server

```bash
python manage.py runserver
```

Now, you can access the Django admin site by visiting `http://127.0.0.1:8000/admin/` in your web browser. Use the superuser credentials you created earlier to log in. From the admin site, you can manage your "Tag" and "Post" models.