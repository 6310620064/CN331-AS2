from multiprocessing.connection import Client
from urllib import response
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subject, Register

class SubjectTestCase(TestCase):

    def setUp(self):
        
        subject1 = Subject.objects.create(code="CN331" , subject_name = "Software Engineering", quota = 2 ) 
        student1 = User.objects.create(first_name = "Ploynapat" , last_name = "Bunsena" , username = "6310610966")    
        Register.objects.create(user=student1 , subject=subject1)
        student1.set_password("123456Fresh")
        student1.save()

    def test_seat_available(self):
        cn331 = Subject.objects.first()
        self.assertTrue(cn331.is_seat_available())

    def test_seat_not_available(self):
        cn331 = Subject.objects.first()
        self.assertFalse(cn331.is_seat_not_available())