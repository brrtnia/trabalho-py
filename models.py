
from django.db import models
 
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    birthday=models.CharField(max_length=11)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    
 
    def __str__(self):
        return self.firstname + " " + self.lastname
   
  
    class Meta:  
        db_table = "web_member"