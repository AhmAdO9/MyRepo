from django.db import models

# Create your models here.


class Details(models.Model):
    end_year = models.CharField(max_length=300, blank=True)
    intensity= models.CharField(max_length=300,blank=True)
    sector = models.CharField(max_length=300, blank = True)
    topic= models.CharField(max_length=300,blank=True)
    insight= models.CharField(max_length=300,blank=True)
    url= models.CharField(max_length=1000,blank=True)
    region=  models.CharField(max_length=300,blank=True)
    start_year= models.CharField(max_length=300, blank=True)
    impact= models.CharField(max_length=300, blank=True)
    added= models.CharField(max_length=300,blank=True)
    publishe= models.CharField(max_length=300, blank=True)
    country= models.CharField(max_length=300, blank=True)
    relevance= models.CharField(max_length=300,blank=True)
    pestle= models.CharField(max_length=300,blank=True)
    source= models.CharField(max_length=300,blank=True)
    title= models.CharField(max_length=300,blank=True)
    likelihood= models.CharField(max_length=300, blank=True)


    def __str__(self):
        return self.topic

class DetailsNew(models.Model):
    start_year= models.CharField(max_length=300, blank=True)
    end_year = models.CharField(max_length=300, blank=True)
    intensity= models.CharField(max_length=300,blank=True)
    relevance= models.CharField(max_length=300,blank=True)
    likelihood= models.CharField(max_length=300, blank=True)
