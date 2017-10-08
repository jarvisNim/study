from django.db import models

# Create your models here.

class Photo(models.Model):
    """pystagram for photo."""
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to='uploads/%Y/%m/%d/filterd')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def delet(self,*args,**kwargs):
        self.image.delet()
        self.filtered_image.delete()
        super(Photo,self).delete(*args,**kwargs)
