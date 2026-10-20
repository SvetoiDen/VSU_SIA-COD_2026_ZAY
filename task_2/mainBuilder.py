from BuilderPlayer import BuilderPlayer
from DirectorPlayer import DirectorPlayer
from SpeciesPlayer import SpeciesPlayer
from SkillsPlayer import SkillsPlayer
from ClassPlayer import ClassPlayer

if __name__ == "__main__":
    builder = BuilderPlayer()
    director = DirectorPlayer()

    director.builder = builder
    director.build_player_human_magic()
    builder.skillsPlayer(SkillsPlayer.NON_SKILL)
    builder.skillsPlayer(SkillsPlayer.NON_SKILL, 4)
    builder.skillsPlayer(SkillsPlayer.WIZARD_SKILL)


    resPerson = builder.player.build()
