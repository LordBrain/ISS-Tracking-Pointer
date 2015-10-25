#Raspberry Pi ISS (& others) Tracking
This is the Raspberry PI adaptation of the ISS-Tracking-Pointer project by Grady Hillhouse ([github](https://github.com/gradyh/ISS-Tracking-Pointer)).

In order to get this to run on a Raspberry PI has a few pre-reqs that are needed.

1. Make sure the Raspberry Pi is update to date:
  sudo apt-get update
2. Install python
  sudo apt-get install python-dev
  then install it
  sudo python setup.py install
3. Install the GPIO python libraries
  sudo apt-get install python-rpi.gpio
4. Install smbus libraries
  sudo apt-get install python-smbus
5. Install i2c libraries
  sudo apt-get install i2c-tools
6. Run raspi-config to enable SPI and i2c
  sudo raspi-config
  Advanced Option
  A6 & A7
7. Make sure SPI and i2c are not in (or commented out) /etc/modprobe.d/raspi-blacklist.conf
8. Install libnova for astronomy dependancies
  sudo apt-get install libnova-dev
9. Reboot the Pi

------------------
#Parts List
This is the list of parts I used in building out this device.

1. [OLED Display](https://www.adafruit.com/products/938)
2. [5-way Navigation switch](https://www.adafruit.com/product/504)
3. [Stepper Motor HAT](https://www.adafruit.com/products/2348)
4. [Slip Ring](https://www.adafruit.com/product/736)
5. [Stepper motor](https://www.adafruit.com/product/324)
6. [Servo](https://www.adafruit.com/product/155)
7. [Raspberry PI](https://www.adafruit.com/products/1914)
