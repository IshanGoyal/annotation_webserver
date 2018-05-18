from django.db import models

# Create your models here.
# These are just the basics from the slides
class Sequence(models.Model):
    seq_name = models.CharField(max_length=200)
    blast = models.CharField(max_length=200)
    pfam = models.CharField(max_length=200)
    prosite = models.CharField(max_length=200)
    kegg = models.CharField(max_length=200)
    go = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.seq_name
