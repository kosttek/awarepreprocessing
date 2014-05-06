__author__ = 'kosttek'

from datamodel.types import Time, Weather, Screen, ApplicationStart, Network, NetworkTrafficRec, NetworkTrafficSent


class ConfigVals():
    sqltype="mysql"

    tables = [
        "applications_history",
        "network",
        "network_traffic",
        "plugin_weather_current",
        "screen"
    ]

    databasename = "aware"

    username = "aware"

    password = "awarepass"

    attributes=[
        Time,
        Weather,
        Screen,
        ApplicationStart,
        Network,
        NetworkTrafficRec,
        NetworkTrafficSent
    ]

    point_event_attributes=[
        ApplicationStart
    ]