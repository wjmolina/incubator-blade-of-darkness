import Bladex
import Levers
import Objects
import Sparks

from DefFuncs import move_gate

gate_1 = Bladex.CreateEntity(
    "gate_1", "Rastrillo10", 5284.0770509, -2366.91968365, 1506.1086106, "Physic"
)
gate_1.Scale = 0.8
gate_1.Orientation = (0.500000059605, 0.500000059605, -0.500000059605, 0.499999821186)
gate_1.Frozen = 1
gate_1 = Sparks.SetMetalSparkling(gate_1.Name)

gate_1_din = Objects.CreateDinamicObject(gate_1.Name)

gate_1_lever = Levers.PlaceLever(
    "gate_1_lever",
    Levers.LeverType3,
    (4864.20330698, -1495.59549893, 3494.25367907),
    (
        0.500000059605,
        0.500000059605,
        0.499999910593,
        -0.499999970198,
    ),
    0.8,
)
gate_1_lever.mode = 0
gate_1_lever.OnTurnOnFunc = move_gate
gate_1_lever.OnTurnOnArgs = (gate_1_din, 1)
gate_1_lever.OnTurnOffFunc = move_gate
gate_1_lever.OnTurnOffArgs = (gate_1_din, 0)
