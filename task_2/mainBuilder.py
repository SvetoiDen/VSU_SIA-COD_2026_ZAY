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
    print(f"ХП = {player.health} ; МАНА = {player.mana}")
    print(
        f"CИЛА = {player.strength} ; ЛОВКОСТЬ = {player.agility} ; ИНТЕЛЛЕКТ = {player.intelligent} ; СКОРОСТЬ = {player.speed} ;")
    player.itemsPlayerInfo()
    player.skillsPlayerInfo()
    player.viewPlayerInfo()


if __name__ == "__main__":
    builder = BuilderPlayer()
    director = DirectorPlayer()

    director.builder = builder
    director.build_player_human_magic()
    builder.skillsPlayer(SkillsPlayer.NON_SKILL)
    builder.skillsPlayer(SkillsPlayer.NON_SKILL, 4)
    builder.setStrength(5)

    player1 = builder.player.build()
    view_player(player1)

    director.build_player_dfarf_warlor()
    builder.manaPlayer(40)
    player2 = builder.player.build()
    view_player(player2)

    director.build_player_elf_bow()
    player3 = builder.player.build()
    view_player(player3)
