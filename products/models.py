from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#product title
#url
#pub_date
#votes total
#image
#icon
#body



#pub_date_pretty  


#hunter: who submiited the product

class Product(models.Model):
    title=models.CharField(max_length=200)
    url=models.TextField()
    pub_date=models.DateTimeField()
    votes_total=models.IntegerField(default=1)
    image=models.ImageField(upload_to='images/')
    icon=models.ImageField(upload_to='images/')
    body=models.TextField()
    #hunter: who submiited the product
    hunter=models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
    return self.title


def pub_date_pretty(self):
    return self.pub_date.strftime('%b  %e  %y')

def summary(self):
    return self.body[:100]
