from abc import abstractmethod, ABC


class DAOInterface(ABC):
    @abstractmethod
    def selectAll(self):
        pass

    @abstractmethod
    def select(self, part):
        pass

    @abstractmethod
    def insert(self, part):
        pass

    @abstractmethod
    def update(self, part):
        pass

    @abstractmethod
    def delete(self, part):
        pass
