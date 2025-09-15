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
    plane_2 = set_center(netsblox.common.decode_image('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').convert('RGBA'), (0.0, 0.0))
    plane_3 = set_center(netsblox.common.decode_image('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').convert('RGBA'), (0.0, 0.0))
    plane_1 = set_center(netsblox.common.decode_image('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C7fbvboJW1HY5hMz2KLrOmWjU/TZysM4X6CaC7tN6uY4rovIDkdkUKP9fCbI5j43Jq77V+66665Ef739GLSfbmjoXYiCxGqIkx0KCt5E4tHuQvYul+ShSNXV1QdsNhvpqrUcfn80Gu32er057Zr89kN1zS6Lu1MQ9U6TcPO7h//eINy0XDJJ8JEjR7Bz5068+OKLeOmllzIeR9u66Obfettd2LfPTPuofgrqUNwhn4Xt1/LUqbq6umZd1w8KQupUV1W1n+O43pmZjT2uhSRclHTP48/Ej5Pe3759O+z2wrMa09PTbGbddvsne3d3XN83MXElL2thLWztZx8CaGho+C7HcT0UHauoKGyvNenYqSkjZj01NUWzrmgx06355M4kyLLMvCqa3rSAFoLFRSPQpBkeWlED0lue4Pn5+TP0HDd66AZZJ/lieXk5saApivG0wmJiyxNMIMuFFk4iamZmJmdJpoUt6ab00M1CkbHldbCJmpqavYIg9NH+CHrqH+lk09lJR5otTubi8enp6b9ACfCBIXgF5fX19f1kVdAbIjo950a2OBFLKoVAls709PSGHoT/m0Sw6U2SyqDKmjUTb+z5m7JcErXwQScYJurr6+/WNC1lX7Eoin5VVfs2aofniv8Hk54FuffBZIoAAAAASUVORK5CYII=').convert('RGBA'), (0.0, 0.0))
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
globals.gravitational_constant = -9.8

@netsblox.graphical.stage
class stage(netsblox.graphical.StageBase):
    pass
    @onmouse('up')
    def my_onup(self, x, y):
        if(globals.launching):
            globals.launching = False
            globals.flying = True
            globals.speed = [(globals.charge) * np.cos(globals.angle), (globals.charge) * np.sin(globals.angle)]
            globals.charge = 0
            nb.send_message('animate')
        
    @onstart()
    def run(self):
        step = 1
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
        self.costume = images.plane_1  
        self.starting = (-425, 0)
        self.pos = (self.starting[0], self.starting[1])    
        pass
        
    @onmouse('down')
    def my_onmouse(self, x, y):
        while _yield_(not globals.flying): 
            globals.launching = True
            globals.charge = np.min([100, np.sqrt((self.starting[0] - stage.mouse_pos[0])**2 + (self.starting[1] - stage.mouse_pos[1])**2)])
            globals.angle = np.pi + np.arctan2(stage.mouse_pos[1] - self.starting[1], stage.mouse_pos[0] - self.starting[0])
            if np.abs(self.starting[0] - stage.mouse_pos[0]) < 30 and np.abs(self.starting[1] - stage.mouse_pos[1]) < 30:
                self.pos = (stage.mouse_pos[0], stage.mouse_pos[1])
            else:
                self.pos = (self.starting[0] - np.cos(globals.angle) * 30, -np.sin(globals.angle) * 30)
            self.heading = 90 - np.rad2deg(globals.angle)
    
        
        
    @nb.on_message('animate')
    def my_on_message_2(self):
        wait = .125
        while _yield_(globals.flying):
            self.costume = images.plane_1         
            time.sleep(wait)
            if not globals.flying:
                break
            self.costume = images.plane_2         
            time.sleep(wait)
            if not globals.flying:
                break
            self.costume = images.plane_3         
            time.sleep(wait)
            if not globals.flying:
                break
            self.costume = images.plane_2         
            time.sleep(wait)
            
sprite = sprite()

@netsblox.graphical.sprite
class aimingDots(netsblox.graphical.SpriteBase):
    pass
    @onstart()
    def my_onstart(self):
        self.visible = False
        
        self.pen_size = 10
        
        self.local_angle = globals.angle;
        self.local_charge = globals.charge;
        
        while _yield_(True):        
            if self.local_angle != globals.angle or self.local_charge != globals.charge:
                
                self.local_angle = globals.angle;
                self.local_charge = globals.charge;
                
                if globals.charge == 0:
                    stage.clear_drawings()
                    break
                    
                self.renderKinematics(5)
                
                
    def renderKinematics(self, iterations):
        stage.clear_drawings()
        
        for i in map(_yield_, range(1, iterations + 1)):
            self.drawDotAtPoint(
                sprite.x_pos + math.cos(self.local_angle) * self.local_charge * i,
                sprite.y_pos + math.sin(self.local_angle) * self.local_charge * i + (0.5) * (globals.gravitational_constant) * (i ** 2),
                12 - i
            )
                
    def drawDotAtPoint(self, x, y, size):
        self.drawing = False
        self.pen_color = 'black'
        self.pen_size = size
        self.pos = (x, y)
        
        self.drawing = True
        
        self.pos = (x, y)
        
        self.drawing = False
        self.drawing = False
        self.pen_color = 'white'
        self.pen_size = size - 2
        self.pos = (x, y)
        
        self.drawing = True
        
        self.pos = (x, y)
    
            
aimingDots = aimingDots()

start_project()