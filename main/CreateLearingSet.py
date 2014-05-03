from conffiles.defaultconfigvalues import ConfigVals
from datamodel import Screen, NetworkTrafficSent, ApplicationStart, Network, Weather, NetworkTrafficRec, Time
from datamodel.parserdictionary import UpdateElement
from main.Config import Config
from main.SortedRawAwareEvents import SortedRawAwareEvents
from datamodel.learinigsetelement import LearningSetElement
from main.preparearff import PrepareArff
from parser.Parser import Parser

__author__ = 'kosttek'

class CreateLearningSet():





    def create(self):
        Config.load_config(ConfigVals)
        sortedEvents = SortedRawAwareEvents()
        sortedEvents.get_events_from_MySQL()
        print "sorted"
        parser = Parser()
        result = list()

        temp_learning_element = LearningSetElement()

        for event in sortedEvents:
            learning_element = temp_learning_element.clone()

            parsed_events = parser.parse_event(event)
            UpdateElement.update(learning_element,parsed_events)

            result.append(learning_element)
            temp_learning_element = learning_element

        return result


if __name__ == "__main__":
    cls = CreateLearningSet()
    result = cls.create()
    sample = result[10000]
    sample = LearningSetElement()
    print len(result)

    print Screen.values_set
    print NetworkTrafficSent.values_set
    print NetworkTrafficRec.values_set
    print ApplicationStart.values_set
    print Network.values_set
    print Weather.values_set
    print Time.values_set

    pa = PrepareArff()
    pa.prepare_association_file("aware_association",result)



