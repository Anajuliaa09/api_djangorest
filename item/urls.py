from django.conf.urls import url
from item import views

urlpatterns = [
    url(r'^api/item', views.item),
]