from django.db import models

# Create your models here.


class AccessData(models.Model):
    state = models.CharField(max_length=2)
    county = models.CharField(max_length=20)
    pct_access = models.CharField(max_length=20)
    county_id = models.CharField(max_length=20)

    def __str__(self):
        return self.county+self.state
