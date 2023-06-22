from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from .forms import CreatePostForm





def home(request):
    posts = BlogPost.objects.order_by('-publication_date')
    return render(request,"blog/index.html",{'posts': posts})


from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})


def blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/blog_post.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            # Create a new instance of the blog post
            blog_post = form.save(commit=False)
            
            # Set the author of the blog post
            blog_post.author = request.user
            
            # Save the blog post to the database
            blog_post.save()
            
            # Redirect to the blog post detail page
            return HttpResponse("""<script>alert('Blog uploaded successfully')</script>
                                <script>location.href('127.0.0.1:8000')</script>""")
    else:
        form = CreatePostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    content = request.POST['content']
    author = request.user
    comment = Comment(post=post, content=content, author=author)
    comment.save()
    return redirect('blog_post', post_id=post_id)


