from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BookingViewSet,
    MovieViewSet,
    SeatViewSet,
    movie_list_page,
    seat_booking_page,
    book_seat_action,
    booking_history_page,
    cancel_booking_action,
)

#router to automatically create REST API endpoints for our viewsets
router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("seats", SeatViewSet, basename="seat")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    #function to show the home page with the list of movies
    path("", movie_list_page, name="movie_list"),

    #function to show the seat map for a specific movie
    path("movies/<int:movie_id>/seats/", seat_booking_page, name="seat_booking"),

    #function to book a specific seat for a specific movie
    path(
        "movies/<int:movie_id>/seats/<int:seat_id>/book/",
        book_seat_action,
        name="book_seat",
    ),

    #function to show the logged in users booking history
    path("my-bookings/", booking_history_page, name="booking_history"),

    #function to cancel one booking and free the seat again
    path("my-bookings/<int:booking_id>/cancel/", cancel_booking_action, name="cancel_booking"),

    #function to expose the REST API under the /api/ prefix
    path("api/", include(router.urls)),
]
