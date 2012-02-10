# -*- coding: iso-8859-1 -*-
from _core import *

"""Defining astronomical constants defined in the keplerian_toolbox file astro_constants.h"""
AU = _core._get_AU()
DAY2SEC = _core._get_DAY2SEC()
DAY2YEAR = _core._get_DAY2YEAR()
DEG2RAD = _core._get_DEG2RAD()
EARTH_VELOCITY = _core._get_EARTH_VELOCITY()
G0 = _core._get_G0()
MU_SUN = _core._get_MU_SUN()
RAD2DEG = _core._get_RAD2DEG()
SEC2DAY = _core._get_SEC2DAY()

epoch.epoch_type = _core._epoch_type


"""Detecting Installed Extensions"""
# Fill up the __extensions__ variable with all detected extensions

__extensions__ = {'matplotlib': False, 'mplot3d': False,'pygmo': False}
try:
	import matplotlib
	__extensions__['matplotlib']=True
except:
	pass
try:
	import mpl_toolkits.mplot3d
	__extensions__['mplot3d']=True
except:
	pass
try:
	import PyGMO
	__extensions__['pygmo']=True
except:
	pass
	
#Importing various utilities
if (__extensions__['matplotlib'] == True):
	from _plots import *

