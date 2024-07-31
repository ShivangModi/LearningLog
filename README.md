# Learning Log
It is web app called Learning Log that allows users to log the topics they're interested in and to make journal entries as they learn about each topic.
The Learning Log home page will describe the site amd invites users to either register or log in.
Once logged in, a user can create a new topics, add new etries, and read and edit existing entries.
When user learn about new topic, keeping a journal of what they have learned can be helpful in tracking and revisiting information.

## Create virtual environment and install libraray
First create virtual environment and activate virtual environment:
```bash
conda create -n learning_log
conda activate learning_log
```

Now install python libraries which is required:
```bash
conda install python=3.10
conda install django
```

## Creating a Project in Django
Without leaving the activate environment, enter following commands to create a new project:
```bash
django-admin startproject learning_log .
ls
ls learning_log
```

Running the `ls` command shows that Django has created a new directory called **learning_log**, a **manage.py** file which is a short program that takes in commands and feeds them to the relevant part of Django to run them. We use these commands to manage tasks, such as working with databases and running servers.

The **learning_log** directory contains five files; the most important are **settings.py**, **urls.py**, and **wsgi.py**. The **settings.py** file controls how Django interacts with system and manages project. The **urls.py** file tells Django which pages to build in reponse to browser requests. The **wsgi.py** file helps Django server the files it creates. The filename is an acronym for *web server gateway interface*.

## Creating the Database
Django stores most of the information for project in database, so create database by following command:
```bash
python manage.py migrate
```

Any time modifying a database, we say we're *migrating* the database. Issuing the `migrate` command for the first time tells Django to make sure the databse matches the current state of project. The first time when we run command in a new project using SQLite, Django will create a new database. Django reports that it will prepare the databse to store information in needs to handle administrative and authenticatoin tasks. Django also created another file called `db.sqlite3`. 

**Viewing the Project:**
Enter the runsurver command as follows to view the project:
```bash
python manage.py runserver
```

**Note:** If you receive the *error* message that port is already in use, tell Django to use a different port by entering `python manage.py runserver 8001`, and then cycle through higher number until find an open port.

## Starting an App learning_logs
A Django project is organized as a group of individual *apps* that work together to make the project work as a whole.
```bash
python manage.py startapp learning_logs
```

The command `startapp appname` tells Django to create the infrastructure needed to build an app. When we look in the project directory, we will see a new folder called *learning_logs*. In that folder Django created some files. The most important files are *models.py*, *admin.py*, and *views.py*.

In *models.py* file create a class called **Topic**, which inherits Model from `django.db.models.Model` - a parent class included in Django that defines a model's basic functinality. We add two attributed to the *Topic* class: text and date_added. The *text* attribute is a `CharField` with *max_length *of 200 characters, which hold topic names and the *date_added* attribute is a `DateTimeField` which record a data and time with *auto_now_add=True* which tells Django to automatically set this attribute to the current date and time whenever the user creates a new topic.

We tell Django which attribute to use by default when it display information about topic. Django calls a `__str__()` method to display a simple representation of a model.

### Activate Models
To use our models, we have to tell Django to include our app in the overall project. Open *settings.py* file (in the *learning_log* directory); and add our app to the `INSTALLED_APPS`.

Now, we need to tell Django to modify the database so it can store information related to the model Topic. Run following command:
```bash
python manage.py makemigrations learning_logs
```
The command `makemigrations` tells Django to figure out how to modify the database so it can store the data associated with new models we've defined. This will create a table for the model Topic in the database.

## The Django Admin Site
Django makes it easy to worl with models through the admin site. Only the site's administrators use the admin site, not general users. Django allows to create a *superuser*, a user who has all precileges available on site. A user's *previleges* control the actions that user can take. The most restrictive privilege settings allow a user to only read public information on the site. To create a superuser in Django, enter the following command and
respond to the prompts:
```bash
python manage.py createsuperuser
```
**Note:** Django doesn't store the password enter; instead it stores a string deruved from the password, called hash. Each time user enter password, Django hashed entry and compare it to the stored hash. If the two hashes match, than you can log in. By requiring hashes to match, if an attacker gains access to a site’s database, they’ll be able to read its stored hashes but not the passwords. When a site is set up properly, it’s almost impossible to get the original passwords from the hashes.

