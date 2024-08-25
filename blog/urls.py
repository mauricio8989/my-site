from django.urls import path
from blog import views


urlpatterns = [
    path('', views.post_view.PostView.as_view(), name='home')
]
