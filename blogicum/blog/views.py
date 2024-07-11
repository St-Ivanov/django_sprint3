from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Post


def post_query_set():
    query_set = (
        Post.objects.select_related(
            'author',
            'location',
            'category'
        ).filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
        )
    )
    return query_set


def index(request):
    template = 'blog/index.html'
    posts = post_query_set().order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/detail.html'
    post = get_object_or_404(
        post_query_set().filter(pk=pk),  # Почему не работает с get?
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.values('title', 'slug'),
        slug=category_slug,
        is_published=True,
    )
    posts = post_query_set().filter(
        category__slug=category_slug,
    )
    context = {'category': category, 'post_list': posts}
    return render(request, template, context)