Django includes some models in the admin site automatically, such as User and Group, but models we create need to be added manually. In *learning_logs* directory, Django has created *admin.py* file. In this file register Topic with admin site.

## Defining Entry Model
For a user to record what they've been learning about topic, we need to define a model for the kinds of entries users can make in their leaning logs. Each entry need to be associated with a particular topic. This relationship is called a *many-to-one* relationship, meaning many entries can be associated with one topic.

## The Learning Log Home Page
Making web pages with Django consists of three stages: defining URLs, writing views, and writing templates. You can do these in any order. 

A URL pattern describes the way the URL is laid out. It also tells Django what to look for when matching a browser request with a site URL so it knows which page to return. Each URL then maps to a particular *view* — the view function retrieves and processes the data needed for that page. The view function often renders the page using a template, which contains the overall structure of the page. 

### Mapping a URL
Users request pages by entering URLs into a browser and clicking links, so we’ll need to decide what URLs are needed. The home page URL is first: it’s the base URL people use to access the project. At the moment the base
URL, http://localhost:8000/, returns the default Django site that lets us know the project was set up correctly. We’ll change this by mapping the base URL to Learning Log’s home page.

### Writing a View
A view function takes in information from a request, prepares the data needed to generate a page, and then sends the data back to the browser, often by using a template that defines what the page will look like. The file *views.py* in learning_logs was generated automatically when we ran the command `python manage.py startapp`.

When a URL request matches the pattern we just defined, Django looks for a function in the *views.py* file. Django then passes the *views.py* request object to this view function. In this case, we don’t need to process any data for the page, so the only code in the function is a call to render(). The render() function here passes two arguments—the original request object and a template it can use to build the page.

### Writing a Template
The template defines what the page should look like, and Django fills in the relevant data each time the page is requested. A template allows you to access any data provided by the view. Because our view for the home page provided no data, this template is fairly simple.

Inside the **learning_logs** folder, make a new folder called templates. Inside the templates folder, make another folder called learning_logs. This might seem a little redundant (we have a folder named learning_logs inside a folder named templates inside a folder named learning_logs), but it sets up a structure that Django can interpret unambiguously, even in the context of a large project containing many individual apps. Inside the inner learning_logs folder, make a new file called *index.html*. 

## Building Additional Pages
We'll build two pages that display data: a page that lists all topics and a page that shows all the entries for a particular topic. For each page, we’ll specify a URL pattern, write a view function, and write a template. But before we do this, we’ll create a base template that all templates in the project can inherit from.

### Template Inheritance
When building a website, some elements will always need to be repeated on each page. Rather than writing these elements directly into each page, you can write a base template containing the repeated elements and then have each page inherit from the base. This approach lets you focus on developing the unique aspects of each page and makes it much easier to change the overall look and feel of the project.

**The Parent Template:**
We’ll create a template called *base.html* in the same directory as *index.html*. This file will contain elements common to all pages; every other template
will inherit from *base.html*.

**Note:**
In Python code, we almost always use four spaces when we indent. Template files tend to have more levels of nesting than Python files, so it’s common to use only two spaces for each indentation level. You just need to ensure that you’re consistent.

**Note:**
In a large project, it’s common to have one parent template called base.html for the entire site and parent templates for each major section of the site. All the section templates inherit from base.html, and each page in the site inherits from a section template. This way you can easily modify the look and feel of the site as a whole, any section in the site, or any individual page. This configuration provides a very efficient way to work, and it encourages you to steadily update your site over time.

### Allowing User to Enter Data
Allow user to add a new topic, add a new entry, and edit their previous entries. Currently, only a superuser can enter data through the admin site. We don’t want users to interact with the admin site, so we’ll use Django’s formbuilding tools to build pages that allow users to enter data.
