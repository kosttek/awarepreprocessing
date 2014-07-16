from parser.parser_classes import NetworkTrafficParser, NetworkParser, ApplicationHistoryParser, ScreenParser, WeatherParser, ActivityParser, ApplicationForegroundParser, NetworkAllTrafficParser, CallParser, SmsParser

__author__ = 'kosttek'


class GenericType():
    def __init__(self):
        self._value = None
        #something like singleton
        if not hasattr(self.__class__, 'values_set'):
            self.__class__.values_set = set()

    def add_to_value_set(self, val):
        self.values_set.add(val)

    def set_value(self,value):
        self._value = value
        if value != None:
            self.add_to_value_set(value)

    def get_value(self):
        return self._value

    def set_value_none(self):
        self._value = None


class Time(GenericType):
    parser = None


class DayTime(GenericType):
    parser = None


class Network(GenericType):
    parser = NetworkParser


class NetworkTrafficRec(GenericType):
    parser = NetworkTrafficParser


class NetworkTrafficSent(GenericType):
    parser = NetworkTrafficParser


class NetworkTrafficWifi(GenericType):
    parser = NetworkAllTrafficParser


class NetworkTrafficMobile(GenericType):
    parser = NetworkAllTrafficParser


class Screen(GenericType):
    parser = ScreenParser


class Weather(GenericType):
    parser = WeatherParser


class ApplicationStart(GenericType):
    parser = ApplicationHistoryParser


class ApplicationForeground(GenericType):
    parser = ApplicationForegroundParser


class Activity(GenericType):
    parser = ActivityParser


class Call(GenericType):
    parser = CallParser


class Sms(GenericType):
    parser = SmsParser