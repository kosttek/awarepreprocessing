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
        self.add_to_value_set(value)

    def get_value(self):
        return self._value

    def set_value_none(self):
        self._value = None



class Time(GenericType):
    pass


class Network(GenericType):
    pass


class NetworkTrafficRec(GenericType):
    pass


class NetworkTrafficSent(GenericType):
    pass


class Screen(GenericType):
    pass


class Weather(GenericType):
    pass


class ApplicationStart(GenericType):
    pass


