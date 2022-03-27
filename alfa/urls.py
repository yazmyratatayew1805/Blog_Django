from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


from posts.views import (
    index, blog, post, search,
    LikeView, desLikeView, foto, audio, video, login_user, paper_kid , paper, magazine_kid, magazine, hobby_kid, hobby )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    path('blog/', blog, name='post-list'),
    path('search/', search, name='search'),    
    path('post/<id>/', post, name='post-detail'),    
    path('accounts/login/',login_user,name='account_login'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('desLikeView/<int:pk>',desLikeView,name='desLikeView'),
    path('foto/', foto),
    path('audio/', audio),
    path('video/', video),
    path('paper_kid/', paper_kid, name='papers'),
    path('paper/<str:pk>/', paper, name='paper-detail'),
    path('magazine_kid/', magazine_kid, name='magazine'),
    path('magazine/<str:pk>/', magazine, name='magazine-detail'),
    path('hobby_kid/', hobby_kid, name='hobby'),
    path('hobby/<str:pk>/', hobby, name='hobby-detail'),
    # path('accounts/', include('allauth.urls'))
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    