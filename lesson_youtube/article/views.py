from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from . import models
def basic_one(request):
    view = "basic_one"
    html = "<html><body>this is %s view</html></body>" % view
    return HttpResponse(html)

def template_one(reqest):
    view = "template_one"
    t = get_template('myview.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_next(reqest):
    view = "3 var"
    return render_to_response('myview.html', {'name': view})

def articles(regest):
    return render_to_response('articles.html', {'articleles': models.Article.objects.all()})

def article(regest, article_id=1):
    render_to_response('article.html', {'article': models.Article.objects.get(id=article_id),
                                        'commens': models.Comments.object.filter(comments_article_id=article_id)})
