from BuilderPlayer import BuilderPlayer
from DirectorPlayer import DirectorPlayer
from SpeciesPlayer import SpeciesPlayer
from ClassPlayer import ClassPlayer

if __name__ == "__main__":
    builder = BuilderPlayer()
    director = DirectorPlayer()

    # director.builder = builder
    # director.build_player_human_magic()
    #
    # print(builder.player.build())

    builder
    print(builder.player.build())

    print(builder.player.build())
