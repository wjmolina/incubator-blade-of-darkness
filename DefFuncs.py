import Bladex
import GameText
import Objects
import Sounds

GameText.MapList["PILOT"] = ["pilot"]

Bladex.SetSun(1, -20, 20, -20)

# pilot_doors

SND_SLIDE_GATE = Sounds.CreateEntitySound(
    "..\\..\\Sounds\\rastrillo.wav", "GateSlideSound"
)
SND_SLIDE_GATE.MaxDistance = 20000
SND_SLIDE_GATE.MinDistance = 2000

SND_HIT_GATE = Sounds.CreateEntitySound(
    "..\\..\\Sounds\\golpe-metal-mediano.wav", "GateHitSound"
)
SND_HIT_GATE.MaxDistance = 20000
SND_HIT_GATE.MinDistance = 2000

WHILE_SND = (SND_SLIDE_GATE, SND_SLIDE_GATE)
END_SND = ("", SND_HIT_GATE)

DISPLACEMENT = (2200, 600)
OPEN_VECTORS = (0.0, -1.0, 0.0), (0.0, -1.0, 0.0)
CLOSE_VECTORS = (0.0, 1.0, 0.0), (0.0, 1.0, 0.0)
VEL_INIT = (2000, 2000)
VEL_FIN = (2000, 2000)


def move_gate(gate, is_open=1):
    if is_open == 1:
        movement_vectors = OPEN_VECTORS
    else:
        movement_vectors = CLOSE_VECTORS

    Objects.NDisplaceObject(
        gate,
        DISPLACEMENT,
        movement_vectors,
        VEL_INIT,
        VEL_FIN,
        (),
        WHILE_SND,
        END_SND,
    )


def awaken_enemy_1(sector_index, entity_name):
    if entity_name == "Player1":
        enemy_1 = Bladex.GetEntity("enemy_1")
        enemy_1.Blind = 0
        enemy_1.Deaf = 0
        sector_1 = Bladex.GetSector(18190.1692214, -1067.67050036, 1278.97962967)
        sector_1.OnEnter = ""
