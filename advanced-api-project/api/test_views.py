from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User

from api.models import Book

class BookAPITestCase(APITestCase):
    class BookAPITestCase(APITestCase):

        def setUp(self):
            """
            Set up test data and users
            """
            self.client = APIClient()

            # Create a user for authenticated requests
            self.user = User.objects.create_user(
                username="testuser",
                password="testpassword"
            )

            # Create sample books
            self.book1 = Book.objects.create(
                title="Django for Beginners",
                author="William Vincent",
                publication_year=2018
            )

            self.book2 = Book.objects.create(
                title="Two Scoops of Django",
                author="Daniel Roy Greenfeld",
                publication_year=2020
            )

            # URL for book list endpoint
            self.book_list_url = reverse("book-list")



    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "publication_year": 2008
        }

        response = self.client.post(self.book_list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data["title"], "Clean Code")

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "Unknown",
            "publication_year": 2023
        }

        response = self.client.post(self.book_list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_get_book_list(self):
        response = self.client.get(self.book_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_delete_book(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("book-detail", args=[self.book1.id])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)


    def test_search_books(self):
        response = self.client.get(
            self.book_list_url,
            {"search": "Django"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(
            self.book_list_url,
            {"ordering": "-publication_year"}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(
            response.data[0]["publication_year"],
            response.data[1]["publication_year"]
        )

