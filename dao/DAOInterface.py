from abc import abstractmethod, ABC


class DAOInterface(ABC):
    @abstractmethod
    def selectAll(self):
        pass

    @abstractmethod
    def select(self, model):
        pass

    @abstractmethod
    def insert(self, model):
        pass

    @abstractmethod
    def update(self, model):
        pass

    @abstractmethod
    def delete(self, model):
        pass
