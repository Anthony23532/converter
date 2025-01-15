class LengthConverter:
    @staticmethod
    def meters_to_kilometers(meters):
        return meters / 1000

    @staticmethod
    def kilometers_to_meters(kilometers):
        return kilometers * 1000

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

class TimeConverter:
    @staticmethod
    def seconds_to_minutes(seconds):
        return seconds / 60

    @staticmethod
    def minutes_to_seconds(minutes):
        return minutes * 60

class SpeedConverter:
    @staticmethod
    def kilometers_per_hour_to_meters_per_second(kph):
        return kph / 3.6

    @staticmethod
    def meters_per_second_to_kilometers_per_hour(mps):
        return mps * 3.6

class VolumeConverter:
    @staticmethod
    def liters_to_milliliters(liters):
        return liters * 1000

    @staticmethod
    def milliliters_to_liters(milliliters):
        return milliliters / 1000
