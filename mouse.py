# main.py -- put your code here!
import pyb
switch = pyb.Switch()
accel = pyb.Accel()
hid = pyb.USB_HID()

while True:
    if switch():
        hid.send((1, accel.x(), -accel.y(), 0))
    else:
        hid.send((0, accel.x(), -accel.y(), 0))
    pyb.delay(10)


