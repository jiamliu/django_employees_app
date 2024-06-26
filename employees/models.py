from django.db import models

class Employee(models.Model):
    
    fullname = models.CharField(max_length = 200, null = True)
    department = models.CharField(max_length = 200, null = True)
    birthdate = models.CharField(max_length = 30, null = True)
    salary = models.TextField(max_length = 30, null = True)
    created_at = models.DateTimeField(auto_now_add = True, null = True)

    class Meta:
        ordering = ['created_at']

def __str__(self):
    return self.fullname
