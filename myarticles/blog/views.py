from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from . import forms

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.all().order_by('date')
    return render(request,'blog/blog_list.html',{'blogs':blogs})

def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render (request,'blog/blog_details.html',{'blog':blog})
    # return HttpResponse (slug)

@login_required(login_url='accounts:login')
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            reserveData = form.save(commit=False)
            reserveData.user = request.user
            reserveData.save()
            return redirect( 'blogs:all')
    else:
        form = forms.CreateBlog()
    return render (request,'blog/blog_create.html',{'form': form})
    # return HttpResponse (slug)

