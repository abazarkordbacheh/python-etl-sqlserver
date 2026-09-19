from abc import ABC, abstractmethod


class ConnectionBase(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_connection(self):
        pass
