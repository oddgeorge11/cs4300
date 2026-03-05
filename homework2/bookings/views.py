from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from rest_framework import viewsets

from .models import Booking, Movie, Seat
from .serializers import BookingSerializer, MovieSerializer, SeatSerializer


#class to provide CRUD operations for movies through the REST API
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


#class to provide CRUD operations for seats through the REST API
class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


#class to provide CRUD operations for bookings through the REST API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


#function to render the main page that shows all movies
def movie_list_page(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})


#function to render the seat booking page for a specific movie
def seat_booking_page(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie).order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats
    })


#function to book a seat when the user clicks the book button
@login_required
@require_POST
def book_seat_action(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)

    if seat.is_booked:
        messages.error(request, f"Seat {seat.seat_number} is already booked.")
        return redirect("seat_booking", movie_id=movie_id)

    seat.is_booked = True
    seat.save()

    Booking.objects.create(
        movie=movie,
        seat=seat,
        user=request.user,
    )

    messages.success(request, f"Booked seat {seat.seat_number} for {movie.title}.")
    return redirect("booking_history")


#function to cancel a booking and free the seat again
@login_required
@require_POST
def cancel_booking_action(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    seat = booking.seat
    seat.is_booked = False
    seat.save()

    booking.delete()

    messages.success(request, f"Canceled booking for seat {seat.seat_number}.")
    return redirect("booking_history")


#fnuction to show the booking history page for the logged in user
@login_required
def booking_history_page(request):
    bookings = (
        Booking.objects.filter(user=request.user)
        .select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})
