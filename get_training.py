import os;
import sys;
import time;

mydir = os.getcwd();
os.system('faces');
for i in range(40):
	os.system('echo '+'fswebcam'+sys.argv[1]+' '+str(i)+'.jpg')
	time.sleep(.25);
os.system('cd ..')
