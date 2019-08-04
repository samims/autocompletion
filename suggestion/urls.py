from django.urls import path
from .views import AutoCompleteView, SearchTemplateView

app_name = "suggestion"

urlpatterns = [
    # path(
    path('search', AutoCompleteView.as_view(), name='auto_complete'),
    path('', SearchTemplateView.as_view(), name='home')
]
