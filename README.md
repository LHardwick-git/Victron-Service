# Victron-Service
Temperature and Humidity d-bus services for Victron GX

This is a service to publish temperature type data onto the DBus ov VenusOs running
on a Victron GX device.

I develop on a Raspberry Pie 3B+, this service was last tested on VenusOS 2.60 in November 2020.
I use these service on my NArrowboat Lady's Smock, I am based in the UK.

IF all goes well with the install when youstart up your GX device the service will start.
The data is published with a type of "Temperature" and will be available:
  1) On the VenusOS DBus API
  2) On the GX console
  3) On the Victron VRM - if you have this configured for you instllation
  
 Note, only services of path type "Temperature" will be displayed on the console and VRM
 If you modify the service to pubish data as a dpath that is of a different type
 it will only be available via the DBus and will not appear on the console or VRM.
 
 
