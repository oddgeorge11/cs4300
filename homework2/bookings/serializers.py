from rest_framework import serializers
from .models import Movie, Seat, Booking


#class to convert movie objects into json and back again for the api
class MovieSerializer(serializers.ModelSerializer):
    #class to define which model and fields this serializer should use
    class Meta:
        model = Movie
        fields = "__all__"


#class to convert seat objects into json and back again for the api
class SeatSerializer(serializers.ModelSerializer):
    #class to define which model and fields this serializer should use
    class Meta:
        model = Seat
        fields = "__all__"


#class to convert booking objects into json and back again for the api
class BookingSerializer(serializers.ModelSerializer):
    #field that prevents the client from choosing the booking owner manually
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    #class to define which model and fields this serializer should use
    class Meta:
        model = Booking
        fields = "__all__"
