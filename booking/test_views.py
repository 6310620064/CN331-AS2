from ast import arg
from urllib import response
from xmlrpc import client
from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from django.contrib.auth.models import User
import booking
from booking.views import index
from .models import Subject, Register

class RegisterViewTestCase(TestCase):

    def setUp(self):
        subject1 = Subject.objects.create(code="CN331" , subject_name = "Software Engineering", quota = 2 ) 
        student1 = User.objects.create(first_name = "Ploynapat" , last_name = "Bunsena" , username = "6310610966")
        student1.set_password("123456Fresh")
        student1.save()
        Register.objects.create(
            user=student1 , subject=subject1)
        

    def test_index_view_status_code(self):
        c = Client()
        self.client.login(username = "6310610966" , password = "123456Fresh")
        response = c.get(reverse("booking:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_context(self):
        c = Client()
        self.client.login(username = "6310610966" , password = "123456Fresh")
        response = self.client.get(reverse("booking:index"))
        self.assertEqual(response.context['booking'].count(), 0)

    def test_valid_subject_page(self):

        c = Client()
        self.client.login(username = "6310610966" , password = "123456Fresh")
        s = Subject.objects.first()
        response = self.client.get(reverse("booking:enrollment", args=(s.id,)))
        self.assertEqual(response.status_code, 302)

    def test_invalid_subject_page(self):

        max_id = Subject.objects.all().aggregate(Max("id"))['id__max']
        c = Client()
        self.client.login(username = "6310610966" , password = "123456Fresh")
        response = c.get('/views.subject', args=(max_id+1,))
        self.assertEqual(response.status_code, 404)


    def test_cannot_book_nonavailable_seat(self):
        student2 = User.objects.create_user(username = "6310620064", password = "123456Pooz", first_name = "Pavisa")
        s = Subject.objects.first()
        s.seats.add(student2)
        s.save()

        c = Client()
        self.client.login(username = "6310620064" , password = "123456Pooz")
        c.get("/views.subject")
        self.assertFalse(s.is_seat_not_available())
