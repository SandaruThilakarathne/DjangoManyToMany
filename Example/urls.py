from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .router import router

urlpatterns = [
    path('', include(router.urls))
]

urlpatterns = format_suffix_patterns(urlpatterns)
