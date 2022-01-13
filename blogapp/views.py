from django.shortcuts import render,redirect
from blogapp.models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User, auth
from django. contrib import messages
# from .models import Feature

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts}) 


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()


    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context, )


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-date_created')
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)


# def post(request, pk):
#     post = Post.objects.get(id=pk)
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post
#             )
#             comment.save()


#     comments = Comment.objects.filter(post=post)
#     context = {
#         "post": post,
#         "comments": comments,
#         "form": form,
#     }
#     return render(request, "blog_detail.html", context, )


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used ')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, "Password Not Thesame")
            return redirect('register')
    else:
        return render(request, 'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('design')
        else:
            messages.info(request, 'wrong info')
            return redirect('login')
    else:
        return render(request, 'login.html')


def post(request, pk):
    return render(request, 'post.html', {'pk':pk})