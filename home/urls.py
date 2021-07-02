from django.urls import path, include
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.homePageView, name='homePage'),
    # path('login/', views.loginView, name='login'),
    # path('logout/', views.logoutView, name='logout'),
    # path('delete/', views.deleteView, name='delete'),
    # path('edit/', views.editView, name='edit'),
]
