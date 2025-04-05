from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from datetime import datetime


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.filter(is_published=True,
                                    category__is_published=True,
                                    pub_date__date__lt=datetime.now()
                                    ).order_by('-pub_date')[:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.objects.filter(
                             pub_date__date__lt=datetime.now(),
                             is_published=True,
                             category__is_published=True),
                             pk=id
                             )
    return render(request, template_name, {'post': post})


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.objects.filter(slug=category_slug,
                                 is_published=True))
    post_list = Post.objects.filter(category=category,
                                    is_published=True,
                                    pub_date__date__lt=datetime.now(),
                                    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
