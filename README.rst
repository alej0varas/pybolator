===========
 pybolator
===========

PyBoard emulator

.. note:: very early development state

Features
========

- Run any `main.py` script.
- See what happens to the pyboard in the GUI or
- Run in batch mode and optionally
- Simulate hardware interaction from a script.

Dependencies
============

python3-tk
~~~~~~~~~~

Debian based distros::

  $ apt-get install python3-tk

Run
~~~

GUI
+++
::

  $ PYBOLATOR_MAIN=path/to/main.py python3 pybolator.py

Batch
+++++
::

  $ PYBOLATOR_MAIN=path/to/main.py python3 pybolator.py --batch

optionally pass a `pyb` script
::

  $ PYBOLATOR_MAIN=path/to/main.py python3 pybolator.py --batch tests/script.pyb


Development
~~~~~~~~~~~
::

  $ mkvirtualenv --python=/path/to/python3.x pybolator
  $ workon pybolator
  $ PYBOLATOR_MAIN=test.py python pybolator.py

Supported methods and classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Time related functions
++++++++++++++++++++++

- delay(ms)

Class pyb.Accel
+++++++++++++++

Methods
#######

- accel.x()
- accel.y()

Class pyb.LED
+++++++++++++

Methods
#######

- led.intensity([value])*
- led.off()*
- led.on()*
- led.toggle()*

Class pyb.Switch
++++++++++++++++

Methods
#######

- switch()
- switch.callback(fun)

Unsupported methods and classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- udelay(us)
- millis()
- micros()
- elapsed_millis(start)
- elapsed_micros(start)

Reset related functions
+++++++++++++++++++++++


- hard_reset()
- bootloader()

Interrupt related functions
+++++++++++++++++++++++++++

- disable_irq()
- enable_irq(state=True)

Power related functions
+++++++++++++++++++++++

- freq([sysclk[, hclk[, pclk1[, pclk2]]]])
- wfi()
- stop()
- standby()

Miscellaneous functions
+++++++++++++++++++++++

- have_cdc()
- hid((buttons, x, y, z))
- info([dump_alloc_table])
- main(filename)
- mount(device, mountpoint, \*, readonly=False, mkfs=False)
- repl_uart(uart)
- rng()
- sync()
- unique_id()

Class pyb.Accel
+++++++++++++++

Methods
#######

- accel.filtered_xyz()
- accel.tilt()
- accel.z()

Class pyb.Switch
++++++++++++++++

Methods
#######

- switch()
- switch.callback(fun)

Class pyb.ADC
+++++++++++++

Class pyb.CAN
+++++++++++++

Class pyb.DAC
+++++++++++++

Class pyb.ExtInt
++++++++++++++++

Class pyb.I2C
+++++++++++++

Class pyb.LCD
+++++++++++++

Class pyb.Pin
+++++++++++++

Class pyb.RTC
+++++++++++++

Class pyb.Servo
+++++++++++++++

Class pyb.SPI
+++++++++++++

Class pyb.Timer
+++++++++++++++

Class pyb.UART
++++++++++++++

Class pyb.USB_VCP
+++++++++++++++++

