---
title: "Stepper Motor Control Service"
date: 2017-02-04
categories: 
  - "piwars2017"
tags: 
  - "piwars2017"
  - "python-2"
  - "raspberry-pi"
  - "stepper-motor"
slug: "stepper-motor-control-service"
---

[![](images/20170202_220206-300x169.jpg)](images/20170202_220206.jpg)Today I have been busy developing a stepper motor service class. The service class will allow the Team Seaford robot to play crazy golf.  
  
  
  
  

```
import RPi.GPIO as GPIO
import time

class ServiceStepMotor:

  PinPhase1 = 14
  PinPhase2 = 15
  PinPhase3 = 17
  PinPhase4 = 16
  
  Steps = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
  ]

  StepIndex = 0
  
  MotorOnTime = 0.05  
  
  ## Constructor
  # @param self Class pointer
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    self.SetPinToOutput(self.PinPhase1)
    self.SetPinToOutput(self.PinPhase2)
    self.SetPinToOutput(self.PinPhase3)
    self.SetPinToOutput(self.PinPhase4)
    pass

  ## Change pin type to output
  # @param self Class pointer
  # @param pin Pin Number  
  def SetPinToOutput(self, pin):
    GPIO.setup(pin,GPIO.OUT)
    self.Off(pin)
    pass
  
  ## Turn output pin On
  # @param self Class pointer
  # @param pin Pin Number  
  def On(self, pin):
    print "On="+str(pin)
    GPIO.output(pin,1)
    pass

  ## Turn output pin off
  # @param self Class pointer
  # @param pin Pin Number
  def Off(self, pin):
    GPIO.output(pin, 0)
    pass
  
  ## Change the output state of a pin
  # @param self Class pointer
  # @param PinNumber GPIO pin number
  # @param PinValue The new value for the GPIO pin  
  def ChangeOuput(self, PinNumber, PinValue):
    GPIO.output(PinNumber, PinValue)  
    pass
  
  ## Move stepper motor
  # @param self Class Pointer
  # @param Direction 1 = Forwards, 0 = Backwards
  def Step(self, direction):
    
    # Increment / decrement step count based on direction
    if (direction):
      # forward
      self.StepIndex += 1
    else:
      # backwards
      self.StepIndex -= 1
    
    # Check if we have passed the end of the steps list  
    if (self.StepIndex >= len(self.Steps)):
      self.StepIndex = 0
    
    # Check if we have reached the start of the steps list
    if (self.StepIndex < 0):
      self.StepIndex = len(self.Steps) - 1
      
    # Set output pin states
    print "StepIndex=" + str(self.StepIndex)
    phase = self.Steps[self.StepIndex]
    self.ChangeOuput(self.PinPhase1, phase[0])
    self.ChangeOuput(self.PinPhase2, phase[1])
    self.ChangeOuput(self.PinPhase3, phase[2])
    self.ChangeOuput(self.PinPhase4, phase[3])
    #for i in range(len(phase)):
    #  self.On(phase[i])
    
    # Delay while motor turns
    time.sleep(self.MotorOnTime)
    pass

```

The example code below shows how to use the stepper motor service class.

```
import ServiceStepMotor
sm = ServiceStepMotor.ServiceStepMotor()

print"Start"

print "Step forwards 10 steps"
for i in range(10):
  print "Step forward " + str(i)
  sm.Step(True)
  
print "Step backwards 10 steps"
for i in range(10):
  print "Step backward " + str(i)
  sm.Step(False)
  
print "Finish" 

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/stepper-motor-control-service](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/stepper-motor-control-service)
