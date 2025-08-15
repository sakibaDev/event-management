import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from events import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
    path('', views.dashboard, name='home'), 
]
