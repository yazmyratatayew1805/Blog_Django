from django.contrib import messages
from django.db.models import Count, Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .forms import CommentForm
from .models import Post, Author, PostView, Galery, Fotolar, FotolarGornusler, Audio_kid, Audio, Video_kid, Video, Paper_kid, Paper, Magazine_kid, Magazine, Hobby_kid, Hobby
from marketing.models import Signup
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import *
from django.contrib.auth.forms import User


def register(request):
    form=Register_Form()
    if request.method == 'POST':
        form=Register_Form(request.POST)
        if form.is_valid:
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            parol=form.cleaned_data['parol']
            username=form.cleaned_data['username']
            user=User.objects.create_user(username=username,password=parol,first_name=first_name,last_name=last_name)
            user.save()
        
    context={
        'form':form
    }
    return render(request,'registation.html',context)


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    post.dislike.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def desLikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.dislike.add(request.user)
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

    
def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = Post\
        .objects\
        .values('categories__title')\
        .annotate(Count('categories__title'))
    return queryset    


def index(request):
    featured = Post.objects.filter(featured=True)[0:3]
    latest = Post.objects.order_by('-timestamp')[0:3]
    picture=Galery.objects.all()

    if request.method == "POST":
        text = request.POST.get("text")
        
        new_signup = Signup() 
        new_signup.text = text   
        new_signup.ip = request.META.get('REMOTE_ADDR')      
        new_signup.save()
        messages.success(request,"Size admin tarapyndan login we parol berler!")


    context = {
        'object_list' : featured,
        'latest' : latest,
        'picture':picture
    }
    return render(request, 'index.html', context)

def foto(request):
    foto_kat=FotolarGornusler.objects.all()
    fotolar=Fotolar.objects.order_by('-fg')

    context = {
        'foto_kat':foto_kat,
        'fotolar':fotolar
    }

    return render(request, 'foto.html', context)


    

def audio(request):
    audio_kid = Audio_kid.objects.all()
    audio = Audio.objects.all()

    context = {
        'audio_kid':audio_kid,
        'audio':audio
    }

    return render(request, 'audio.html', context)

def video(request):
    video_kid = Video_kid.objects.all()
    video = Video.objects.order_by('video_kid')

    context = {
        'video_kid':video_kid,
        'video':video
    }

    return render(request, 'video.html', context)


def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset,
        'most_recent' : most_recent,
        'page_request_var' : page_request_var,
        'category_count' : category_count
    }
    return render(request, 'blog.html', context)

def paper_kid(request):
    paper_list = Paper_kid.objects.all()        
    context = {        
        'paper_list':paper_list

    }
    return render(request, 'paper_kid.html', context)

def paper(request,pk):
    paper_list=Paper.objects.filter(paper_kid=pk)
    paginator = Paginator(paper_list, 6)    
    page_request_var = 'page'
    page = request.GET.get(page_request_var)    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset
       
    }

    return render(request,'paper.html', context)

def magazine_kid(request):
    magazine_list = Magazine_kid.objects.all()        
    context = {        
        'magazine_list':magazine_list

    }
    return render(request, 'magazine_kid.html', context)

def magazine(request,pk):
    magazine_list=Magazine.objects.filter(magazine_kid=pk)
    paginator = Paginator(magazine_list, 6)    
    page_request_var = 'page'
    page = request.GET.get(page_request_var)    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset
       
    }

    return render(request,'magazine.html', context)

def hobby_kid(request):
    hobby_list = Hobby_kid.objects.all()        
    context = {        
        'hobby_list':hobby_list

    }
    return render(request, 'hobby_kid.html', context)

def hobby(request,pk):
    hobby_list=Hobby.objects.filter(hobby_kid=pk)
    paginator = Paginator(hobby_list, 6)    
    page_request_var = 'page'
    page = request.GET.get(page_request_var)    
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset
       
    }

    return render(request,'hobby.html', context)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]    
    post = get_object_or_404(Post, id=id)
    like=Post.objects.get(id=id)
    likes=like.likes.count
    dislikes=like.dislike.count    

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)
     
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            
            form.instance.user = request.user
            form.instance.post = post
            
            
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'id': post.pk
            }))  
    context = {
        'form': form,
        'post': post,        
        'most_recent' : most_recent,
        'category_count' : category_count,
        'likes':likes,
        'dislikes':dislikes
        
    }
    return render(request, 'post.html', context)
 
# def post_create(request): 
#     title = 'Döretmek'
#     form = PostForm(request.POST or None, request.FILES or None)
#     author = get_author(request.user)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.author = author
#             form.save()
#             return redirect(reverse("post-detail", kwargs={
#                 'id': form.instance.id
#             }))
#     context = {
#         'title': title,
#         'form': form
#     }
#     return render(request, "post_create.html", context)



# def post_update(request, id):
#     title = 'Üýtgetmek'
#     post = get_object_or_404(Post, id=id)
#     form = PostForm(
#         request.POST or None,
#         request.FILES or None,
#         instance=post)
#     author = get_author(request.user)
#     if request.method == "POST":
#         if form.is_valid():
#             form.instance.author = author
#             form.save()
#             return redirect(reverse("post-detail", kwargs={
#                 'id': form.instance.id
#             }))
#     context = {
#         'title': title,
#         'form': form
#     }
#     return render(request, "post_create.html", context)

# def post_delete(request, id):
#     post = get_object_or_404(Post, id=id)
#     post.delete()
#     return redirect(reverse("post-list"))

def login_user(request):
    form=Login_Form()
    if request.method == 'POST':
        forms=Login_Form(request.POST)
        if forms.is_valid():
            username=request.META.get('REMOTE_ADDR')
            password=forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('home'))
    context={
        'form':form
    }
    return render(request,'login.html',context)


# def register(request):
#     form=Register_Form()

#     if request.method == 'POST':
#         forms=Register_Form(request.POST)
#         if forms.is_valid:
#             ady=forms.cleaned_data['ady']
#             fam=forms.cleaned_data['famiyasa']
#             parol=forms.cleaned_data['password']
#             user=Users.objects.create_user(username=ady,first_name=ady,last_name=fam,password=parol)
#             user.save()

#     context={
#         'form':form
#     }
#     return render(request,'register.html',context)