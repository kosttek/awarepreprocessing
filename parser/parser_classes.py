import datetime
from datamodel import ParserDict

__author__ = 'kosttek'


class GenericParser():

    def parse(self, event):
        changed_events_list = list()
        changed_events_list.append(self.parse_time(event))
        value = self.parse_value(event)
        if isinstance(value, list):
            changed_events_list += value
        else:
            changed_events_list.append(value)
        result = dict()
        for changed_event in changed_events_list:
            result[changed_event[0]] = changed_event[1]
        return result

    def parse_time(self,event):
        '''return  tuples (time,value)'''
        day_of_week = datetime.datetime.fromtimestamp(event.timestamp/1000).weekday()
        return (ParserDict.time, day_of_week)

    #abstract
    def parse_value(self,event):
        '''ABSTRACT return list of tuples (time,value) or single tuple'''
        pass


class ApplicationHistoryParser(GenericParser):

    table = "applications_history"

    def parse_value(self,event):
        return (ParserDict.application_start,event.application_name)


class NetworkParser(GenericParser):

    table = "network"

    def parse_value(self,event):
        return (ParserDict.network,event.network_subtype)

class NetworkTrafficParser(GenericParser):

    table = "network_traffic"

    def parse_value(self,event):

        type = event.network_type
        traffic_rec_val = event.double_received_bytes
        traffic_sent_val = event.double_sent_bytes

        result_rec = str(type) + self.getVal(traffic_rec_val) +"_REC"
        result_sent = str(type)+self.getVal(traffic_sent_val)+"_SENT"

        return [(ParserDict.network_traffic_rec,result_rec),(ParserDict.network_traffic_sent,result_sent)]

    def getVal(self,intval):
        if intval > 30000:
            return "BIG"
        elif intval == 0:
            return "ZERO"
        else:
            return "SMALL"

class WeatherParser(GenericParser):

    table = "plugin_weather_current"

    def parse_value(self,event):
        return (ParserDict.weather,event.weather_name)

class ScreenParser(GenericParser):

    table = "screen"

    screen_status = {0: "OFF", 1: "ON", 2: "LOCKED", 3: "UNLOCKED"}

    def parse_value(self,event):
        return (ParserDict.screen,self.screen_status[event.screen_status])



