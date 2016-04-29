from pygame import mixer # Load the required library

from dual_mc33926_rpi import motors, MAX_SPEED
import time
mixer.init()
sound = mixer.music.Sound('./bb8 - he he he ho.wav')

def make_noise():
  sound.play()

  while mixer.get_busy():
    sleep(1)

def forward(seconds):
  motors.setSpeeds(seconds, seconds)

def reverse(seconds):
  motors.setSpeeds(-seconds, -seconds)


try:
  motors.enable()

  forward(10)
  make_noise()
  reverse(2)
  make_noise()
  
finally:
  motors.setSpeeds(0,0)
  motors.disable()