from Builder import Builder
from ClassPlayer import ClassPlayer
from SpeciesPlayer import SpeciesPlayer


class DirectorPlayer:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_player_human_magic(self):
        self.builder.setSpeciesPlayer(SpeciesPlayer.HUMAN)
        self.builder.setClassPlayer(ClassPlayer.MAGIC)
        self.builder.manaPlayer(40)
        self.builder.healthPlayer(10)
        self.builder.statsPlayer()

