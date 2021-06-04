import Bladex

from DefFuncs import awaken_enemy_1

sector_1 = Bladex.GetSector(18190.1692214, -1067.67050036, 1278.97962967)
sector_1.OnEnter = awaken_enemy_1
