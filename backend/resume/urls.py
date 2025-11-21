from django.urls import path
from .views import resume_matcher


urlpatterns = [
    path('resume_matcher/', resume_matcher, name='resume_matcher')
]
