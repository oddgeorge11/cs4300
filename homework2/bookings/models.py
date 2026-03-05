from django.db import models
from django.contrib.auth.models import User


#class to represent a movie that users can book seats for
class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()

    #function to return a readable string for the admin and debug output
    def __str__(self):
        return self.title


#class to represent a seat for a specific movie
class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats", null=True, blank=True)
    seat_number = models.CharField(max_length=10)
    is_booked = models.BooleanField(default=False)

    #class to enforce database rules like unique seat numbers per movie
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["movie", "seat_number"], name="unique_seat_per_movie")
        ]

    #function to return a readable string for the admin and debug output
    def __str__(self):
        if self.movie is None:
            return self.seat_number
        return f"{self.movie.title} - {self.seat_number}"


#class to represent a booking that connects a user to one seat for one movie
class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="bookings")
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    booking_date = models.DateTimeField(auto_now_add=True)

    #function to return a readable string for the admin and debug output
    def __str__(self):
        return f"{self.user.username} booked {self.seat.seat_number} for {self.movie.title}"
