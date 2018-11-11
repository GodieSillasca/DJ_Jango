from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    #auth = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    #text = models.TextField()
    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.user

    def password(self):
    	return self.password
