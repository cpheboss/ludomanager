from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GameListView.as_view(), name='games'),
    path('games/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('members/', views.MemberListView.as_view(), name='members'),
    path('members/<int:pk>', views.MemberDetailView.as_view(), name='member-detail'),
]

