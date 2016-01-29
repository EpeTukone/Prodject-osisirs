from django.conf.urls import include, url


urlpatterns = [
    # Examples:
    # url(r'^$', 'lesson_youtube.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^1/', 'article.views.basic_one'),
    url(r'^2/', 'article.views.template_one'),
    url(r'^3/', 'article.views.template_next'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?<article_id>)\d+/$', 'article.views.article'),
]
