from django.db import models


class ShortURL(models.Model):
    url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    access_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        """
        Return the short code.
        :return: Short code.
        :rtype: str
        """
        return self.short_code
