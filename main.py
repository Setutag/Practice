from ursina import *
import math

class Scene(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.texture = 'race_line'
        self.scale_x = 45
        self.scale_y = 45
        self.rotation_x = 90
        self.position = (0, 0, 0)

class Player(Entity):
    def __init__(self, setpos):
        super().__init__()
        self.model = 'sphere'
        self.texture = 'me.png'
        self.scale = (7, 7, 7)
        self.rotation_y = -90
        self.position = (setpos[0], self.scale_y/2, setpos[1])
        self.angle = math.radians(-90)
        self.wheel_radius = 0.025
        self.velocity = [1, 1]
        self.wheel_between_length = self.scale_z

    def update(self):
        if held_keys['w']:
            self.x += 2*(self.wheel_radius / 2) * (self.velocity[0] + self.velocity[1]) * math.cos(self.angle)
            self.z -= 2*(self.wheel_radius / 2) * (self.velocity[0] + self.velocity[1]) * math.sin(self.angle)

        if held_keys['d']:
            self.angle += math.radians((self.wheel_radius/self.wheel_between_length)*(151*self.velocity[1] - self.velocity[0]))
            #self.rotation_y += (self.wheel_radius/self.wheel_between_length)*(151*self.velocity[1] - self.velocity[0])

        if held_keys['a']:
            self.angle += math.radians((self.wheel_radius/self.wheel_between_length)*(self.velocity[1] - 151*self.velocity[0]))
            #self.rotation_y += (self.wheel_radius/self.wheel_between_length)*(self.velocity[1] - 151*self.velocity[0])
        self.rotation_y += 2*(self.wheel_radius/self.wheel_between_length)*(self.velocity[1] - 151*self.velocity[0])


app = Ursina()
landscape = Scene()
#audio = Audio('melody.wav', loop = True)
bot = Player((0, -17))
camera.position = (0, 30, -100)
camera.rotation_x = 15

app.run()
