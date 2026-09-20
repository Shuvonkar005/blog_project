from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import RegisterForm, BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})



def post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', {'form': form})



@login_required
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form, 'editing': True})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)

    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")

    if request.method == 'POST':
        post.delete()
        return redirect('blog:home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})


@login_required
def my_posts(request):
    posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})