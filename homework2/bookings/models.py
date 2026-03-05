from django.db import models
from django.contrib.auth.models import User

#create the Movie model
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()  # minutes

    def __str__(self):
        return self.title

#create the Seat model
class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats", null=True, blank=True)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["movie", "seat_number"], name="unique_seat_per_movie")
        ]

    def __str__(self):
        if self.movie is None:
            return self.seat_number
        return f"{self.movie.title} - {self.seat_number}"

#create the Booking model
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)  # one seat can have one booking
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seat.seat_number} for {self.movie.title}"
