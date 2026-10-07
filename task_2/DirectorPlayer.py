from Builder import Builder
from ClassPlayer import ClassPlayer
from SpeciesPlayer import SpeciesPlayer
from ItemsPlayer import ItemsPlayer
from ViewPlayer import ViewPlayer


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
        self.builder.speciesPlayer(SpeciesPlayer.HUMAN_WITH_MAGIC)
        self.builder.classPlayer(ClassPlayer.MAGIC)
        self.builder.balanceHealthMana()
        self.builder.statsPlayer()
        self.builder.manaPlayer(40).healthPlayer(45)
        self.builder.itemAddStartPlayer(ItemsPlayer.ADVENTURE)
        self.builder.itemAddPlayer("мешок говна")
        self.builder.viewPlayer(ViewPlayer.HUMAN)

    def viewPlayer(self, jsData: dict) -> None:
        import json
        print(json.dumps(jsData, indent=2, ensure_ascii=False))

    def saveFilePlayer(self, jsData: dict, name: str, path: str) -> None:
        import json
        with open(f'{path}/{name}.json', 'w', encoding='utf-8') as jFile:
            json.dump(jsData, jFile, indent=3, ensure_ascii=False)
