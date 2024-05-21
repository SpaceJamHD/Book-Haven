from django.urls import path
from .views import item_details, store, tag_details, tag_list, page2

app_name = 'store'

urlpatterns = [
    path('', store, name='home'),
    path('store/', page2, name='store'),
    path('item/<slug:item_slug>/', item_details, name='item_details'),
    path('tags/', tag_list, name='tag_list'),
    path('tags/<slug:slug>/', tag_details, name='tag_details'),
]
