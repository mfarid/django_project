from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Mohd Farid',
        'title' : 'A new blog by Farid',
        'date_posted' : 'Nov 28, 2020',
        'content' : 'some cool content of the blog by Mohd'
    },
    {
        'author': 'John Doe',
        'title' : 'A new blog by John',
        'date_posted' : 'Nov 21, 2020',
        'content' : 'some cool content of the blog by John'
    }
]

def home(request):
    context = {'posts': posts};
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'The title is about....'})
