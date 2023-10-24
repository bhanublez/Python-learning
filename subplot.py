import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t);
t1=np.arange(0,1,0.2)
t2=np.arange(0,1,0.35)

plt.figure(1)

plt.subplot(221)
plt.plot(t1,f(t1),'ro',label='2rows 2cols 1stsubplot')
plt.legend()

plt.subplot(222)
plt.plot(t2,f(t2),'g^',label='2rows 2cols 2ndSubplot')
plt.legend()

plt.subplot(223)
plt.plot(t2,f(t2),'y--',label='2rows 2cols 3rdSubplot')
plt.legend()

plt.subplot(224)
plt.plot(t1,f(t1),'b+',label='2rows 2cols 4thSubplot')
