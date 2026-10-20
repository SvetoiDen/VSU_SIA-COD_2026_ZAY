from Builder import Builder
from ClassPlayer import ClassPlayer
from SpeciesPlayer import SpeciesPlayer
from ItemsPlayer import ItemsPlayer
from ViewPlayer import ViewPlayer
from SkillsPlayer import SkillsPlayer


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
        self.builder.balanceStatsHealthMana()
        self.builder.manaPlayer(40).healthPlayer(45)
        self.builder.skillsPlayer(SkillsPlayer.WIZARD_SKILL)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 1)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 3)
        self.builder.itemAddStartPlayer(ItemsPlayer.ADVENTURE)
        self.builder.itemAddPlayer("Легендарный айтем")
        self.builder.viewPlayer(ViewPlayer.HUMAN)

    def build_player_elf_bow(self):
        self.builder.speciesPlayer(SpeciesPlayer.ELF)
        self.builder.classPlayer(ClassPlayer.BOW)
        self.builder.balanceStatsHealthMana()
        self.builder.manaPlayer(10).healthPlayer(20)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 3)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 2)
        self.builder.skillsPlayer(SkillsPlayer.PHISYCAL_SKILL)
        self.builder.itemAddStartPlayer(ItemsPlayer.RANGER)
        self.builder.itemAddPlayer("Медальон матери")
        self.builder.viewPlayer(ViewPlayer.ELF)

    def build_player_dfarf_warlor(self):
        self.builder.speciesPlayer(SpeciesPlayer.DFARF)
        self.builder.classPlayer(ClassPlayer.WARLOR)
        self.builder.balanceStatsHealthMana()
        self.builder.manaPlayer(5).healthPlayer(50)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 5)
        self.builder.skillsPlayer(SkillsPlayer.NON_SKILL, 1)
        self.builder.skillsPlayer(SkillsPlayer.PHISYCAL_SKILL)
        self.builder.itemAddStartPlayer(ItemsPlayer.WARLOR)
        self.builder.itemAddPlayer("Кружка пива")
        self.builder.viewPlayer(ViewPlayer.DWARF)
