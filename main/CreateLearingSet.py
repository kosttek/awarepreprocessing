from conffiles.defaultconfigvalues import ConfigVals

from datamodel.parserdictionary import UpdateElement
from main.Config import Config
from main.SortedRawAwareEvents import SortedRawAwareEvents
from datamodel.learinigsetelement import LearningSetElement
from main.preparearff import PrepareArff
from parser.Parser import Parser

__author__ = 'kosttek'

class CreateLearningSet():





    def create(self,configfile):
        Config.load_config(configfile)
        sortedEvents = SortedRawAwareEvents()
        sortedEvents.get_events_from_MySQL()
        print "sorted"
        parser = Parser()
        result = list()

        temp_learning_element = LearningSetElement()
        i = 0
        for event in sortedEvents:
            learning_element = temp_learning_element.clone()

            parsed_events = parser.parse_event(event)
            UpdateElement.update(learning_element,parsed_events)

            result.append(learning_element)
            temp_learning_element = learning_element

            i+=1
            print i
        return result


if __name__ == "__main__":
    cls = CreateLearningSet()
    result = cls.create(ConfigVals)
    print len(result)

    pa = PrepareArff()
    pa.prepare_association_file("aware_association",result)



