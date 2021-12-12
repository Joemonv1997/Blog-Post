from django.db import models

class login_user(models.Model):
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class register_user(models.Model):
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    def __str__(self):
        return self.name

class title(models.Model):
    title= models.TextField()
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title


