from django.db import models

# Create your models here.


class AccessData(models.Model):
    county_id = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=100)
    pct_access_2010 = models.CharField(max_length=5)
    pct_access_2015 = models.CharField(max_length=5)
    pct_diabetes_2008 = models.CharField(max_length=5)
    pct_diabetes_2013 = models.CharField(max_length=5)
    pct_obese_2008 = models.CharField(max_length=5)
    pct_obese_2013 = models.CharField(max_length=5)
    grocery_2009 = models.CharField(max_length=5)
    grocery_2014 = models.CharField(max_length=5)
    supercenter_2009 = models.CharField(max_length=5)
    supercenter_2014 = models.CharField(max_length=5)
    convenience_2009 = models.CharField(max_length=5)
    convenience_2014 = models.CharField(max_length=5)
    white_2010 = models.CharField(max_length=5)
    black_2010 = models.CharField(max_length=5)
    hispanic_2010 = models.CharField(max_length=5)
    asian_2010 = models.CharField(max_length=5)
    amerindian_2010 = models.CharField(max_length=5)
    hawaiian_2010 = models.CharField(max_length=5)


    def __str__(self):
        return self.county+','+' '+self.state


class MapData(models.Model):
    variable = models.CharField(max_length=20)
    header_text = models.CharField(max_length=200)
    legend_text = models.CharField(max_length=200)
    lower_bound = models.CharField(max_length=20)
    upper_bound = models.CharField(max_length=20)

    def __str__(self):
        return self.variable


class CorrelationData(models.Model):
    variable1 = models.CharField(max_length=20)
    variable2 = models.CharField(max_length=20)
    correlation = models.FloatField(max_length=5)

    def __str__(self):
        return self.variable1+' '+self.variable2
