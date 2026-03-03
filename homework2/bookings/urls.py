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
)

router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("seats", SeatViewSet, basename="seat")
router.register("bookings", BookingViewSet, basename="booking")

urlpatterns = [
    # =========================
    # UI Pages
    # =========================
    path("", movie_list_page, name="movie_list"),
    path("movies/<int:movie_id>/seats/", seat_booking_page, name="seat_booking"),
    path(
        "movies/<int:movie_id>/seats/<int:seat_id>/book/",
        book_seat_action,
        name="book_seat",
    ),
    path("my-bookings/", booking_history_page, name="booking_history"),

    # =========================
    # API
    # =========================
    path("api/", include(router.urls)),
]
