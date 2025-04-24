from django.db import models

# Create your models here.




#custom user model, admin comliant permissions
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    has_voted = models.BooleanField(default=False)



#candidate model

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


from django.contrib import admin
from .models import User, Candidate
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name', 'votes']
