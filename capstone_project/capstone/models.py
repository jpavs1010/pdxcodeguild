from django.db import models

# Create your models here.


class AccessData(models.Model):
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=20)
    pct_access = models.IntegerField()
    county_id = models.IntegerField()

    def __str__(self):
        return self.county+self.state
