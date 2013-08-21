
import glob
import numpy as np
import scipy as sc
import re
import scipy.integrate as integrate
#import scipy.signal as signal
# import scipy.stsci.convolve as ss
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('PSD')
ax.set_xlabel('frequency')

list2 = glob.glob('*.xyz')
leg = []
for filename in list2:
	f = open(filename, 'r')
	a = f.readlines()
	# print(a)
	p = re.sub(",", ".", a[7])
	p = p.split(' ')
	# print (p[6])
	xs = float(p[6])*10000
	
	ys = xs

	b = a[14:len(a)]
	
	k = 0
	d = np.zeros ((480, 640), dtype=float)
	for i in range(480):
		for j in range(640):
			p = re.sub(",", ".", b[k])
			p = p.split(' ')
			try:
				d[i, j] = round(float(p[2]),7) #* 1000
			except ValueError:
				d[i, j] = 0
			k = k + 1
	# print d[1,1]
# 	d = np.zeros ((200,200), dtype = float)
# 	for i in range(200):
# 		for j in range(200):
# 			d[i,j]=d2[i,j]
	
	psdx = np.zeros([d.shape[0], d.shape[1] / 2])
	
	for i in np.arange(1., d.shape[0], 0.1):
		pp = d[i, :]
		
		psd1 = (abs(sc.fft(pp) * np.conjugate(sc.fft(pp)))) 
		
		psdx[i, :] = psd1[0:d.shape[1] / 2]
	
	psdx = sum(psdx, 0) * (xs) / (5 * psdx.shape[1] ** 2)

	vx = np.arange((1 / (xs * d.shape[1])), (1 / xs), (2 / (xs * d.shape[1]))) 
	
	
	
#	psdy = np.zeros([d.shape[1],480]) # d.shape[0] / 2])
#	#print psdy.shape
#	for i in np.arange(1., d.shape[1]):
#		pp2 = d[:, i]
#		for i in range(480):
#			pp[i]=pp2[i]
#		psd1 = (abs(sc.fft(pp) * np.conjugate(sc.fft(pp))))
#		psdy[i, :] = psd1[0:480]#d.shape[0] / 2]
#	psdy = sum(psdy, 0) * (ys) / (5 * psdy.shape[1] ** 2)
#	#vy = np.arange((1 / (ys * d.shape[0])), (1 / ys), (2 / (ys * d.shape[0])))
#	vy = np.arange(0,480)
#	
#	interp = signal.cspline1d(psdy, 7.0)
	
	
	psdy=np.zeros([d.shape[1],d.shape[0]/2])
	for i in np.arange(1.,d.shape[1]):
		pp = d[:,i]
		psd1 = (abs(sc.fft(pp)*np.conjugate(sc.fft(pp))))
		psdy[i,:] = psd1[0:d.shape[0]/2]
	psdy = sum(psdy,0)*(ys)/(5*psdy.shape[1]**2)
	vy = np.arange( (1/(ys*d.shape[0])), (1/ys), (2/(ys*d.shape[0])) )
	
	minX=5
	maxX=10 ** 2
	
	
	
	ax.loglog(vx, psdx)
	#plt.xlim(minX,maxX)
	#ax.loglog(vy,interp)
	leg.append(filename + '_x')
	ax.loglog(vy,psdy)
	leg.append(filename+'_y')
	ax.legend(filename)
	rms = integrate.trapz(psdx, fieldX=vx)
	rms2 = integrate.trapz(psdy, fieldX=vy)
	# print('/n')
	print filename, rms, rms2
	
list2 = glob.glob('*.dat')

for filename in list2:	
	xrs = np.loadtxt(filename)
	xrsx = xrs[:, 0]
	xrsy = xrs[:, 1]
	ax.loglog(xrsx, xrsy, 'o-')
	leg.append(filename)

ax.legend(leg, 'upper right')
# test1=open("c:/01/test2.txt", 'w')
# test1.write(str(psdx))
# test1.write(str(vx))

# test1.write(str(rms))


# test1.close
plt.show()
