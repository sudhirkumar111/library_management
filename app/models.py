from django.db import models

# Create your models here.
BOOK_STATUS=(('BR','BORROWED'),
('AVL','AVAILABLE'),
)
class Book(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=3,choices=BOOK_STATUS)


