from django.db import models
from django.utils import timezone

# Create your models here.
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.core.validators import MaxValueValidator, MinValueValidator


class MeteoRecord(models.Model):
    """Model representing a weather record form meteo station """
    DATE = models.DateTimeField(default=timezone.now)
    TA = models.FloatField()
    DP = models.FloatField(default=0)
    WC = models.FloatField(default=0)
    RH = models.FloatField(default=0)
    PA = models.FloatField(default=0)
    PR = models.FloatField(default=0)
    PR1H = models.FloatField(default=0)
    PR24h = models.FloatField(default=0)
    SR_1M = models.FloatField(default=0)
    SR_1D = models.FloatField(default=0)
    SR_45_1M = models.FloatField(default=0)
    SR_45_1D = models.FloatField(default=0)
    SD_1H = models.FloatField(default=0)
    SD_1D = models.FloatField(default=0)
    SD_45_1H = models.FloatField(default=0)
    SD_45_1D = models.FloatField(default=0)

    class Meta:
        ordering = ['-DATE']

    def __str__(self):
        """String for representing the Model object."""
        return self.DATE.strftime("%Y-%m-%d, %H:%M:%S")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('meteorecord-detail', args=[str(self.id)])

class MeteoRecord(models.Model):
    """Model representing a weather record form meteo station """
    DATE = models.DateTimeField(default=timezone.now)
    TA = models.FloatField()
    DP = models.FloatField(default=0)
    WC = models.FloatField(default=0)
    RH = models.FloatField(default=0)
    PA = models.FloatField(default=0)
    PR = models.FloatField(default=0)
    PR1H = models.FloatField(default=0)
    PR24h = models.FloatField(default=0)
    SR_1M = models.FloatField(default=0)
    SR_1D = models.FloatField(default=0)
    SR_45_1M = models.FloatField(default=0)
    SR_45_1D = models.FloatField(default=0)
    SD_1H = models.FloatField(default=0)
    SD_1D = models.FloatField(default=0)
    SD_45_1H = models.FloatField(default=0)
    SD_45_1D = models.FloatField(default=0)

    class Meta:
        ordering = ['-DATE']

    def __str__(self):
        """String for representing the Model object."""
        return self.DATE.strftime("%Y-%m-%d, %H:%M:%S")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('meteorecord-detail', args=[str(self.id)])

class WindRecord(models.Model):
    """Model representing a weather record form meteo station """
    #`WS1AVG`, `WD1AVG`, `WS1MIN2`, `WS1AVG2`, `WS1MAX2`, `WD1MIN2`, `WD1AVG2`, `WD1MAX2`, `WS1MIN10`, `WS1AVG10`, `WS1MAX10`, `WD1MIN10`, `WD1AVG10`, `WD1MAX10`
    DATE = models.DateTimeField(default=timezone.now)
    WS1AVG = models.FloatField(default=0)
    WD1AVG = models.FloatField(default=0)
    WS1MIN2 = models.FloatField(default=0)
    WS1AVG2 = models.FloatField(default=0)
    WS1MAX2 = models.FloatField(default=0)
    WD1MIN2 = models.FloatField(default=0)
    WD1AVG2 = models.FloatField(default=0)
    WD1MAX2 = models.FloatField(default=0)
    WS1MIN10 = models.FloatField(default=0)
    WS1AVG10 = models.FloatField(default=0)
    WS1MAX10 = models.FloatField(default=0)
    WD1MIN10 = models.FloatField(default=0)
    WD1AVG10 = models.FloatField(default=0)
    WD1MAX10 = models.FloatField(default=0)

    class Meta:
        ordering = ['-DATE']

    def __str__(self):
        """String for representing the Model object."""
        return self.DATE.strftime("%Y-%m-%d, %H:%M:%S")

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('windrecord-detail', args=[str(self.id)])
