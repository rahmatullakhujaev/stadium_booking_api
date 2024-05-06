from rest_framework import serializers
from st_booking_api.booking.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Booking
        exclude = ['user', 'status']

        def create(self, validated_data):
            user = self.context['request'].user
            validated_data['user'] = user
            return super().create(validated_data)


class BookingSerializerForStadiumOwner(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    end_time = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Booking
        exclude = ['user']

        def create(self, validated_data):
            user = self.context['request'].user
            validated_data['user'] = user
            return super().create(validated_data)
