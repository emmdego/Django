I already have python3 installed in my system 

# Installation
So first we'll install all the necessary, and the process would be the following:

```
mkdir my-django-project
cd my-django-project

python3 -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install django
```

1. `mkdir my-django-project`: First I create a directory named "my-django-project"
2. `cd my-django-project`: Then I change my current directory to the one I just created
3. `python3 -m venv .venv`: I create the hidden venv directory, the one that will help me as the virtual environment
4. `source .venv/bin/activate`: I initialize the virtual environment
5. `python -m pip install --upgrade pip`: I upgrade the package manager pip
6. `python -m pip install django`: So I can finally install Django


---


# Creation of the new Django project
To start a project with Django, we execute the following command:
```
django-admin startproject config .
```

- `django-admin`: It's for using the commands of django (It serves for creating projects, apps, servers, etc.)
- `startproject`: It's for starting a new project with django
- `config`: core of the project / the backend
- `.`: We're referring to the current directory


Then, to start running our server we execute the following command:
```
python3 manage.py runserver
```


---

# Applications/Apps in Django
The apps in Django are the foundations of how to structure a project in Django

The apps are independent modules(like sales, inventory, dashboard, etc.) in charge of a specific functionality, it's a piece of the project(and the project is the one that joins all the pieces together)

To create an app, we use the following command:
```
python3 manage.py startapp Library
```
(Library will be the name that I want my app to has)


Then we update the "INSTALLED_APPS" section in the [settings.py](/config/settings.py) file of the [config](/config) directory, adding the new app we just created/started, in my case it'd be 'Library'
Example:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Library'
]
```

Then we have to make the migrations of the new apps:
```
python3 manage.py makemigrations
```

And migrate:
```
python3 manage.py migrate
```



# Views
The views are functions or classes that get HTTP requests and give back a HTTP response

In the app that we created [Library](/Library/), there's a file named [views.py](/Library/views.py), and there we can get the requests and give the responses:

## Static views
A static view happens when only has one path, like in this example, that the function "greetings" only has one `return`
```
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greetings(request):
    return HttpResponse("Hello everyone")
```

Then in the [config](/config/) directory, in the [urls.py](/config/urls.py) file we import the created view, in my case it would be like this: `from Library.views import greetings`

Then add in the 'urlpatterns' list the path of the new view like this:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', greetings)
]
```

## Dinamic views
A dinamic view happens when a view can have different paths, something like this:
```
def books(request, name=None, author=None):
    if name and author:
        return HttpResponse(f'Now your seeing the view of the books with name and autor')
    elif name:
        return HttpResponse(f'Now your seeing the view of the books without author')
    elif author:
        return HttpResponse(f'Now your seeing the view of only authors')
    else:
        return HttpResponse(f'Now your seeing the view without parameters')
```

Here we can see that the response changes depending on the parameters `name` and `author`, if we have them or not

Then in the [config](/config/) directory, in the [urls.py](/config/urls.py) file we import the created view, in my case it would be like this: `from Library.views import greetings, books`

Then add in the 'urlpatterns' list the path of the new view like this:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/', greetings),
    path('book/', books),
    path('book/<str:name>/', books),
    path('book/<str:author>/', books),
    path('book/<str:name>/<str:author>/', books)
]
```

We write `<str:parameter>` to specify that the path needs that parameter



## View redirection
The redirection of views is used when something specific happens, and we want to redirect the user to another view

So, first we'll need to import the `redirect` function in the [views.py](./Library/views.py) file of the [Library](./Library/) directory we created:
```
from django.shortcuts import render, redirect
```

And then we create a new function, I'll name it 'onSystem':
```
def onSystem(request):
    return redirect('/book/')
```

And we only do a `return redirect('/path that we want to redirect the user/')`

Then we go to the [urls.py](./config/urls.py) file of the [config](./config/) directory, and add to the 'urlpatters' the path like this:
```
path('to_system/', onSystem)
```

# HTTP STATUS CODE
The HTTP status codes are numbers that our server send to the clients, to tell them what happend with a specific request

The views always returns HTTP responses, and those responses have HTTP status codes

**EXAMPLES**
- 200: OK
- 301: Moved Permanently
- 302: Found (Temporary = redi)
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 404: Not found
- 500: Internal Server Error
- 502: Bad Gateway
- 503: Service Unavailable


# TEMPLATES
The templates are dinamic HTML files that allow us to write variables of python in HTML, these templates also get the data to show it to the client by rendering the html with the data prepared in the views

Example:
```
def template_books(request):
    books_data = {
        'name': 'Don Quijote de la Mancha',
        'author': 'Miguel de Cervantes'
    }

    return render(request, 'books/index.html', books_data) # 'books/index.html' is the path of the file in the project
```

Then inside our Library directory, we create the "templates" directory, and inside of it we create the paths, for example, in my case it'd be the "books" directory, and inside of it the "index.html" file of the previous example

Inside this index.html file, we create the visual part to show the variables of the 'books_data' dictionary created in views.py:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>Books in stock</h2>
    
    <br>

    <p><strong>Name: </strong>{{ name }}</p>
    <p><strong>Author: </strong>{{ author }}</p>
</body>
</html>
```


And finally we import the new template function in [`config/urls.py`](./config/urls.py) and add a new path with the "template_books" function/view