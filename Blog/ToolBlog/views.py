from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def blog_post(request):
    return render(request, 'blog-post.html')


def blog_list(request):
    return render(request, "blog-list.html")
