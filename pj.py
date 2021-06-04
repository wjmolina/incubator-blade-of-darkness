import Actions
import Basic_Funcs
import Bladex
import ItemTypes

Player1_weapon = Bladex.CreateEntity("Player1_weapon", "Gladius", 0, 0, 0, "Weapon")
ItemTypes.ItemDefaultFuncs(Player1_weapon)

Player1 = Bladex.CreateEntity(
    "Player1", "Knight_N", -1416.19641952, -1063.69443931, 1449.34735809, "Person"
)
Player1.Angle = 4.80641487042
Player1.Data = Basic_Funcs.PlayerPerson(Player1)

Actions.TakeObject(Player1.Name, Player1_weapon.Name)
