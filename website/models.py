from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=100)
    foundation_year = models.PositiveSmallIntegerField()
    foundation_city = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.PositiveSmallIntegerField()
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.name, self.band, self.release_year)

    @staticmethod
    def get_old_albums():
        return Album.objects.filter(release_year__lte=2000)


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(
        Album,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tracks',
        related_query_name='track'
    )
    is_single = models.BooleanField(default=False)
    band = models.ForeignKey(
        Band,
        on_delete=models.CASCADE,
        related_name='tracks',
        related_query_name='track'
    )

    def __str__(self):
        return "{} - {}".format(self.name, self.band)

