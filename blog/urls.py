from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tag_id>\d+)/(?P<page>\d+)$', views.TagView.as_view(), name='tag'),
    url(r'^category/(?P<category_id>\d+)/(?P<page>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^recommend/(?P<recommend_id>\d+)$', views.IndexView_rc.as_view(), name='rc'),
    url(r'^cate-rc/(?P<category_id>\d+)/(?P<page>\d+)$', views.CategoryView_rc.as_view(), name='category_rc'),
    # url(r'^blog/category/(?P<cate_id>\d+)$', views.)
]