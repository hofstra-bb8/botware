from pygame import mixer # Load the required library

from dual_mc33926_rpi import motors, MAX_SPEED
import time

mixer.init()
mixer.music.load('./bb8.mp3')
mixer.music.play()

try:
  motors.enable()
  motors.setSpeeds(MAX_SPEED, MAX_SPEED)
  time.sleep(10)
  
finally:
  motors.setSpeeds(0,0)
  motors.disable()