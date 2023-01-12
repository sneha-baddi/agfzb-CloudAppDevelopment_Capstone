from django.db import models
from django.utils.timezone import now
from django.core import serializers
import uuid
import json

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Make')
    description = models.CharField(max_length=500)

def __str__(self):
        return "Name: " + self.name + "," + \
            "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    CARTYPE_CHOICE = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon'),
        ]

    carMake = models.ForeignKey(CarMake, null=True, on_delete=models.CASCADE)
    modelName = models.CharField(null=False, max_length=30,  default='Car')
    dealerId = models.IntegerField(default=1, primary_key=True)
    carType = models.CharField(
        null=False,
        max_length=20,
        choices=CARTYPE_CHOICE,
        default=SEDAN
    )
    year = models.DateField(default=now)

def __str__(self):
        return "Car Make: " + self.carMake + "," + \
                "Model Name: " + self.modelName + "," + \
                "Car Type: " + self.carType

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, id, lat, long, st, zip, full_name):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
        # Dealer Full Name
        self.full_name = full_name

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review):
        # Required attributes
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes
        self.purchase_date = ""
        self.purchase_make = ""
        self.purchase_model = ""
        self.purchase_year = ""
        self.sentiment = ""
        self.id = ""

    def __str__(self):
        return "Review: " + self.review

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)