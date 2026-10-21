from BuilderPlayer import BuilderPlayer
from DirectorPlayer import DirectorPlayer
from SpeciesPlayer import SpeciesPlayer
from SkillsPlayer import SkillsPlayer
from ClassPlayer import ClassPlayer
from PlayerView import PlayerView


def view_player(player: PlayerView):
    print(player.namePlayer)
    print(player.classPlayer)
    print(player.speciesPlayer)
    player.itemsPlayerInfo()
    player.skillsPlayerInfo()
    player.statsPlayerInfo()
    player.viewPlayerInfo()


if __name__ == "__main__":
    builder = BuilderPlayer()
    director = DirectorPlayer()

    director.builder = builder
    director.build_player_human_magic()
    builder.skillsPlayer(SkillsPlayer.NON_SKILL)
    builder.skillsPlayer(SkillsPlayer.NON_SKILL, 4)

    resPerson = builder.player.build()
    view_player(resPerson)

    director.build_player_dfarf_warlor()
    resperson2 = builder.player.build()
    view_player(resperson2)

    director.build_player_elf_bow()
    resperson3 = builder.player.build()
    view_player(resperson3)
