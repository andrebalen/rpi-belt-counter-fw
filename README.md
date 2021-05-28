
<img src="https://github.com/andrebalen/rpi-belt-counter-fw/blob/main/logo.png" alt="Logo" align="right" />

## rpi-belt-counter-fw

 everything you need to use a camera and count bags of onions or potatoes on the cargo belt, used in industrial and rural environments.

## dependencies

hw - raspberry pi3 (aka rpi) , camera and 16gb sdcard

the best way to configure the software is using ssh on rpi, to do this u need a client in your computer and
start this service on rpi ( sudo raspi-config )


sw - connect your rpi and run this commands on terminal
 
```

sudo apt-get install aptitude git
sudo aptitude install python3-pip python3-numpy python3-picamera python3-pandas python3-opencv libatlas-base-dev -y 

TODO: 
sudo aptitude install  python3-imutils -y


```

## how to install

connect your raspberry pi with a `plain raspian version`, using `pi` as user and a default pw

 clone this repo: 

	
```

 git clone https://github.com/andrebalen/rpi-belt-counter-fw.git


```

solving the dependencies ( as listed below) and change the source of video 



 run :

``` 

sh run


 ```


## other troubleshoting


some troubles can be caused by a low swap memory, to solve this: 


'''


 sudo nano /etc/dphys-swapfile

'''


change the amount of swap to 1024 like:


'''

#CONF_SWAPSIZE=100
CONF_SWAPSIZE=1024

'''

save and restart the swap service with:


'''


sudo /etc/init.d/dphys-swapfile restart



'''



to see how much free mem just type:


'''


 free -m


'''


results in:


'''

 pi@rasp:~ $ free -m


              total        used        free      shared  buff/cache   available

Mem: 434 21 359 5 53 360
 Swap: 1023 0 1023

'''



Locale config, avoid errors

Digite:

'''

 sudo raspi-config

'''

in: 

localization options/Change locale change to: : pt_BR UTF8 UTF8

change timezoneâchange to: Sao Paulo

Change Wifi country change to: selecione BR

to this make effect: 


'''

sudo reboot

''' 


OpenCV3 research:

https://cadernodelaboratorio.com.br/instalando-python3-e-opencv3-no-raspbian-stretch-lite/




we are constantly improving

