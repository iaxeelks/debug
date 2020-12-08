import os, time

def debug(msg):
	fecha_hora = (time.strftime("%M:%d:%Y"), time.strftime("%H:%M:%S"))
	debug_msg = fecha_hora[0] + " - " + fecha_hora[1] + ": " + msg
	os.system(f"echo {debug_msg} >> debug.txt")
