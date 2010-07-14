"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from django.test import TestCase

class PIPAvailableTest(TestCase):
    def test_can_import(self):
        try:
            import PIL
            from PIL import Image
        except ImportError:
            self.fail('Could not import PIL')
