from main.Config import Config
from copy import deepcopy

__author__ = 'kosttek'


class LearningSetElement():
    '''
    valies is dictionary of kay = Type and value Type() from types see GenericType
    set g
    '''


    def __init__(self):
        self.attributes = Config.attributes
        self.point_event_attributes = Config.point_event_attributes
        self.values = dict()


        for type_obj in self.attributes:
            self.values[type_obj] = type_obj()

    def __getitem__(self, arg):
        return self.values[arg]

    def clone(self):
        return deepcopy(self)

    def clone2(self):

        result = LearningSetElement()
        for type , val in self.values.iteritems():
            '''type is GenericType()'''
            val_new = type()
            val_new.set_value(val.get_value())
            result.values[type]=val_new
        return result

    def clear_from_point_events(self):
        for point_event in self.point_event_attributes:
            self[point_event].set_value(None)

