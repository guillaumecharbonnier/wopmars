"""
Module containing the FooWrapper1 class
"""
import os
import time

from matplotlib.compat import subprocess

from wopmars.framework.database.tables.ToolWrapper import ToolWrapper


class FooWrapper12(ToolWrapper):
    """
    This class has been done for example/testing purpose.
    Modifications may lead to failure in tests.
    """
    __mapper_args__ = {'polymorphic_identity': "FooWrapper12"}

    def specify_output_file(self):
        return ["output1"]

    def specify_output_table(self):
        return ["FooBase"]
