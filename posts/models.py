from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse 



User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Galery(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FotolarGornusler(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Fotolar(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    fg = models.ForeignKey(FotolarGornusler, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

   
class Video_kid(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    

class Video(models.Model):
    name = models.CharField(max_length=100)
    play = models.FileField()
    picture = models.ImageField()
    video_kid = models.ForeignKey(Video_kid, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Audio_kid(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Audio(models.Model):
    name = models.CharField(max_length=100)
    music = models.FileField()
    audio_kid = models.ForeignKey(Audio_kid, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class Paper_kid(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Paper(models.Model):
    date = models.CharField(max_length=100)
    paper_kid = models.ForeignKey(Paper_kid, on_delete=models.CASCADE)
    image = models.ImageField()
    pdf = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paper_kid.name +' * '+ self.date

    def get_absolute_url(self):
        return reverse('paper-detail', kwargs={
            'id':self.id
        })

class Magazine_kid(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Magazine(models.Model):
    date = models.CharField(max_length=100)
    magazine_kid = models.ForeignKey(Magazine_kid, on_delete=models.CASCADE)
    image = models.ImageField()
    pdf = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.magazine_kid.name +' * '+ self.date

    def get_absolute_url(self):
        return reverse('magazine-detail', kwargs={
            'id':self.id
        })

class Hobby_kid(models.Model):
    name = models.CharField(max_length=100)
    desciption = models.TextField()
    image = models.ImageField()
    imageleft = models.ImageField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Hobby(models.Model):
    date = models.CharField(max_length=100)
    hobby_kid = models.ForeignKey(Hobby_kid, on_delete=models.CASCADE)
    image = models.ImageField()
    pdf = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hobby_kid.name +' * '+ self.date

    def get_absolute_url(self):
        return reverse('hobby-detail', kwargs={
            'id':self.id
        })



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    Teswir  = models.TextField()
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    
    timestamp = models.DateTimeField(auto_now_add=True)    
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    likes = models.ManyToManyField(User, blank=True, related_name='blog_posts')
    dislike = models.ManyToManyField(User, blank=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id':self.id
        }) 

  



    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()
