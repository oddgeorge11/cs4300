from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework import viewsets

from .models import Booking, Movie, Seat
from .serializers import BookingSerializer, MovieSerializer, SeatSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


def movie_list_page(request):
    movies = Movie.objects.all().order_by("title")
    return render(request, "bookings/movie_list.html", {"movies": movies})


def seat_booking_page(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all().order_by("seat_number")
    return render(request, "bookings/seat_booking.html", {
        "movie": movie,
        "seats": seats
    })


@login_required
def book_seat_action(request, movie_id, seat_id):
    if request.method != "POST":
        return redirect("seat_booking", movie_id=movie_id)

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


@login_required
def booking_history_page(request):
    bookings = (
        Booking.objects.filter(user=request.user)
        .select_related("movie", "seat")
        .order_by("-booking_date")
    )
    return render(request, "bookings/booking_history.html", {"bookings": bookings})
