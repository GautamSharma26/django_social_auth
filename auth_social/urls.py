from django.urls import path, include
from auth_social.views import login_view, home

urlpatterns = [
    path('login/', login_view, name="login"),
    path('home/',home, name="home"),
    path('outh/', include('social_django.urls', namespace='social'))
]
