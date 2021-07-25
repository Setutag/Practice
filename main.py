import cv2
import numpy as np
from PIL import ImageGrab
from ursina import *
import math

def analize():
    signal = 'no signal'
    screenshot = ImageGrab.grab()
    rgb_img = np.array(screenshot)
    bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)

    lb = np.array([30, 70, 70])
    ub = np.array([120, 255, 120])

    mask = cv2.inRange(hsv_img, lb, ub)

    M = cv2.moments(mask, 1)

    if M['m00'] != 0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

        cv2.circle(bgr_img, (x, y), 25, (0, 0, 225), -1)

        if x < 810:
            cv2.putText(bgr_img, 'Left', (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            signal = 'left'
        if x > 1110:
            cv2.putText(bgr_img, 'Right', (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
            signal = 'right'
        if (x > 810) & (x < 1110):
            cv2.putText(bgr_img, 'Fine', (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            signal = 'forward'

    else:
        signal = 'stop'

    cv2.rectangle(bgr_img, (0, 0), (1920, 1080), (0, 0, 0), 70)
    cv2.line(bgr_img, (960, 0), (960, 1080), (0, 0, 255), 5)
    cv2.line(bgr_img, (810, 0), (810, 1080), (0, 0, 255), 5)
    cv2.line(bgr_img, (1110, 0), (1110, 1080), (0, 0, 255), 5)

    cv2.imshow('Res', cv2.resize(bgr_img, (480, 270)))

    return signal
class Scene(Entity):
    def __init__(self):
        super().__init__()
        self.model = 'quad'
        self.texture = 'map'
        self.scale_x = 45
        self.scale_y = 45
        self.rotation_x = 90
        self.position = (0, 0, 0)


class Player(Entity):
    def __init__(self):
        super().__init__()
        camera.position = [-16.741268157958984, 4, -16.832792282104492]
        camera.rotation_x = 45
        camera.rotation_y = 361.1536560058594
        self.a = 4.732460266782609 #angle
        self.r = 0.025 #radius
        self.v = [1, 1] #velocity
        self.l = 0.5 #distance between wheels
        self.k = 30 #rotation coefficient
        self.s = 20 #speed
        self.pic = analize()

    def update(self):

        if self.pic == 'forward':
            camera.x += self.s * (self.r / 2) * (self.v[0] + self.v[1]) * math.cos(self.a)
            camera.z -= self.s * (self.r / 2) * (self.v[0] + self.v[1]) * math.sin(self.a)

        if self.pic == 'right':
            self.a += math.radians((self.r / self.l) * (self.k * self.v[1] - self.v[0]))
            camera.rotation_y += (self.r / self.l) * (self.k * self.v[1] - self.v[0])

        if self.pic == 'left':
            self.a += math.radians((self.r / self.l) * (self.v[1] - self.k * self.v[0]))
            camera.rotation_y += (self.r / self.l) * (self.v[1] - self.k * self.v[0])

        if held_keys['r']:
            self.a = 4.732460266782609
            camera.x = -16.741268157958984
            camera.z = -16.832792282104492
            camera.rotation_y = 361.1536560058594

       # if held_keys['t']:
       #    print('X: ', camera.x, '\nZ: ', camera.z, '\nAngle:', camera.rotation_y, ' ', self.a )

        self.pic = analize()



app = Ursina()

bot = Player()
land = Scene()
music = Audio ('melody', loop = True, multiplier = 1)

app.run()
