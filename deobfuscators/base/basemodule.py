from abc import abstractmethod


class BaseModule:
    @abstractmethod
    def process(self, line):
        pass
