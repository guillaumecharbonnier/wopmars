"""
Module containing the FooWrapper1 class
"""
import time

from matplotlib.compat import subprocess

from FooBase import FooBase
from wopmars.framework.database.tables.ToolWrapper import ToolWrapper

class FooWrapper5(ToolWrapper):
    """
    This class has been done for example/testing purpose.
    Modifications may lead to failure in tests.
    """
    __mapper_args__ = {'polymorphic_identity': "fooPackage.FooWrapper5"}

    def specify_input_file(self):
        return ["input1"]

    def specify_output_file(self):
        return ["output1"]

    def specify_output_table(self):
        return ["FooBaseP"]

    def run(self):
        print(self.__class__.__name__ + " en cours d'exécution.")
        p = subprocess.Popen(["touch", self.output_file("output1")])
        p.wait()
        # self.session().delete_content(self.output_table("FooBase"))
        for i in range(10):
            f = self.output_table("FooBaseP")(name="Foowrapper5 - " + str(i))
            self.session().add(f)
        self.session().commit()
        time.sleep(1)