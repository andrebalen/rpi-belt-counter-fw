
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
sudo aptitude install python-pip
pip install pandas
pip install numpy

```

add this to PATH:  /home/pi/.local/bin

TODO: need some talent here ...

```
echo '/home/pi/.local/bin' >

```

## how to install

connect your raspberry pi with a `plain raspian version`, using `pi` as user and a default pw

 clone this repo: 
	
	```

	 git clone https://github.com/andrebalen/rpi-belt-counter-fw.git

	 ```

 solving the dependencies and change the source of video 



 run :

	``` 

	sh run


	 ```

we are constantly improving

