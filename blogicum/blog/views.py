from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.http import Http404
from datetime import datetime


def index(request):
    template_name = 'blog/index.html'
    post_list = (Post.objects.filter(is_published=True,
                                     category__is_published=True,
                                     pub_date__lte=datetime.now()
                                     ).order_by('-pub_date')[:5])
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(pk=post_id),
                             pub_date__lte=datetime.now()
                             or Post.is_published == True
                             or Category.is_published == True)
    return render(request, template_name, {'post': post})


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.objects, slug=category_slug,
                                 is_published=True)
    post_list = (Post.objects.filter(category=category,
                                     is_published=True,
                                     pub_date__lte=datetime.now(),
                                     ))
    context = {
        'post_list': post_list,
        'category': category
    }
    return render(request, template_name, context)
