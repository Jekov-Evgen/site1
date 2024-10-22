from django.shortcuts import render
from .models import GamePost

def post_submission(request):
    data_model = GamePost.objects.all().order_by("-date")
    data_post = {"post" : data_model}
    return render(request, "post/home.html", context=data_post)

def go_to_post(request, pk):
    data_model = GamePost.objects.get(id=pk)
    data_post = {"post" : data_model}
    return render(request, "post/go_to_post.html", context=data_post)