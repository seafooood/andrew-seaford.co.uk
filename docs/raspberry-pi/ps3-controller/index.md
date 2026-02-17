---
title: "Pairing PS3 Controller with Raspberry Pi"
date: 2017-02-04
---

[![](images/20170204_163209-300x169.jpg)](images/20170204_163209.jpg)We used WIFI to control our 2015 Pi Wars robot. Using WIFI was a big mistake. On the day of the competition, there was too much interference and lag. We have learnt from our mistakes. This time we will be using Bluetooth.

We have connected a USB Bluetooth dongle to the Raspberry Pi and using the instructions below connected a Sony Playstation Six Axis Controller.

- Using micro usb cable plug in the PS3 controller into the raspberry pi
- Enter the command `sudo ./sixpair`
- Disconnect USB cable from PS3 controller
- Enter the command `bluetoothctl`
- Enter the command `devices`
- Enter the command `agenton`
- Enter the command trust followed by the MAC address of the controller. In my case the MAC address is 00:06:F5:C4:01:3b.  
    `trust 00:06:F5:C4:01:3b`
- Disconnect the usb cable
- Press the PS button the top of the controller
- Confirm the new input device has been succesffully added. Enter the command `sudo ls /dev/input` you should see JS0 has been added to the list of input devices


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/ps3-controller](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/ps3-controller)
