from django.test import TestCase
from .views import inappropriate_content_filter
import pytest

class InappropriateContentFilterTest(TestCase):
    titles = []
    bodies = []

    def setUp(self):
        self.titles = ["Hello", "hell"]
        self.bodies = ["hello", "hell with it"]

    def test_appropriate_content(self):
        self.assertEqual(
            inappropriate_content_filter(self.titles[0], self.bodies[0]), 
            {'inappropriate': False, 'inappropriate_words': []}
        )
        
        self.assertNotEqual(
            inappropriate_content_filter(self.titles[0], self.bodies[0])['inappropriate'], 
            True
        )

    def test_inappropriate_content(self):
        self.assertEqual(
            inappropriate_content_filter(self.titles[1], self.bodies[1]), 
            {'inappropriate': True, 'inappropriate_words': ['hell', 'hell']}
        )
        
        self.assertNotEqual(
            inappropriate_content_filter(self.titles[1], self.bodies[0])['inappropriate'], 
            False
        )
        
    def test_incorrect_arguments(self):
        with self.assertRaisesMessage(IndexError, 'tuple index out of range'):
            inappropriate_content_filter(self.titles[0])