__author__ = 'kosttek'


class Config():

    username = None
    password = None
    databasename = None
    tables = None
    attributes = None
    point_event_attributes = None
    sqltype = None
    dbfile = None

    @staticmethod
    def load_config(configclass):
        Config.sqltype = configclass.sqltype
        if Config.sqltype == "mysql":
            Config.username = configclass.username
            Config.password = configclass.password
            Config.databasename = configclass.databasename
        elif Config.sqltype == "sqlite":
            Config.dbfile = configclass.dbfile
        Config.tables = configclass.tables
        Config.attributes = configclass.attributes
        Config.point_event_attributes = configclass.point_event_attributes