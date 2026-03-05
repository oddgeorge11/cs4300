from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Booking, Movie, Seat


class BookingUnitTests(TestCase):
    #function that sets up the starting data that every test will use
    def setUp(self):
        self.ali = User.objects.create_user(
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

    #function to test that the booking history page only shows the logged in user's bookings
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

    #function to test that one user cannot cancel another user's booking
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

#END OF UNIT TESTING

#START OF INTEGRATION TESTING


