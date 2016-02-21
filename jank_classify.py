import scipy as sp;
import numpy as np;
import os;
import sys;
from sklearn import svm
from scipy import misc
import pdb
mydir = os.getcwd();
os.chdir('faces');
mylist = os.listdir(os.getcwd());
tvect = [];
label = [];
for im in mylist:
	imarr = misc.imread(im,flatten = True);
	imarr = misc.imresize(imarr,[640,480]);
	imarr = np.reshape(imarr,[640*480]);
	print np.shape(imarr)
	if(im[0:3] == 'umb'):
		tvect.append(imarr)
		label.append(1);
		print 1
	elif(im[0:3] == 'sta'):
		tvect.append(imarr)
		label.append(2);
		print 2 
	else:
		vect.append(imarr)
		label.append(3);
		print 3


print 'done'


clf = svm.SVC()
while(1):
	os.system('echo '+'fswebcam'+' blah.jpg');
	imarr = misc.imread('blah.jpg',flatten = True);
	imarr = misc.imresize(imarr,[640,480]);
	imarr = np.reshape(imarr,[640*480]);
	print clf.predict(imarr)
	os.system('rm blah.jpg');


#For debugging
#clf = svm.SVC()
#clf.fit(tvect, label)
#for im in mylist:
#	imarr = misc.imread(im,flatten = True);
#	imarr = misc.imresize(imarr,[640,480]);
#	imarr = np.reshape(imarr,[640*480]);
#	print clf.predict(imarr)
#print clf.predict([[2., 2.]])


