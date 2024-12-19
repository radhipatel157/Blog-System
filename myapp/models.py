from django.db import models

# Create your models here.
class login(models.Model):
    email=models.EmailField(max_length=100)
    passw=models.CharField(max_length=100)
    def __str__(self):
        return self.email 
    
class Blog(models.Model):
    user = models.ForeignKey(login, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 