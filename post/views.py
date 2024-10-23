from django.shortcuts import render, redirect, get_object_or_404
from .models import GamePost, Comments
from post.form import FormComm

def post_submission(request):
    data_model = GamePost.objects.all().order_by("-date")
    data_post = {"post" : data_model}
    return render(request, "post/home.html", context=data_post)

def go_to_post(request, pk):
    post = get_object_or_404(GamePost, id=pk)
    comments = Comments.objects.filter(belonging=post)
    
    context = {
        'post': post,
        'comments': comments
    }
    
    return render(request, "post/go_to_post.html", context)

def add_comment(request, pk):
    if request.method == 'POST':
        form = FormComm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.belonging = GamePost.objects.get(pk=pk)
            comment.save()
            return redirect('go_to_post', pk=pk)  
    else:
        form = FormComm()
    return render(request, 'post/add_comment.html', {'form': form})