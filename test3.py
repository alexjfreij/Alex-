import serial
import time
import sys
import getopt
import platform
from binascii import b2a_hex
from driver import Driver
from ax12 import *

def is_open(self): 
#      '''If port is opening, return True.'''        
    return self.isOpen() 

if __name__ == "__main__":
    
	ax12 = Driver(9, 38400, False, False)
	robot_id = 1
	#	relay_id = 1
	robot_move = 0
	robot_id3 = 0
	serial_usb=[]
	serial_pow=[]
	sysos = platform
	if sysos.system() == 'Windows':
		print "I am in Win"
#		ser = serial.Serial(9, 38400, 8, 'N', 2)
#		ser = serial.Serial(8, 19200, 8, 'N', 2)
#		serial_usb.append(ser)
 #       pow = serial.Serial(5, 19200, 8 , 'N', 2)
 #       serial_pow.append(pow)
	if sysos.system() =='Linux':
		ser = serial.Serial('/dev/ jttyUSB0', 19200, timeout=10) 
		serial_usb.append(ser)
		pow = serial.Serial('/dev/cu.usbserial', 19200, timeout=10)
		serial_pow.append(pow)
	opts, args = getopt.getopt(sys.argv[2:], "hr:s:", ["usb="])
	for opt, arg in opts:
		if opt == "-s":
			robot_id1 = int(arg)
			robot_val11 = int(arg)
			robot_val12 = int (arg)			
		elif opt == "-r":
			robot_move = int(arg)
 #           setserialport(usb)         
		elif opt == "-e":
			robot_id2= int(arg)
			robot_val21 = int(arg)
			robot_val22 = int (arg)
		elif opt == "-m":
			robot_id3= int(arg)
#			robot_val31 = int(arg)
#			robot_val32 = int (arg)
		elif opt == "-h":
			print "power_relay8_connect.exe [-h] -r relay_id [--rbi relay_board_index_usb] -s "
			sys.exit(0)
#   choose the ids and the value of movements
	relay_board_index = 1
	Interpolation = False
	count = 2
	out_log = 0  # output a return 0 if serial port is Open
	if not is_open: 
		out_log = 1		
	print(out_log)
	speed = input ('enter the speed values 0 to 256:  ')
	pos = input ('enter the position values from 0-512:  ')
	if robot_move == 0:
		print "I am in the set state"
		for servo in range(count):
			for servo in range(count):
				ax12.setReg(servo+1, P_GOAL_SPEED_L, [speed%256, speed>>8])
				ax12.setReg(servo+1, P_GOAL_POSITION_L, [pos%256, pos>>8])
		print ("PASS")
		sys.exit(0)
	print ("FAIL")
