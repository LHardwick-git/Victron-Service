# Victron-Service
Temperature and Humidity d-bus services for Victron GX  
Oh! and also now reading the Raspberry Pi CPU temperature which is why I was asked to post this !
This has been updated for Venus 2.8x and Python 3.

Now with added 1 wire support contributed by Albertbm however read the community
Notes here regarding setting up 1-wire
https://community.victronenergy.com/questions/58792/raspberry-pi-3b-heat-temperature.html
(Look for post from olafd  Feb  11  2022)

This is a service to publish temperature type data onto the DBus of VenusOs running on a Victron GX device.  
Note: Currently this will not display the CPU temperature on Venus GX, only on RPi.

I develop on a Raspberry Pi 3B+, this service was last tested on VenusOS 2.87 in July 2022.
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
  
3) &#35;&#35;  create a symlink from /service/dbus-i2c to /opt/victronenergy/dbus-i2c/service  
   &#35;&#35;  ln -s /opt/victronenergy/dbus-i2c/service /service/dbus-i2c
  For Venus OS 2.8 (using Python 3), this now needs to be. 
  
  mkdir /opt/victronenergy/service/dbus-i2c  
  cp -r /opt/victronenergy/dbus-i2c/service/* /opt/victronenergy/service/dbus-i2c/
   
4) Set execute on the following files (Sadly storing things on github does not preserve execute bits)  
   dbus-i2c/i2c.py  
   dbus-i2c/start-i2c.sh  
   dbus-i2c/check-i2c.sh - this is just a simple file you can use to check if the service is running  
   dbus-i2c/service/run  
   /service/dbus-i2c
  
   The command is  
   chmod a+x <filename>
  
   So do this for each of the files listed above.
  
There is a good chance the service will start, if not reboot your VenusOS device  
You can check in the file /var/log/dbus-i2c to see what is happening as the service starts up
  
5) Go through the file dbus-12c.py and comment out (or uncomment) the setting and  creation of each service.  
  (OK this could now be a single config section in a future release of the services to run as we have so many.)
  
  For now look here and only enable the services you want.

&#35; So the only service left running is the Raspberry pi CPU temperature.  
&#35;  
&#35;    update_i2c()  
&#35;    update_adc()  
    update_rpi()  
&#35;    update_W1()  
    return True  
  
  ALSO below this line:  
&#35; I have commented out the bits that will make new services for i2C and ADC services here  
&#35; If you want to re-enable these you need to uncomment the right lines  
  
  Look for and comment out the 1-wire (unless you have one)  
&#35; dbusservice['W1-temp']     = new_service(base, 'temperature', 'Wire',      '1Wire',  0, 28, 5)  
  and here  
&#35; dbusservice['W1-temp']   ['/ProductName']     = '1Wire Sensor' 
  
6) Currently this will not survive an OS upgrade and will need to be re-installed.  
  There are frameworks from other contributors that csn be used to make sure this   
  PAckage will remain (or be re-installed) after an upgrade.

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
    
