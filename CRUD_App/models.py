from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)


def __str__(self):
    return 'User: ' + self.first_name + ' ' + self.last_name + ' ' + self.user_name + ' ' + self.email + ' ' + self.password
