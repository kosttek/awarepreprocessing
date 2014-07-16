import datetime
from parser.Parser import Parser

__author__ = 'kosttek'
from database import DatabaseAccess
from Config import Config
from conffiles.configvalues2 import ConfigVals

class SortedRawAwareEvents(list):
    '''
    list of events, event is tuple with two keys:
    table : table object from sqlalchemy
    values : tuples of values -> class 'sqlalchemy.util._collections.KeyedTuple'
    '''
    def _get_events_from_MySQL(self,username,password,databasename,tables):
        dbAccess = DatabaseAccess()
        dbAccess.init_mysql(username=username,password=password,databasename=databasename)
        self._get_events(dbAccess,tables)

    def _get_events_from_SQLite(self,filename,tables):
        dbAccess= DatabaseAccess()
        dbAccess.init_sqlite(filename)
        self._get_events(dbAccess,tables)


    def _get_events(self,dbAccess,tables):
        tables = dbAccess.getTables(tables)
        for table in tables:
            events = dbAccess.queryAllFromTable(table)
            events_plus_type= [{'table':table,'values':x} for x in events]
            self += events_plus_type
        self.sort( key=lambda k: k['values'].timestamp)


    def get_events_from_MySQL(self):
        if (Config.username or Config.password or Config.databasename or Config.tables) == None:
            print "Load config file!"
            print Config.username, Config.password, Config.databasename, Config.tables
            return
        self._get_events_from_MySQL(username=Config.username, password=Config.password, databasename=Config.databasename, tables=Config.tables)

    def get_events_from_SQLite(self):
        con = Config
        if (Config.dbfile or Config.tables) == None:
            print "Load config file!"
            print Config.dbfile, Config.tables
            return
        self._get_events_from_SQLite(filename=Config.dbfile, tables=Config.tables)



    def filter_by_occurance_time(self):
        #todo there is much more logs from network screen and network_traffic then application, I mean in some point of time application logs do not occur any more

        pass


if __name__ == '__main__':
    Config.load_config(ConfigVals)
    sortedEvents = SortedRawAwareEvents()
    sortedEvents.get_events_from_MySQL()
    for x in sortedEvents:
        time = datetime.datetime.fromtimestamp(int(x['values'].timestamp/1000)).strftime('%Y-%m-%d %H:%M:%S')
        print x['table'].name+" "+str(time)

    parser = Parser()
    for event in sortedEvents:
        parser.parse_event(event)
