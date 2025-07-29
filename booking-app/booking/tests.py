from django.test import TestCase
from .models import YourModel  # Replace with your actual model

class BookingModelTests(TestCase):

    def test_model_creation(self):
        # Test the creation of a model instance
        instance = YourModel.objects.create(field_name='value')  # Replace with actual fields
        self.assertEqual(instance.field_name, 'value')  # Replace with actual fields

    def test_model_str(self):
        # Test the string representation of the model
        instance = YourModel.objects.create(field_name='value')  # Replace with actual fields
        self.assertEqual(str(instance), 'Expected String Representation')  # Replace with actual expected value

    # Add more test cases as needed for your application