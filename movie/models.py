from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    duration = models.IntegerField()
    #
    # class Meta:
    #     verbose_name_plural = "movies"

    def __str__(self):
        return f" Movie: {self.title} (id = {self.id})"
