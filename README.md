# Weather-App-Django
This repository implements a weather app that uses Open Weather API and Django as a backend framework and deployment using heroku.

<h3>Important Links</h3>
<ul>
<li><a href="https://devcenter.heroku.com/articles/getting-started-with-python">Deployment using Heroku</a></li>
<li><a href="https://openweathermap.org/api">Open Weather API</a></li>
<li><a href="https://github.com/mdn/django-locallibrary-tutorial">MDN Docs</a></li>
</ul>


## Summary Workflow
The following is a basic workflow that you can use as a quick reference for developing a Django Project.

### Setup
1. Within a new directory, create and activate a virtualenv.
2. Install Django.
3. Create your project: <pre> django-admin.py startproject <name> </pre>
4. Create a new app:<pre> python manage.py startapp <appname> </pre>
5. Add your app to the INSTALLED_APPS tuple.


### Add Basic URLs and Views
1. Map your Project’s urls.py file to the new app.
2. In your App directory, create a urls.py file to define your App’s URLs.
3. Add views, associated with the URLs, in your App’s views.py; make sure they return a HttpResponse object. Depending on the situation, you may also need to query the model (database) to get the required data back requested by the end user.


### Templates and Static Files
1. Create a templates and static directory within your project root.
2. Update settings.py to include the paths to your templates.
3. Add a template (HTML file) to the templates directory. Within that file, you can include the static file with - <pre>{% load static %}</pre> and <pre> {% static "filename" %} </pre>. Also, you may need to pass in data requested by the user.
4. Update the views.py file as necessary.


### Models and Databases

1. Update the database engine to settings.py (if necessary, as it defaults to SQLite).
2. Create and apply a new migration.
3. Create a super user.
4. Add an admin.py file in each App that you want access to in the Admin.
5. Create your models for each App.
6. Create and apply a new migration. (Do this whenever you make any change to a model).


### Forms
1. Create a forms.py file at the App to define form-related classes; define your ModelForm classes here.
2. Add or update a view for handling the form logic - e.g., displaying the form, saving the form data, alerting the user about validation errors, etc.
3. Add or update a template to display the form.
4. Add a urlpattern in the App’s urls.py file for the new view.

### User Registration
1. Create a UserForm
2. Add a view for creating a new user.
3. Add a template to display the form.
4. Add a urlpattern for the new view.

### User Login
1. Add a view for handling user credentials.
2. Create a template to display a login form.
3. Add a urlpattern for the new view.

### Setup the template structure
1. Find the common parts of each page (i.e., header, sidebar, footer).
2. Add these parts to a base template
3. Create specific. templates that inherent from the base template.

### Heroku Hosting
- Copy the project seperately
- Go to 'Getting Started on Heroku with Python'
- Create an Heroku account
- install pipenv
- Install git ( check git --version)
- Install Heroku CLI
- Login heroku
- Create a virtual enviroment
- Run manage.py not gonna run - pip freeze nothing installing
- Check which version django,requests you have and install it
- Run manage.py and then stop it
- Go to django heroku
- Create a Procfile and
- Install django-heroku
- Add stuff to settings.py file
- Install guincorn
- pip freeze > requirements.txt
- heroku create <name> (to create an app on heroku)
- git status git commands (git push heroku master)
- Open up the website
- Admin panel not working. heroku run bash. Migrations
