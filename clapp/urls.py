from django.urls import path,include
from .views import update_likes

urlpatterns = [
    
    path('<int:clapp_id>/', update_likes, name='update_likes'),
]