from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title']) <2:
            errors['titleLength'] = "Title must be atleast 2 characters"
        if len(postData['network']) <2:
            errors['networkLength'] = "Network must be atleast 2 characters"
        return errors

class Show(models.Model):
    #id
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()