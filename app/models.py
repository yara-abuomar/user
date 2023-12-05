from django.db import models
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    age=models.IntegerField()
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def creat_user(first,last,email,age):
        User.objects.create(first_name=first,last_name=last, email=email,age=age)

    def all_user():
        User.objects.all()
        




# Create your models here.
