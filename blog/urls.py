from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<page>\d+)$', views.IndexView.as_view(), name='pages'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    # url(r'^blog/category/(?P<cate_id>\d+)$', views.)
]