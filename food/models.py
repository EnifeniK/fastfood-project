from django.db import models


class Meal(models.Model):
    image = models.ImageField(upload_to='food/images/')
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default=1)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title



