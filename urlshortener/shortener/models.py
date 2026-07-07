from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10,unique = True)
    clicks = models.PositiveIntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    expires_at = models.DateTimeField(null = True , blank = True )

    def __str__(self):
        return  self.short_code
    
    

