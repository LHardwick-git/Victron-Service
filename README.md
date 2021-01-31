# Victron-Service
Temperature and Humidity d-bus services for Victron GX  
Oh! and also now reading the Raspberry Pi CPU temperature which is why I was asked to post this !

This is a service to publish temperature type data onto the DBus of VenusOs running on a Victron GX device.  
Note: Currently this will not display the CPU temperature on Venus GX, only on RPi.

I develop on a Raspberry Pi 3B+, this service was last tested on VenusOS 2.60 in November 2020.
I use these service on my Narrowboat Lady's Smock, I am based in the UK.

If all goes well with the install when youstart up your GX device the service will start.
The data is published with a type of "Temperature" and will be available:
  1) On the VenusOS DBus API
  2) On the GX console
  3) On the Victron VRM - if you have this configured for you installation
  
 Note, only services of path type "Temperature" will be displayed on the console and VRM
 If you modify the service to pubish data as a path that is of a different type
 it will only be available via the DBus and will not appear on the console or VRM.
 
INSTRUCTIONS
1) Download the GitHub repo, probably by hitting the green  (V Code) button on GITHub

2) Copy the dbus-i2c directory onto the VenusOS filessystem as /opt/victronenergy/dbus-i2c  
   cp -r <your location>/dbus-i2c /opt/victronenergy/dbus-i2c
  
3) create a symlink from /service/dbus-i2c to /opt/victronenergy/dbus-i2c/service  
   ln -s /opt/victronenergy/dbus-i2c/service /service/dbus-i2c
   
4) Set execute on the following files (Sadly storing things on github does not preserve execute bits)  
   dbus-i2c/i2c.py  
   dbus-i2c/start-i2c.sh  
   dbus-i2c/check-i2c.sh - this is just a simple file you can use to check if the service is running  
   dbus-i2c/service/run  
   /service/dbus-i2c
  
   The command is  
   chmod a+x <filename>
  
There is a good chance the service will start, if not reboot your VenusOS device
You can check in the file /var/log/dbus-i2c to see what is happening as the service starts up

NOTES  
Why is it call dbus-i2c ?    = Well it started as a service to add i2c devices   
    - you will see I have left the code in just commented it out.  
    
What's the adc stuff?        = Victron GX devices only use 5 of the 8 analogue interfaces available  
    - again this is commented out, if you add an 8 channel adc device to a Raspberry pi you can use 
      the extra 3 channels as additional temperature inputs (the VenusOS code will read it's usual 5 inputs)
      In fact there is no conflict as the Venus OS and the service would both quite happily read the 
      same inputs - but you would end up with the same inputs twice in the User Interface.   
      
I added some code recently to enable all the setting of names and temperature offsets as this is supported in VenusOS 2.60.  

There is some other useful stuff (Which answers other questions I have seen on the Victron comunity)
Such as how to have one service publish multiple types of data to the DBus from one file.
      
Hope this all works for you
    
