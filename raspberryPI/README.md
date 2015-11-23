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
9. Install tools needed to compile astronomy applications
    sudo apt-get install texinfo autoconf automake make libtool
10. Reboot the Pi
11. Install Servo signal tools
    mkdir servo_support
    wget abyz.co.uk/rpi/pigpio/pigpio.zip
    unzip pigpio.zip
    cd PIGPIO
    make
    sudo make install
    cd ~/
12. Install astronomy applications
    mkdir Astro
    cd Astro
    wget http://downloads.sourceforge.net/project/libnova/libnova/v%200.15.0/libnova-0.15.0.tar.gz
    tar -xzvf libnova-0.15.0.tar.gz
    cd libnova-0.15.0/
    # Clean up some compile issues
    autoreconf --force --install
    ./configure
    make
    sudo make install
13. Add pigpio to startup.
    edit /etc/rc.local
    Add "sudo pigpiod" at the bottom of the file

------------------
#Parts List
This is the list of parts I used in building out this device.

1. [OLED Display](https://www.adafruit.com/products/938)
2. [Navigation Switch](https://www.sparkfun.com/products/8236)
3. [Stepper Motor HAT](https://www.adafruit.com/products/2348)
4. [Slip Ring](https://www.adafruit.com/product/736)
5. [Stepper motor](https://www.adafruit.com/product/324)
6. [Servo](https://www.adafruit.com/product/155)
7. [Raspberry PI](https://www.adafruit.com/products/1914)
