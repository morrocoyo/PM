from django.shortcuts import render, render_to_response
from django.views.generic.edit import View
# from django.views.generic import View
from django.template import RequestContext
from .models import BlogPost
from datetime import datetime, timedelta
import random


# Create your views here.

class HomeView(View):
    def get(self, request, *arg, **kwargs):
        num = random.randint(0,10000)
        # TweetsAmb = pickle.load(open('/home/juang/Documents/Python Scripts/Genesis/Data/TweetsAmb', "rb"))
        # TweetsAmb = TweetsAmb[0:10]
        context = {"bool_item": True,
                   "num": num,
            }
        return render(request, 'home.html', context)


def ArticulosView(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = BlogPost(title=title,content=content)
        post.last_update = datetime.utcnow() - timedelta(hours=5)
        post.content = content
        post.save()

    posts = BlogPost.objects
    context = {'Posts':posts}
    return render(request, 'articulos.html', context)

def Update(request):
    id = eval("request." + request.method + "['id']" )
    post = BlogPost.objects(id=id)[0]

    if request.method == 'POST':
        post.title = request.POST['title']
        post.last_update = datetime.utcnow()
        post.content = request.POST['content']
        post.save()

        template_name = 'articulos.html'
        context = {'Posts':BlogPost.objects}

    elif request.method == 'GET':
        template_name = 'snippets/update.html'
        context = {'post': post}

    return render(request, template_name, context)

def Delete(request):
    id = eval("request." + request.method + "['id']")
    post = BlogPost.objects(id=id)[0]
    if request.method == 'POST':
        post = BlogPost.objects(id=id)[0]
        post.delete()
        template_name = 'articulos.html'
        context = {'Posts': BlogPost.objects}
    elif request.method == 'GET':
        template_name = 'snippets/delete.html'
        context = {'id': id}

        return render(request, template_name, context)