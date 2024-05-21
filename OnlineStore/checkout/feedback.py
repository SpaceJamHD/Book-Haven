from django.db import models
from django.contrib.auth.models import User
from store.models import Item

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='feedbacks')
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.comment} - Рейтинг: {self.rating}'
