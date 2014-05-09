__author__ = 'kosttek'

from datamodel.types import Time, Weather, Screen, ApplicationStart, Network, NetworkTrafficRec, NetworkTrafficSent, ApplicationForeground, Activity


class ConfigVals():
    sqltype="mysql"

    tables = [
        "applications_history",
        "network",
        "network_traffic",
        "plugin_weather_current",
        "screen",
        "applications_foreground",
        "plugin_google_activity_recognition"
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
        NetworkTrafficSent,
        Activity,
        ApplicationForeground

    ]

    point_event_attributes=[
        ApplicationStart,
        ApplicationForeground
    ]