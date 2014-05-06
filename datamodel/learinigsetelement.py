from main.Config import Config
from copy import deepcopy

__author__ = 'kosttek'


class LearningSetElement():

    def __init__(self):
        self.values = dict()
        self.attributes = Config.attributes
        self.point_event_attributes = Config.point_event_attributes
        self.date = None

        for type_obj in self.attributes:
            self.values[type_obj] = type_obj()

    def __getitem__(self, arg):
        return self.values[arg]

    def clone(self):
        return deepcopy(self)

    def clear_from_point_events(self):
        for point_event in self.point_event_attributes:
            self[point_event].set_value_none()

