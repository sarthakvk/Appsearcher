from django.db import models

# Create your models here.


class Url(models.Model):

    url = models.URLField(primary_key=True)

    def __str__(self):

        return str(self.url)


class Keyword(models.Model):

    name = models.CharField(max_length=50)

    url = models.ForeignKey("Url", on_delete=models.CASCADE)

    def __str__(self):

        return str(self.name) + " with url " + str(self.url)
