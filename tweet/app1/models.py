from django.db import models

# Create your models here.
class tweeter(models.Model):
    person=models.CharField(max_length=50)
    dop=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="media")
    caption=models.CharField(max_length=150)


    def __str__(self):
        return self.person