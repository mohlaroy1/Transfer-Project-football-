from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Season(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs/')
    president = models.CharField(max_length=50, blank=True, null=True)
    coach = models.CharField(max_length=50, blank=True, null=True)
    found_date = models.DateField(blank=True, null=True)

    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50, blank=True, null=True)
    number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(99)],
        blank=True, null=True
    )
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)

    club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    old_club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True, related_name="export_transfers")
    new_club = models.ForeignKey(Club, on_delete=models.SET_NULL, blank=True, null=True, related_name="import_transfers")
    price = models.FloatField(blank=True, null=True)
    price_tft = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    season = models.ForeignKey(Season, on_delete=models.SET_NULL, blank=True, null=True)


class Tryout(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    position = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



