from conffiles.defaultconfigvalues import ConfigVals

__author__ = 'kosttek'
from datamodel.types import *
from datamodel.learinigsetelement import *


class PrepareArff():


    def __init__(self):
        PrepareArff.variables_set = Config.attributes

    def prepare_association_file(self, relation_name, data):
        f = open(relation_name+".arff","w")
        self.write_relation(f, relation_name)
        self.write_atributes(f)
        self.write_boolean_values(f,data)


    @staticmethod
    def write_relation(file_des, relation_name):
        file_des.write("@relation "+relation_name+"\n")




    @staticmethod
    def write_atributes(file_des):
        set = PrepareArff.variables_set
        file_des.write("\n")
        for var in PrepareArff.variables_set:
            PrepareArff.write_var(file_des,var)

    @staticmethod
    def write_var(file_des, var):
        var_filtered = PrepareArff.filterVar(var.__name__)
        new_val_set=set()
        for val in var.values_set:
            new_val_set.add(PrepareArff.filterVar(val))
        file_des.write("@attribute "+var_filtered+" "+PrepareArff.write_set_values(new_val_set)+"\n")

    @staticmethod
    def write_set_values(set):

        try:
            result = ""
            for val in set:
                result+=PrepareArff.filterVar(val)+","
            result=result[0:-1]
            return "{"+result+"}"
        except TypeError:
            return "{}"



    @staticmethod
    def filterVar(var):
        var = str(var)
        var = var.replace("%","<pr>")
        var = var.replace("\n","")
        var = var.replace("\\n","")
        var = var.replace("\\r","")
        var = var.replace("\"","||")
        var = var.replace("\'","|")
        var = var.replace("{","((")
        var = var.replace("}","))")
        var = var.replace("\t","_tab_")
        var_no_withespaces = var.replace(" ","_")
        var_no_comma = var_no_withespaces.replace(",",";")
        return var_no_comma

    @staticmethod
    def write_boolean_values(file_des,vals):
        file_des.write("\n")
        file_des.write("\n")
        file_des.write("@data\n")
        for element in vals:
            PrepareArff.write_learning_element(file_des,element)


    @staticmethod
    def get_learning_element(element):
        result = ""
        for variable in PrepareArff.variables_set:
            raw_value = element[variable].get_value()
            if raw_value is None:
                raw_value="?"
            val = PrepareArff.filterVar(raw_value)
            result += val+","
        result = result[0:-1]
        return result


    @staticmethod
    def write_learning_element(file_des,element):
        result = PrepareArff.get_learning_element(element)
        file_des.write(result+"\n")


if __name__ == "__main__":
    Config.load_config(ConfigVals)
    data = list()
    el = LearningSetElement()
    el[Network].set_value("WIFI")
    el2 = LearningSetElement()
    el2[Network].set_value("MODEM\nMM")
    el3 = LearningSetElement()
    el3[Screen].set_value("ON")


    data.append(el)
    data.append(el2)
    data.append(el3)
    pa = PrepareArff()
    pa.prepare_association_file("test",data)