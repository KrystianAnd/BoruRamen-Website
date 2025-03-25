from index import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('menu/', views.menu, name='menu'),
    path('polityka-strony/', views.PolitykaStrony, name='polityka_strony'),
    path('set-language/', views.set_language, name='set_language'),  # ✅ Dodajemy obsługę zmiany języka
]
