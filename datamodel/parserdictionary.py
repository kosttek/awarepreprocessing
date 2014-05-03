from main import Config

__author__ = 'kosttek'
from learinigsetelement import LearningSetElement


class ParserDict():

    def __init__(self):
        pass

    time = 'time_key'
    application_start = 'application_start_key'
    screen = 'screen_key'
    weather = 'weather_key'
    network = 'network_key'
    network_traffic_rec = 'network_traffic_key_rec',
    network_traffic_sent = 'network_traffic_key_sent'

    dataTypeMap = {
        time: LearningSetElement.get_time,
        application_start: LearningSetElement.get_application_start,
        screen: LearningSetElement.get_screen,
        weather: LearningSetElement.get_weather,
        network: LearningSetElement.get_network,
        network_traffic_rec: LearningSetElement.get_network_traffic_rec,
        network_traffic_sent: LearningSetElement.get_network_traffic_sent
    }


class UpdateElement():
    '''
    parsed_event -> dict() {time:"morning",network:"MOBILE", ...}
    '''
    @staticmethod
    def update(element, parsed_event):
        element.clear_from_point_events()
        for key, val in parsed_event.iteritems():
            method = ParserDict.dataTypeMap[key]
            variable_instance = method(element)
            variable_instance.set_value(val)


