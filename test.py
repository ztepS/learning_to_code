import glob
import numpy as np
import scipy as sc
import re
#import scipy.stsci.convolve as ss
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylabel('PSD')
ax.set_xlabel('frequency')

list = glob.glob('*.txt')
leg=[]
for filename in list:
    f = open(filename, 'r')
    a = f.readlines()

    # pick up fieldX-scale
    p = re.sub(",",".",a[5])
    p = p.split(' ')
    xs = eval(p[3])*1e-4
    ys = xs
    
    # pick up z-scale 
    p = re.sub(",",".",a[7])
    p = p.split(' ')
    zs = eval(p[3])*1e-3
    
    # pick up data
    b = a[16:len(a)]
    d = np.zeros(( len(b), len(np.fromstring(a[17], dtype=int, sep=' ')) ))
    for n,fieldX in enumerate(b):
        d[n,:]=np.fromstring(fieldX, dtype=int, sep=' ')
    d = d*zs
    
    psdx=np.zeros([d.shape[0],d.shape[1]/2])
    for i in np.arange(1.,d.shape[0]):
        pp = d[i,:]
        psd1 = (abs(sc.fft(pp)*np.conjugate(sc.fft(pp))))
        psdx[i,:] = psd1[0:d.shape[1]/2]
    psdx = sum(psdx,0)*(xs)/(5*psdx.shape[1]**2)
    vx = np.arange( (1/(xs*d.shape[1])), (1/xs), (2/(xs*d.shape[1])) ) 
    
    psdy=np.zeros([d.shape[1],d.shape[0]/2])
    for i in np.arange(1.,d.shape[1]):
        pp = d[:,i]
        psd1 = (abs(sc.fft(pp)*np.conjugate(sc.fft(pp))))
        psdy[i,:] = psd1[0:d.shape[0]/2]
    psdy = sum(psdy,0)*(ys)/(5*psdy.shape[1]**2)
    vy = np.arange( (1/(ys*d.shape[0])), (1/ys), (2/(ys*d.shape[0])) )
    
    ax.loglog(vx,psdx)
    leg.append(filename+'_x')
    #ax.loglog(vy,psdy)
    #leg.append(filename+'_y')
    #ax.legend(filename)

    
list = glob.glob('*.dat')

for filename in list:    
    xrs = np.loadtxt(filename)
    xrsx=xrs[:,0]
    xrsy=xrs[:,1]
    ax.loglog(xrsx,xrsy,'o-')
    leg.append(filename)

ax.legend(leg,'upper right')

f = open(test.txt, 'w')

plt.show()
