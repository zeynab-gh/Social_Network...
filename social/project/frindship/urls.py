from django.urls import path
from .views import UserListView,RequestView,RequestListView,AcceptView,FrindListView


urlpatterns =[
    path('users-list/', UserListView.as_view()),
    path('request/', RequestView.as_view()),
    path('request-list/', RequestListView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('friends/', FrindListView.as_view()),
]
