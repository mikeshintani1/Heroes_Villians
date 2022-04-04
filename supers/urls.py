from . import views
from django.urls import path


urlpatterns = [
    path('', views.review_list),
    path('<int:pk>', views.review_detail),
]