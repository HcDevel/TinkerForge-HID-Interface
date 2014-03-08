import uinput

from tinkerforge.ip_connection import IPConnection
from tinkerforge.bricklet_rotary_poti import RotaryPoti

class emulate:
	def poti_cb(self,position):
		print(str(position))
		self.device.emit(uinput.ABS_Z, position) #Setzt den Wert des Joysticks auf den Wert des Potis

	def __init__(self):
		#uinput Bereich
		self.events = (
			uinput.BTN_A, #Es wird mindestens ein Button benötigt (seltsam)
			uinput.ABS_Z + (-150, 150, 0, 0), #Erstellt Joystick Achse Z, kleinster Wert des Potis ist -150, größter Wert ist +150
			)

		self.device = uinput.Device(self.events, "TF Virutal HID Joystick")
		
		#TinkerForge Bereich
		ipcon = IPConnection()
		self.poti = RotaryPoti("aBQ", ipcon) #UID ändern!

		ipcon.connect("127.0.0.1", 4223) #IP / Port anpassen
		self.poti.set_position_callback_period(50)
		self.poti.register_callback(self.poti.CALLBACK_POSITION, self.poti_cb) #Sobald der Callback auslöst wird die Funktion poti_cb aufgerufen

if __name__ == "__main__":
	joy = emulate()
	input ("Press key to exit...\n")
