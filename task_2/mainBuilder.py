from BuilderPlayer import BuilderPlayer
from DirectorPlayer import DirectorPlayer
from SpeciesPlayer import SpeciesPlayer
from ClassPlayer import ClassPlayer

if __name__ == "__main__":
    builder = BuilderPlayer()
    director = DirectorPlayer()

    director.builder = builder
    director.build_player_human_magic()

    resPerson = builder.player.build()
    director.viewPlayer(resPerson)
    director.saveFilePlayer(
        resPerson,
        'person_1',
        'D:/Cogs_Project/VSU_SIA-COD_2026_ZAY/task_2'
    )
