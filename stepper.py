import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

StepPins = [11,12,15,16]

for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

StepCounter = 0
WaitTime = 0.005

StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [0,1,0,1]
Seq1[1] = [0,1,1,0]
Seq1[2] = [1,0,1,0]
Seq1[3] = [1,0,0,1]

Seq = Seq1
StepCount = StepCount1

while 1==1:
 
  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      print " Step %i Enable %i" %(StepCounter,xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)
 
  StepCounter += 1
 
  # If we reach the end of the sequence
  # start again
  if (StepCounter==StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount
 
  # Wait before moving on
  time.sleep(WaitTime)

