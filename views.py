from django.shortcuts import render

posts = [


    {
        'author': 'Ayman',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Nov 20, 2023'
    },

    {
        'author': 'Hamza',
        'title':'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Nov 22, 2023'
    }
     



]


def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})