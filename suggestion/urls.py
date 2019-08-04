from django.urls import path
from .views import WordSearchView

app_name = "suggestion"

urlpatterns = [
    # path(
    path('', WordSearchView.as_view(), name='search')
]
