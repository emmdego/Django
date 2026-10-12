from django.shortcuts import render, redirect
from django.http import HttpResponse

# Static view
def greetings(request):
    return HttpResponse("Hello everyone")


# Dinamic view
def books(request, name=None, author=None):
    if name and author:
        return HttpResponse(f'Now your seeing the view of the books with name and autor')
    elif name:
        return HttpResponse(f'Now your seeing the view of the books without author')
    elif author:
        return HttpResponse(f'Now your seeing the view of only authors')
    else:
        return HttpResponse(f'Now your seeing the view without parameters')

# Redirection
def onSystem(request):
    return redirect('/book/')


# Templates
def template_books(request):
    books_data = {
        'name': 'Don Quijote de la Mancha',
        'author': 'Miguel de Cervantes'
    }

    return render(request, 'books/index.html', books_data) # 'books/index.html' is the path of the file in the project
