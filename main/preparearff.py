__author__ = 'kosttek'
from datamodel.types import *
from datamodel.learinigsetelement import *


class PrepareArff():

    def prepare_association_file(self, relation_name, data):
        f = open(relation_name+".arff","w")
        self.write_relation(f, relation_name)
        self.write_atributes(f)
        self.write_boolean_values(f,data)


    @staticmethod
    def write_relation(file_des, relation_name):
        file_des.write("@relation "+relation_name+"\n")

    variables_set = [Time,Network,NetworkTrafficRec,NetworkTrafficSent,ApplicationStart,Weather,Screen]

    @staticmethod
    def write_atributes(file_des):
        file_des.write("\n")
        for var in PrepareArff.variables_set:
            PrepareArff.write_var(file_des,var)

    @staticmethod
    def write_var(file_des, var):
        var_filtered = PrepareArff.filterVar(var.__name__)
        new_val_set=set()
        for val in var.values_set:
            new_val_set.add(PrepareArff.filterVar(val))
        file_des.write("@attribute "+var_filtered+" "+str(new_val_set)+"\n")

    @staticmethod
    def filterVar(var):
        var = str(var)
        var = var.replace("%","<pr>")
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
    def write_learning_element(file_des,element):
        result = ""
        for variable in PrepareArff.variables_set:
            raw_value = element[variable].get_value()
            val = PrepareArff.filterVar(raw_value)
            result += val+","
        result = result[0:-1]
        file_des.write(result+"\n")


if __name__ == "__main__":
    data = list()
    el = LearningSetElement()
    el.network.set_value("WIFI")
    el2 = LearningSetElement()
    el2.network.set_value("MODEM")
    el3 = LearningSetElement()
    el3.screen.set_value("ON")


    data.append(el)
    data.append(el2)
    data.append(el3)
    pa = PrepareArff()
    pa.prepare_association_file("test",data)