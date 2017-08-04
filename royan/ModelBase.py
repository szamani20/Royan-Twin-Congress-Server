from django.db import models


class Abstract(models.Model):
    background = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        abstract = True


class Speaker(models.Model):
    avatar = models.ImageField(blank=True, null=True, upload_to='images/speakers/')
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    country = models.CharField(max_length=70)
    affiliation = models.TextField()
    topic = models.CharField(max_length=250)
    time = models.DateTimeField(blank=True, null=True)
    venue = models.CharField(max_length=200)

    class Meta:
        managed = False
        abstract = True


class Winner(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/winners/')
    email = models.EmailField(blank=True, null=True)
    affiliation = models.TextField()
    country = models.CharField(max_length=70)
    short_cv = models.CharField(max_length=200)
    award_time = models.DateTimeField()
    award_venue = models.CharField(max_length=200)
    kazemi = models.BooleanField(default=False)

    class Meta:
        managed = False
        abstract = True


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(null=True, blank=True, upload_to='images/companies/')
    location = models.CharField(max_length=200, null=True, blank=True)  # ghorfe!
    website = models.URLField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        managed = False
        abstract = True
