from django.db import models




class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    filter_class = (
        ('nature', 'nature'),
        ('people', 'people'),
        ('cars', 'cars'),
        ('buildings', 'buildings'),
    )
    filter_class = models.CharField(max_length=40, choices=filter_class)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.name

