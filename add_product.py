import os
import sys
import django

# Add your project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realmcrystal.settings")

# Configure Django
django.setup()

# Now you can import your Django models and perform database operations
from accounts.models import Product




# Create a new Product instance
new_product = Product(
    name="quartz necklace",
    description="this quartz necklace provides a tranquility and uniqueness that makes one feel calm",
    price=23.99,
    quantity=20,
    image_url="https://i.imgur.com/S2tg4dV.png"
)

# Save the new product to the database
new_product.save()

print("New product added successfully!")
