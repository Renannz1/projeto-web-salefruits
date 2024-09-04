from django.db import models
from django.conf import settings


class Room(models.Model):
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    
    
class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tex = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"{self.user.first_name}:{self.tex}"

# Create your models here.
