from django.db import models

class MyAccount(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    profile_image = models.FileField(upload_to='profile_images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
