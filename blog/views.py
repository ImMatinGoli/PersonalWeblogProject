from django.shortcuts import render
from .models import BlogPost, Comment, Category
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator


def posts_list_view(request):
    all_posts = BlogPost.objects.all().order_by('-datetime_created')
    paginator = Paginator(all_posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/posts_list.html', {'posts': page_obj})

def posts_detail_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        comment = Comment()
        comment.content = request.POST['content']
        comment.author = request.user
        comment.post = post
        comment.stars = request.POST['stars']
        comment.save()
        return render(request, 'blog/comment_success.html', {'post': post})
    else:
        return render(request, 'blog/post_detail.html', {'post': post})


# blog/views.py

@login_required
def post_update_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.user != post.author:
        return render(request, 'blog/access_denied.html', status=403)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        if 'cover' in request.FILES:
            post.cover = request.FILES['cover']

        post.save()

        category_ids = request.POST.getlist('categories')
        if category_ids:
            post.categories.set(category_ids)
        else:
            post.categories.clear()

        return redirect('posts_list')

    categories = Category.objects.all()
    context = {
        'post': post,
        'categories': categories,
    }
    return render(request, 'blog/post_update.html', context)

@login_required
def post_delete_view(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if request.user.username != 'matin':
        return render(request, 'blog/access_denied.html', status=403)

    if request.user == post.author:
        if request.method == 'POST':
            post.delete()
            return render(request, 'blog/post_delete_success.html')
        else:
            return render(request, 'blog/post_delete.html', {'post': post})

@login_required
def post_create_view(request):
    if request.user.username != 'matin':
        return render(request, 'blog/access_denied.html', status=403)

    if request.method == 'POST':
        if request.user.username == 'matin':
            post = BlogPost()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.author = request.user

            if 'cover' in request.FILES:
                post.cover = request.FILES['cover']

            post.save()

            category_ids = request.POST.getlist('categories')
            if category_ids:
                post.categories.set(category_ids)

            return render(request, 'blog/post_create_success.html', {'post': post})

    else:
        categories = Category.objects.all()
        return render(request, 'blog/post_create.html', {'categories': categories})

def category_posts_view(request, name):
    category = get_object_or_404(Category, name=name)
    posts = category.posts.all().order_by('-datetime_created')

    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_posts.html', context)

def access_denied_update_view(request, pk):
    return render(request, 'blog/access_denied.html')


def logged_out_view(request):
    return render(request, 'account/logged_out.html')


@login_required
def like_post_view(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return JsonResponse({
        'liked': liked,
        'count': post.total_likes()
    })

def search_view(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct().order_by('-datetime_created')

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'blog/search_results.html', context)


def live_search_view(request):
    query = request.GET.get('q', '')
    results = []

    if len(query) >= 2:
        posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        ).distinct().order_by('-datetime_created')[:5]

        for post in posts:
            results.append({
                'title': post.title,
                'url': post.get_absolute_url(),
            })

    return JsonResponse({'data': results})
