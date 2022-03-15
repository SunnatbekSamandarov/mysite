from django.db import models
class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Project = models.CharField(max_length=100)
    Message = models.TextField()
    def __str__(self):
        return self.Name


