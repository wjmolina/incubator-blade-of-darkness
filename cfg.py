import Bladex
import LoadBar

LoadBar.AutoProgressBar(366, "Blade_progress.jpg")

execfile(r"..\..\Scripts\sys_init.py")
Bladex.ReadLevel("pilot.lvl")
execfile(r"..\..\Scripts\BladeInit.py")

execfile("DefFuncs.py")

execfile("pilot_doors.py")
execfile("pilot_enemies.py")
execfile("pilot_triggers.py")
