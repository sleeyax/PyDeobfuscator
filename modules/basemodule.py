from abc import abstractmethod


class BaseModule:
    """
    A module is basically a class that is called to processes a line of text
    and returns the same line (A), a modified version of that line (B) or None (C)
    Where:
    A = there is nothing to process
    B = the line got processed by the module
    C = the line should not be stored (e.g do not write this line to output)
    """
    @abstractmethod
    def process(self, line):
        pass
