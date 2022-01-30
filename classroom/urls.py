from django.urls import include, path
from django.contrib.auth.views import LoginView 
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('home/', views.home, name = 'home'),
    path('student_entry/', views.student_entry, name = 'student_entry'),
    path('your_attendance/', views.your_attendance, name = 'your_attendance'),
    path('register/', views.register, name = 'register'),
    path('login/', LoginView.as_view(template_name='classroom/login.html'), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('sendmail/', views.sendmail, name = 'sendmail'),
    ]
