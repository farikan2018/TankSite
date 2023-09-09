from django.urls import path
from .views import *



urlpatterns = [
    path('', HomeTank.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('create/', create, name='create'),
    path('proba/', Proba.as_view(), name='proba'),
    path('strana/<int:strana_id>/', GetStrana.as_view()),
    path('klas/<int:klas_id>/', GetKlas.as_view()),
    path('regist/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]