---
title: "Moving Forwards"
date: 2017-02-02
categories: 
  - "piwars2017"
tags: 
  - "piwars2017"
  - "python-2"
  - "raspberry-pi"
  - "robot"
slug: "moving-forwards"
---

[![](images/20170204_151013-300x169.jpg)](http://www.andrew-seaford.co.uk/wp-content/uploads/2017/02/20170204_151013.jpg) Our robot is alive and moving. At the heart of the Team Seaford robot control is the ServiceIo class. The ServiceIo class is responsible for controlling the four drive motors. Each motor is connected to a H bridge motor controller. The H bridge controllers require two inputs per motor. The inputs control the direction of travel.

```
import RPi.GPIO as GPIO
import time

class ServiceIo:
  MotorOnTime = 0.01
  
  # GPIO Pin Numbers
  PinDriveFrontLeftForward = 5    # flf
  PinDriveFrontLeftBackward = 13  # flb
  PinDriveFrontRightForward = 11  # frf
  PinDriveFrontRightBackward = 12 # frb
  PinDriveBackLeftForward = 9     # blf
  PinDriveBackLeftBackward = 10   # blb
  PinDriveBackRightForward = 7    # brf
  PinDriveBackRightBackward = 8   # brb

  ## Constructor
  # @param self Class pointer
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    self.SetPinToOutput(self.PinDriveFrontLeftForward)
    self.SetPinToOutput(self.PinDriveFrontLeftBackward)
    self.SetPinToOutput(self.PinDriveFrontRightForward)
    self.SetPinToOutput(self.PinDriveFrontRightBackward)
    self.SetPinToOutput(self.PinDriveBackLeftForward)
    self.SetPinToOutput(self.PinDriveBackLeftBackward)
    self.SetPinToOutput(self.PinDriveBackRightForward)
    self.SetPinToOutput(self.PinDriveBackRightBackward)
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
  
  ## Stop all drive motors
  # @param self Class pointer
  def DriveStop(self):
    self.Off(self.PinDriveFrontLeftForward) 
    self.Off(self.PinDriveFrontLeftBackward)
    self.Off(self.PinDriveFrontRightForward)
    self.Off(self.PinDriveFrontRightBackward)
    self.Off(self.PinDriveBackLeftForward)
    self.Off(self.PinDriveBackLeftBackward)
    self.Off(self.PinDriveBackRightForward)
    self.Off(self.PinDriveBackRightBackward) 
    pass
  
  ## Drive Forward
  # @param self Class pointer
  def DriveForward(self):
    self.On(self.PinDriveFrontLeftForward)
    self.On(self.PinDriveFrontRightForward)
    self.On(self.PinDriveBackLeftForward)
    self.On(self.PinDriveBackRightForward)
    self.Off(self.PinDriveFrontLeftBackward)
    self.Off(self.PinDriveFrontRightBackward)
    self.Off(self.PinDriveBackLeftBackward)
    self.Off(self.PinDriveBackRightBackward)
    time.sleep(self.MotorOnTime)
    pass

  ## Drive Backward
  # @param self Class pointer
  def DriveBackward(self):
    self.On(self.PinDriveFrontLeftBackward)
    self.On(self.PinDriveFrontRightBackward)
    self.On(self.PinDriveBackLeftBackward)
    self.On(self.PinDriveBackRightBackward)
    self.Off(self.PinDriveFrontLeftForward)
    self.Off(self.PinDriveFrontRightForward)
    self.Off(self.PinDriveBackLeftForward)
    self.Off(self.PinDriveBackRightForward)
    time.sleep(self.MotorOnTime)
    pass
    
  ## Drive Left
  # @param self Class pointer
  def DriveLeft(self):
    self.On(self.PinDriveFrontLeftForward)
    self.Off(self.PinDriveFrontLeftBackward)
    self.On(self.PinDriveBackLeftForward)
    self.Off(self.PinDriveBackLeftBackward)
    self.On(self.PinDriveFrontRightBackward)
    self.Off(self.PinDriveFrontRightForward)
    self.On(self.PinDriveBackRightBackward)
    self.Off(self.PinDriveBackRightForward)
    time.sleep(self.MotorOnTime)
    pass
      
  ## Drive Right
  # @param self Class pointer
  def DriveRight(self):
    self.On(self.PinDriveFrontRightForward)
    self.Off(self.PinDriveFrontRightBackward)
    self.On(self.PinDriveBackRightForward)
    self.Off(self.PinDriveBackRightBackward)
    self.On(self.PinDriveFrontLeftBackward)
    self.Off(self.PinDriveFrontLeftForward)
    self.On(self.PinDriveBackLeftBackward)
    self.Off(self.PinDriveBackLeftForward)
    time.sleep(self.MotorOnTime)
    pass

```

The following code show how to use the ServiceIo within a simple program, which responds to user input from the keyboard.

```
import ServiceIo
import time

io = ServiceIo.ServiceIo()
io.DriveStop()

while True:
  mode = raw_input('Direction (f,b,l,r:')
  if (mode == 'f'):
    io.DriveForward()

  if(mode == 'b'):
    io.DriveBackward()

  if(mode=='l'):
    io.DriveLeft()

  if(mode=='r'):
    io.DriveRight()

  time.sleep(2)
  print("off")
  io.DriveStop()

```
