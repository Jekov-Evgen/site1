from django.db import models
import datetime

class GamePost(models.Model):
    update_header = models.CharField(max_length=100)
    img_update = models.ImageField(upload_to="images")
    description_of_the_update = models.TextField()
    date = models.DateField(default=datetime.date(2024, 11, 18))
    
    def __str__(self) -> str:
        return self.update_header
    
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
    
