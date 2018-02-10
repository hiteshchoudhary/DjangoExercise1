from django.db import models

class Cmdr(models.Model):
    text = models.TextField()


    def __str__(self):
        return self.text
