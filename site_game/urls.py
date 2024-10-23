from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.post_submission, name="post"),
    path('<int:pk>/', views.go_to_post, name="go_to_post"),
    path('comment/<int:pk>/', views.add_comment, name="comment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
