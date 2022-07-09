from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowersView.as_view()),
    path('followers/<int:pk>', views.FollowersDetail.as_view())
]