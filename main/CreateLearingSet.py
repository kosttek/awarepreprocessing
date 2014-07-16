from datetime import datetime
from conffiles.configvalues2 import ConfigVals

from datamodel.parserdictionary import UpdateElement
from datamodel.types import ApplicationForeground, ApplicationStart
from main.Config import Config
from main.SortedRawAwareEvents import SortedRawAwareEvents
from datamodel.learinigsetelement import LearningSetElement
from main.preparearff import PrepareArff
from parser.Parser import Parser

import sys
__author__ = 'kosttek'

class CreateLearningSet():





    def create(self,configfile):
        Config.load_config(configfile)
        sortedEvents = SortedRawAwareEvents()
        sortedEvents.get_events_from_SQLite()
        #sortedEvents.get_events_from_MySQL()
        print "sorted"
        parser = Parser()
        result = list()
        temp_learning_element = LearningSetElement()
        i =0
        for event in sortedEvents:
            learning_element = temp_learning_element.clone2()
            parsed_events = parser.parse_event(event)
            if self.filter_out(parsed_events):
                continue
            UpdateElement.update(learning_element,parsed_events)

            result.append(learning_element)
            temp_learning_element = learning_element
            i += 1
            percent = float(i)/len(sortedEvents)*100

            sys.stdout.write('%s percent \r' %( percent ))
            sys.stdout.flush()

        return result

    filter=\
        [
            (ApplicationStart, 'AWARE'),
            (ApplicationStart, 'Program uruchamiaj?cy'),
            (ApplicationForeground, 'Program uruchamiaj?cy'),
            (ApplicationForeground, 'Interf. sys.'),
            (ApplicationForeground, 'System Android')
        ]

    def filter_out(self, parsed_events):
        for k, v in parsed_events.iteritems():
            for (fk, fv) in self.filter:
                if k == fk and v == fv:
                    return True

        return False


if __name__ == "__main__":
    cls = CreateLearningSet()
    result = cls.create(ConfigVals)
    print len(result)

    pa = PrepareArff()
    pa.prepare_association_file("aware_association",result)



