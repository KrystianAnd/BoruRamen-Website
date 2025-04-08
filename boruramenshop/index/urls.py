from index import views
from django.urls import path
from .views import robots_txt

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('polityka-strony/', views.PolitykaStrony, name='polityka_strony'),
    path('set-language/', views.set_language, name='set_language'),  
    path("robots.txt", robots_txt, name="robots_txt"),
]
