from math import pow

import Actions
import Bladex
import EnemyTypes
import ItemTypes

enemy_1 = Bladex.CreateEntity(
    "enemy_1", "Great_Ork", 18190.1692214, -1067.67050036, 1278.97962967, "Person"
)
enemy_1.Angle = 1.66235867261
enemy_1.Blind = 1
enemy_1.Deaf = 1
enemy_1.ActionAreaMin = pow(2, 0)
enemy_1.ActionAreaMax = pow(2, 1)
EnemyTypes.EnemyDefaultFuncs(enemy_1)

weapon_1 = Bladex.CreateEntity("weapon_1", "Gladius", 0, 0, 0, "Weapon")
ItemTypes.ItemDefaultFuncs(weapon_1)

shield_1 = Bladex.CreateEntity("shield_1", "Escudo5", 0, 0, 0)
ItemTypes.ItemDefaultFuncs(shield_1)

Actions.TakeObject(enemy_1.Name, weapon_1.Name)
Actions.TakeObject(enemy_1.Name, shield_1.Name)
