from abc import ABC, abstractmethod


class ModelsInterface(ABC):
    @abstractmethod
    def makeDict(self):
        pass
