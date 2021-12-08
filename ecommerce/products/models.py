from django.db import models
import csv
import json


# Create your models here.

# for csv file
class Products(models.Model):
    category = models.CharField(max_length=50)
    subcategory = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    raw_price = models.DecimalField(max_digits=6, decimal_places=2)
    currency = models.CharField(max_length=10)
    discount = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    is_new = models.CharField(max_length=10)
    brand = models.CharField(max_length=50, null=True, blank=True)
    brand_url = models.TextField(null=True, blank=True)
    codCountry = models.CharField(max_length=50, null=True, blank=True)
    variation_0_color = models.CharField(max_length=50, null=True, blank=True)
    variation_1_color = models.CharField(max_length=50, null=True, blank=True)
    variation_0_thumbnail = models.TextField(null=True, blank=True)
    variation_0_image = models.TextField(null=True, blank=True)
    variation_1_thumbnail = models.TextField(null=True, blank=True)
    variation_1_image = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)

    @classmethod
    def from_csv(cls, csv_path):
        with open(csv_path) as f:
            reader = csv.reader(f)
            header = next(reader)
            for row in reader:
                _, created = cls.objects.get_or_create(
                    category=row[0],
                    subcategory=row[1],
                    name=row[2],
                    current_price=row[3],
                    raw_price=row[4],
                    currency=row[5],
                    discount=row[6],
                    likes_count=row[7],
                    is_new=row[8],
                    brand=row[9],
                    brand_url=row[10],
                    codCountry=row[11],
                    variation_0_color=row[12],
                    variation_1_color=row[13],
                    variation_0_thumbnail=row[14],
                    variation_0_image=row[15],
                    variation_1_thumbnail=row[16],
                    variation_1_image=row[17],
                    image_url=row[18],
                )


# Uncomment, when data upload from csv to db is needed, then runserver

# csv_paths = ["products/static/products/csv_files/kids.csv",
#              "products/static/products/csv_files/men.csv",
#              "products/static/products/csv_files/women.csv"]

# for path in csv_paths:
#     Products.from_csv(path)


# for json file

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.CharField(max_length=10)
    currency = models.CharField(max_length=10)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    images = models.TextField(max_length=1000)
    gender = models.CharField(max_length=10)
    quantity = models.IntegerField()
    price_usd = models.FloatField()
    # for price_usd and quantity , this SQL codes in db
    # ALTER TABLE products_product
    # ADD quantity AS (CASE
    #                  WHEN in_stock = "True" then 50
    #                  ELSE 0
    #                  END);
    # ALTER TABLE products_product
    # ADD price_usd as (round((price*0.013), 2));


    @classmethod
    def from_json(cls, json_path):
        with open(json_path) as f:
            data = json.load(f)
            for product in data:
                _, created = cls.objects.get_or_create(
                    name=product["name"],
                    price=product["price"],
                    in_stock=product["in_stock"],
                    currency=product["currency"],
                    brand=product["brand"],
                    description=product["description"],
                    images=product["images"],
                    gender=product["gender"],
                )


# Uncomment, when data upload from json to db is needed, then runserver
# Product.from_json("products/static/products/json/dataset.json")



