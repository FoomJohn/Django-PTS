from django.db import models

# models are the database stuff for django

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
    # after making this, we make migration then we push migration
