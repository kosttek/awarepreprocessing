import datetime
#from datamodel import Time, NetworkTrafficSent, Network, NetworkTrafficRec, ApplicationStart, Weather, Screen
#from datamodel import types

__author__ = 'kosttek'


class GenericParser():

    def parse(self, event):
        changed_events_list = list()
        changed_events_list.append(self.parse_day(event))
        changed_events_list.append(self.parse_daytime(event))
        value = self.parse_value(event)
        if isinstance(value, list):
            changed_events_list += value
        else:
            changed_events_list.append(value)
        result = dict()
        for changed_event in changed_events_list:
            result[changed_event[0]] = changed_event[1]
        return result

    def parse_day(self,event):
        '''return  tuples (time,value)'''
        from datamodel.types import Time
        day_of_week = datetime.datetime.fromtimestamp(event.timestamp/1000).weekday()
        return (Time, day_of_week)

    def parse_daytime(self,event):
        '''return  tuples (time,value)'''
        from datamodel.types import DayTime
        hour_of_day = datetime.datetime.fromtimestamp(event.timestamp/1000).hour

        if hour_of_day >= 20 or hour_of_day <= 1:
            result = "evening"
        elif hour_of_day <= 6:
            result = "night"
        elif hour_of_day <= 11:
            result = "morning"
        else:
            result = "day" # 11 - 20
        return (DayTime, result)


    #abstract
    def parse_value(self,event):
        '''ABSTRACT return list of tuples (time,value) or single tuple'''
        pass


class ApplicationHistoryParser(GenericParser):

    table = "applications_history"

    def parse_value(self,event):
        from datamodel.types import ApplicationStart
        return (ApplicationStart,event.application_name)


class NetworkParser(GenericParser):

    table = "network"

    state_dict ={0:"OFF",1:"ON"}

    def parse_value(self,event):
        from datamodel.types import Network
        state = self.state_dict[event.network_state]
        result = event.network_subtype +"_"+state
        return (Network,result)


#todo remove
class NetworkTrafficParser(GenericParser):

    table = "network_traffic"

    def parse_value(self,event):
        from datamodel.types import NetworkTrafficSent, NetworkTrafficRec
        type = event.network_type
        traffic_rec_val = event.double_received_bytes
        traffic_sent_val = event.double_sent_bytes

        result_rec = str(type) + self.getVal(traffic_rec_val) +"_REC"
        result_sent = str(type)+self.getVal(traffic_sent_val)+"_SENT"

        return [(NetworkTrafficRec,result_rec),(NetworkTrafficSent,result_sent)]

    def getVal(self,intval):
        if intval > 30000:
            return "BIG"
        elif intval == 0:
            return "ZERO"
        else:
            return "SMALL"

class NetworkAllTrafficParser(GenericParser):

    table = "network_traffic"

    def parse_value(self,event):
        from datamodel.types import NetworkTrafficWifi, NetworkTrafficMobile
        type = event.network_type

        traffic_rec_val = event.double_received_bytes
        traffic_sent_val = event.double_sent_bytes

        result = self.getVal(traffic_rec_val+traffic_sent_val)
        #wifi
        if type == 1:
            return (NetworkTrafficWifi,result)

        #mobile
        elif type == 2:
            return (NetworkTrafficMobile,result)
        else:
            return (NetworkTrafficWifi,"unknown_source_"+result)

    def getVal(self,intval):
        if intval > 60000:
            return "BIG"
        elif intval > 3000:
            return "SMALL"
        elif intval == 0:
            return "ZERO"
        else:
            return "MINIMAL"

class WeatherParser(GenericParser):

    table = "plugin_weather_current"

    def parse_value(self,event):
        from datamodel.types import Weather
        return (Weather,event.weather_name)

class ScreenParser(GenericParser):

    table = "screen"

    screen_status_switch = {0: "OFF", 1: "ON", 2: "LOCKED", 3: "UNLOCKED"}

    def parse_value(self,event):
        from datamodel.types import Screen
        return (Screen,self.screen_status_switch[event.screen_status])


class ApplicationForegroundParser(GenericParser):

    table = "applications_foreground"

    def parse_value(self,event):
        from datamodel.types import ApplicationForeground
        return (ApplicationForeground,event.application_name)


class ActivityParser(GenericParser):

    table = "plugin_google_activity_recognition"

    def parse_value(self,event):
        from datamodel.types import Activity
        return (Activity,event.activity_name)


class CallParser(GenericParser):

    table = "calls"

    def parse_value(self,event):
        from datamodel.types import Call
        return (Call,event.call_type)


class SmsParser(GenericParser):

    table = "messages"

    def parse_value(self,event):
        from datamodel.types import Sms
        return (Sms,event.message_type)


