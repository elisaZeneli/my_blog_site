from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(requets, 'blog/blog_list.html')
