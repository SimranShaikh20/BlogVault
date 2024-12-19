from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.TextField(  max_length=5000)
    photo=models.ImageField(upload_to='tweet/photo/',blank=True,null=True)
    create_at=models.DateTimeField( auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.user.user_permissions}-{self.text[:10]}'