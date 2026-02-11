---
title: "Configuring a Static IP Address on the Raspberry Pi"
date: 2017-02-02
categories: 
  - "piwars2017"
tags: 
  - "linux"
  - "networking"
  - "piwars2017"
  - "raspberry-pi"
  - "wifi"
  - "wlan0"
slug: "configuring-static-ip-address-raspberry-pi"
---

A static IP address will ensure that the Raspberry Pi will always have the same IP address. Without a static IP address the DHCP service on your router will randomly assign IP addresses from its IP range. A fixed IP address will make it easier to remotely connect to the Raspberry Pi.

In this example, the IP address for the Raspberry Pi will be set to 192.168.0.17.

- Edit the interfaces file by entering the following command at the terminal.
    
    ```
    >sudo nano /etc/network/interfaces
    ```
    
- Change the eth0 settings to  
    
    ```
    iface wlan0 inet static
    address 192.168.0.17
    netmask 255.255.255.0
    gateway 192.168.0.1
    broadcast 192.168.0.255
    ```
    
- Press control + o to save
- reboot by entering the command  
    
    ```
    sudo shutdown -r now
    ```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/configuring-static-ip-address-raspberry-pi](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/raspberry-pi/configuring-static-ip-address-raspberry-pi)
