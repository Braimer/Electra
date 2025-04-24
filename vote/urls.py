from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView, logout_view ,vote_view,results_view

urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('vote/', vote_view, name='vote'),
    path('results/', results_view, name='results'),
    # Add the vote and results URL patterns
]
