from abc import ABC, abstractmethod


class Builder(ABC):

    @property
    @abstractmethod
    def player(self) -> None:
        pass

    @abstractmethod
    def speciesPlayer(self) -> None:
        pass

    @abstractmethod
    def classPlayer(self) -> None:
        pass

    @abstractmethod
    def statsPlayer(self) -> None:
        pass

    @abstractmethod
    def skilsPlayer(self) -> None:
        pass

    @abstractmethod
    def viewPlayer(self) -> None:
        pass

    @abstractmethod
    def updateSkils(self) -> None:
        pass

    @abstractmethod
    def updateState(self) -> None:
        pass