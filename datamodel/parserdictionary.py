__author__ = 'kosttek'


class UpdateElement():
    @staticmethod
    def update(element, parsed_event):
        """
        @type parsed_event: dict
        @type element: datamodel.learinigsetelement.LearningSetElement

        parsed_event -> dict() {GenericType,network:"MOBILE", ...}
        """
        element.clear_from_point_events()
        for key, val in parsed_event.iteritems():
            element[key].set_value(val)