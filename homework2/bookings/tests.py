from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Booking, Movie, Seat


class BookingUnitTests(TestCase):
    #function that sets up the starting data that every test will use
    def setUp(self):
        self.alice = User.objects.create_user(
            username="Alice",
            password="yomama69"
        )
        self.bob = User.objects.create_user(
            username="Bob",
            password="yomama69"
        )
        self.charlie = User.objects.create_user(
            username="Charlie",
            password="yomama69"
        )

        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Space movie",
            release_date="2014-11-07",
            duration=169,
        )

        self.seat1 = Seat.objects.create(
            movie=self.movie,
            seat_number="A1",
            is_booked=False,
        )

        self.seat2 = Seat.objects.create(
            movie=self.movie,
            seat_number="A2",
            is_booked=False,
        )

    #function to test that booking a seat creates a booking and marks the seat as booked
    def test_book_seat_creates_booking_and_marks_seat_booked(self):
        self.client.login(username="Alice", password="yomama69")

        response = self.client.post(
            reverse("book_seat", args=[self.movie.id, self.seat1.id])
        )

        self.assertEqual(response.status_code, 302)

        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.is_booked)

        self.assertEqual(Booking.objects.count(), 1)

        booking = Booking.objects.get()
        self.assertEqual(booking.user, self.alice)
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat1)

    #function to test that a seat that is already booked cannot be booked again
    def test_cannot_book_already_booked_seat(self):
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )
        self.seat1.is_booked = True
        self.seat1.save()

        self.client.login(username="Bob", password="yomama69")

        response = self.client.post(
            reverse("book_seat", args=[self.movie.id, self.seat1.id]),
            follow=True
        )

        self.assertEqual(response.status_code, 200)

        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.is_booked)

        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().user, self.alice)

    #function to test that canceling a booking deletes the booking and frees the seat
    def test_cancel_booking_deletes_booking_and_frees_seat(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )
        self.seat1.is_booked = True
        self.seat1.save()

        self.client.login(username="Alice", password="yomama69")

        response = self.client.post(
            reverse("cancel_booking", args=[booking.id])
        )

        self.assertEqual(response.status_code, 302)

        self.seat1.refresh_from_db()
        self.assertFalse(self.seat1.is_booked)
        self.assertEqual(Booking.objects.count(), 0)

    #function to test that the booking history page only shows the logged in users bookings
    def test_booking_history_shows_only_logged_in_users_bookings(self):
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )
        self.seat1.is_booked = True
        self.seat1.save()

        Booking.objects.create(
            movie=self.movie,
            seat=self.seat2,
            user=self.bob,
        )
        self.seat2.is_booked = True
        self.seat2.save()

        self.client.login(username="Alice", password="yomama69")

        response = self.client.get(reverse("booking_history"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A1")
        self.assertNotContains(response, "A2")

    #function to test that one user cannot cancel another users booking
    def test_another_user_cannot_cancel_someone_elses_booking(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )
        self.seat1.is_booked = True
        self.seat1.save()

        self.client.login(username="Charlie", password="yomama69")

        response = self.client.post(
            reverse("cancel_booking", args=[booking.id])
        )

        self.assertEqual(response.status_code, 404)

        self.seat1.refresh_from_db()
        self.assertTrue(self.seat1.is_booked)
        self.assertEqual(Booking.objects.count(), 1)

#END INTEGRATION TESTING

#BEGIN INTEGRATION TESTING

class BookingIntegrationTests(APITestCase):
    #function that sets up the starting api test data for movies seats and users
    def setUp(self):
        self.alice = User.objects.create_user(
            username="Alice",
            password="yomama69"
        )
        self.bob = User.objects.create_user(
            username="Bob",
            password="yomama69"
        )

        self.movie = Movie.objects.create(
            title="Inception",
            description="Dream movie",
            release_date="2010-07-16",
            duration=148,
        )

        self.seat1 = Seat.objects.create(
            movie=self.movie,
            seat_number="B1",
            is_booked=False,
        )

        self.seat2 = Seat.objects.create(
            movie=self.movie,
            seat_number="B2",
            is_booked=False,
        )

    #function to test that the movies api endpoint returns a successful response and movie data
    def test_movies_api_returns_movie_list(self):
        response = self.client.get("/api/movies/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Inception")

    #function to test that the seats api endpoint returns seat data and booking status
    def test_seats_api_returns_seat_list(self):
        response = self.client.get("/api/seats/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn("seat_number", response.data[0])
        self.assertIn("is_booked", response.data[0])

    #function to test that the bookings api endpoint requires login
    def test_bookings_api_requires_authentication(self):
        response = self.client.get("/api/bookings/")

        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]
        )

    #function to test that a logged in user can create a booking through the api
    def test_create_booking_api_creates_booking(self):
        self.client.login(username="Alice", password="yomama69")

        response = self.client.post(
            "/api/bookings/",
            {
                "movie": self.movie.id,
                "seat": self.seat1.id,
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)

        booking = Booking.objects.get()
        self.assertEqual(booking.user, self.alice)
        self.assertEqual(booking.movie, self.movie)
        self.assertEqual(booking.seat, self.seat1)

    #function to test that the bookings api shows the logged in users booking history
    def test_bookings_api_returns_logged_in_users_bookings(self):
        Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )

        self.client.login(username="Alice", password="yomama69")
        response = self.client.get("/api/bookings/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    #function to test that deleting a booking through the api removes the booking
    def test_delete_booking_api_removes_booking(self):
        booking = Booking.objects.create(
            movie=self.movie,
            seat=self.seat1,
            user=self.alice,
        )

        self.client.login(username="Alice", password="yomama69")
        response = self.client.delete(f"/api/bookings/{booking.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)
