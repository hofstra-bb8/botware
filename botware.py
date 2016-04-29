from pygame import mixer # Load the required library

from dual_mc33926_rpi import motors, MAX_SPEED
import time

mixer.init()
sound = mixer.music.Sound('./bb8 - he he he ho.wav')

sound.play()

while mixer.get_busy():
  sleep(1)

try:
  motors.enable()
  # motors.setSpeeds(MAX_SPEED, MAX_SPEED)
  time.sleep(10)
  
finally:
  motors.setSpeeds(0,0)
  motors.disable()