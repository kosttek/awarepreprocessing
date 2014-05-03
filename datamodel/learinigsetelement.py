__author__ = 'kosttek'

from types import Weather, Time, Screen, ApplicationStart,  Network, NetworkTrafficRec, NetworkTrafficSent
from copy import deepcopy


class LearningSetElement():

    def __init__(self):
        LearningSetElement.point_events_get_methods = [LearningSetElement.get_application_start]
        self.time = Time()
        self.weather = Weather()
        self.screen = Screen()
        self.application_start = ApplicationStart()
        self.network = Network()
        self.network_traffic_rec = NetworkTrafficRec()
        self.network_traffic_sent = NetworkTrafficSent()

    def clone(self):
        return deepcopy(self)

    def clear_from_point_events(self):
        for method in self.point_events_get_methods:
            method(self).set_value_none()

    def get_time(self):
        return self.time

    def get_weather(self):
        return self.weather

    def get_screen(self):
        return self.screen

    def get_network(self):
        return self.network

    def get_network_traffic_rec(self):
        return self.network_traffic_rec

    def get_network_traffic_sent(self):
        return self.network_traffic_sent

    def get_application_start(self):
        return self.application_start

