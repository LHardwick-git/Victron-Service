# Victron-Service
Temperature and Humidity d-bus services for Victron GX

This is a repository for a new service directory to be added to Victron GX VenusOS
I develop on a Rspberry 3B+ running venus OS. 

This code release was tested on VenusOS 2.60 in November 2020.

The service is written in Python. 

If all goes well with the install new srevcies will appear:
 1) on the VenusOS DBus
 2) on the GX console
 3) on the virtron VRM for your istallation if you have VRM configured.
 
 Note that only service paths with type "temperature" will automatically appear
 on the console and VRM. If you modify the service to publush other service paths
 they will only be available on the DBus.
