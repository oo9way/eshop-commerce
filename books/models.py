from django.db import models
class Users(models.Model):
    full_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.full_name