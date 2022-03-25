from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.news_of_day,name='newsToday'),
    re_path(r'^today/$',views.news_of_day,name='newsToday'),

    re_path(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    re_path(r'^search/', views.search_results, name='search_results')
]