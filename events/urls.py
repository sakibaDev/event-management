from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Event URLs
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/update/<int:pk>/', views.event_update, name='event_update'),
    path('events/delete/<int:pk>/', views.event_delete, name='event_delete'),

    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # ✅ Participant URLs
    path('participant/', views.participant_list, name='participant_list'),
    path('participant/create/', views.participant_create, name='participant_create'),
    path('participant/update/<int:pk>/', views.participant_update, name='participant_update'),
    path('participant/delete/<int:pk>/', views.participant_delete, name='participant_delete'),
]
