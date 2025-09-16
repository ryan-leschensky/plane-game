import netsblox
from netsblox import get_location, get_error, nothrow, Namespace
from netsblox.graphical import *
from netsblox.concurrency import *
globals = Namespace(globals())
nb = netsblox.Client(project_name = """game""", project_id = None)
'A connection to NetsBlox, which allows you to use services and RPCs from python.'
netsblox.graphical._INITIAL_SIZE = (1080, 720)
getattr(netsblox.graphical._get_proj_handle(), '_Project__tk').title(f'PyBlox - {nb.public_id}')
nb.set_room(None)
setup_stdio()
setup_yielding()
import time as _time
def _yield_(x):
    _time.sleep(0)
    return x
from netsblox import sound as Sound
Sound.init()

import time
import math
import random
import numpy as np
import gelidum as _gelidum

class images:
    pass
images = images()
_gelidum.freeze(images, on_freeze = 'inplace')
class sounds:
    pass
sounds = sounds()
_gelidum.freeze(sounds, on_freeze = 'inplace')

globals.charge = 0
globals.angle = np.deg2rad(45)
globals.speed = [0, 0]
globals.x = 0
globals.y = 0
globals.launching = False
globals.flying = False

globals.acceleration = np.array([0, 0])
globals.velocity = np.array([0, 0])

@netsblox.graphical.stage
class stage(netsblox.graphical.StageBase):
    pass
    @onmouse('up')
    def my_onup(self, x, y):
        if(globals.launching):
            globals.launching = False
            globals.flying = True
            nb.send_message('launched')
            globals.speed = [(globals.charge) * np.cos(globals.angle), (globals.charge) * np.sin(globals.angle)]
            globals.charge = 0
            print('mu')
        
    @onstart()
    def run(self):
        step = 0.01
        grav = -9.81
        ar = -7
        while _yield_(True):
            if(globals.flying):
                globals.speed[1] += grav * step
                globals.speed[0] += ar * step
                
                globals.x += globals.speed[0]
                globals.y += globals.speed[1]
            time.sleep(step)
stage = stage()

@netsblox.graphical.sprite
class sprite(netsblox.graphical.SpriteBase):
    pass
    @onstart()
    def my_onstart(self):
        self.starting = (-425, 0)
        self.pos = (self.starting[0], self.starting[1])    
        pass
        
    @onmouse('down')
    def my_onmouse(self, x, y):
        globals.flying = False
        globals.launching = True
        while _yield_((not globals.flying)):  
            globals.charge = np.min([100, np.sqrt((self.starting[0] - stage.mouse_pos[0])**2 + (self.starting[1] - stage.mouse_pos[1])**2)])
            globals.angle = np.pi + np.arctan2(stage.mouse_pos[1] - self.starting[1], stage.mouse_pos[0] - self.starting[0])
            if np.abs(self.starting[0] - stage.mouse_pos[0]) < 30 and np.abs(self.starting[1] - stage.mouse_pos[1]) < 30:
                self.pos = (stage.mouse_pos[0], stage.mouse_pos[1])
            else:
                self.pos = (self.starting[0] - np.cos(globals.angle) * 30, -np.sin(globals.angle) * 30)
            self.heading = 90 - np.rad2deg(globals.angle)
            self.say(np.round(globals.charge))
    
        
    @nb.on_message('launched')
    def my_on_message(self):
        self.say('GO', duration = .0125)
        
        while _yield_(True):
            npSpeed = np.array(globals.speed)
            
            npSpeed = npSpeed / np.linalg.norm(npSpeed)
                    
            angle = np.rad2deg(np.arctan(npSpeed[1] / npSpeed[0]))
            
            if (npSpeed[0] < 0 and npSpeed[1] < 0) :
                angle += 180
            elif (npSpeed[0] < 0):
                angle += 180
                        
            self.heading = 90 - angle
sprite = sprite()

start_project()