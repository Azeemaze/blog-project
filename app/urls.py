from django.urls import path

from members.views import EditProfilePageView
from .import views
from .views import HomeView, Article_View, AddPost, UpdatePost, DeletePost, LikeView, AddCategoryView, CategoryView, \
    AddComment

urlpatterns = [
    # path('home/',views.home,name='home')
    path('HomeView',HomeView.as_view(), name='home'),
    path('article/<int:pk>',Article_View.as_view(),name='article-detail'),
    path('addpost/',AddPost.as_view(),name='addpost'),
    path('article/edit/<int:pk>',UpdatePost.as_view(),name='updatepost'),
    path('article/delete/<int:pk>',DeletePost.as_view(),name='deletepost'),
    path('like/<int:pk>', LikeView, name= 'like_post'),
    path('addcategory/', AddCategoryView.as_view(), name='addcategory'),
    path('category/<str:cats>/',CategoryView, name = 'category'),
    path('<int:pk>/edit_profile', EditProfilePageView.as_view(), name='Edit_pageview'),
    path('article/<int:pk>/comment/', AddComment.as_view(), name='addcomment'),

]