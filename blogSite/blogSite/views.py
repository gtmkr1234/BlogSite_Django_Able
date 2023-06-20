from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required




def home(request):
    posts = BlogPost.objects.order_by('-publication_date')
    return render(request,"index.html",{'posts': posts})


from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/blog_post.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = BlogPost(title=title, content=content, author=author)
        post.save()
        return redirect('home')

    return render(request, 'blog/create_post.html')


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    content = request.POST['content']
    author = request.user
    comment = Comment(post=post, content=content, author=author)
    comment.save()
    return redirect('blog_post', post_id=post_id)


