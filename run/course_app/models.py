from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    duration = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    seats_available = models.IntegerField()

    def __str__(self):
        return self.title
