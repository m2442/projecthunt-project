from django.urls import path, include
from . import views

urlpatterns= [
    path('<int:project_id>/', views.detail, name='detail'),
    path('<int:project_id>/upvote', views.upvote, name='upvote'),
    path('<int:project_id>/upvote1', views.upvote1, name='upvote1'),
    path('<int:project_id>/enquiry', views.enquiry, name='enquiry')

]
