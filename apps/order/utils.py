import random
from .models import Order

def randomOrderNumber():
    order_number = int(random.randint(1000000000, 9999999999))  
    return order_number