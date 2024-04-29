
from django.db import models

# Create your models here.
class ProdectDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    quantity=models.IntegerField()
    Price=models.IntegerField()
    

    #def __str__(self):
     #   return self.product_name


#id=505
#select *from tablename where id = 505;












@property
def image_url(self):
    if self.image and hasattr(self.image, 'url'):
        return self.image_url