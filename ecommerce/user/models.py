from django.db import models
from django.contrib.auth.models import User

from helpers.choices import STATUS_CHOICES


def image_path(self, path):
    return f'images/{self.user.id}/{path}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True)
    image = models.ImageField(default="products/images/profile_icon.png", upload_to=image_path, null=True, blank=True)

    # TODO discuss tp add user profile pic

    def __str__(self):
        return f'{self.user.username} Profile'

    # def get_user_gender(self):
    #     return f"{self.gender}"
