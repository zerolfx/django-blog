from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import *
import markdown2


class IndexView(ListView):
    template_name = "index.html"
    context_object_name = "article_list"
    paginate_by = 7

    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['about_list'] = About.objects.all()
        return super(IndexView, self).get_context_data(**kwargs)


class IndexView_rc(ListView):
    template_name = "index_rc.html"
    context_object_name = "article_list"
    paginate_by = 7

    def get_queryset(self):
        article_list = Recommend.objects.all()
        for article in article_list:
            article.abstract = markdown2.markdown(article.abstract, extras=['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category_rc.objects.all().order_by('name')
        kwargs['about_list'] = About.objects.all()
        return super(IndexView_rc, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"
    context_object_name = "article"
    pk_url_kwarg = 'article_id'

    def get_object(self):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'])
        return obj


class CategoryView(ListView):
    template_name = "index.html"
    context_object_name = "article_list"
    paginate_by = 7

    def get_queryset(self):
        article_list = Article.objects.filter(status='p', category=self.kwargs['category_id'])
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['about_list'] = About.objects.all()
        return super(CategoryView, self).get_context_data(**kwargs)


class CategoryView_rc(ListView):
    template_name = "index_rc.html"
    context_object_name = "article_list"
    paginate_by = 7

    def get_queryset(self):
        article_list = Recommend.objects.filter(category=self.kwargs['category_id'])
        for article in article_list:
            article.abstract = markdown2.markdown(article.abstract, extras=['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category_rc.objects.all().order_by('name')
        kwargs['about_list'] = About.objects.all()
        return super(CategoryView_rc, self).get_context_data(**kwargs)

class TagView(ListView):
    template_name = "index.html"
    context_object_name = "article_list"
    paginate_by = 7

    def get_queryset(self):
        article_list = Article.objects.filter(status='p', tags=self.kwargs['tag_id'])
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'])
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['about_list'] = About.objects.all()
        return super(TagView, self).get_context_data(**kwargs)


