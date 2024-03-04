from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    # class MPTTMeta:
    #     order_insersion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    bid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.name