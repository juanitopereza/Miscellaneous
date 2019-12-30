import matplotlib.pyplot as plt
import numpy as np
#%%
class Chorrera:
    g = 980.0
    k = 250
    def __init__(self, x0, y0, vx0, vy0, M, R):
        self.x = x0
        self.y = y0
        self.vx = vx0
        self.vy = vy0
        self.m = M
        self.r = R
    def Fuerza(self):
        self.fx = 0.0
        if (abs(self.y) < self.r):
            self.fy = Chorrera.k * abs(self.r - self.y)**3
        else:
            self.fy = -self.m * Chorrera.g
    def Movelo(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx += (self.fx/self.m)*dt
        self.vy += (self.fy/self.m)*dt
#%%
Arana = Chorrera(0.0, 50.0, 0.0, 0.0, 15.0, 2.6)
Arana.Fuerza()
t = 0
dt = 0.001
t_f = 1.5
X_1 = [Arana.x]
Y_1 = [Arana.y]
tiempos = [t]
while t < t_f:
    Arana.Fuerza()
    Arana.Movelo(dt)
    X_1.append(Arana.x)
    Y_1.append(Arana.y)
    t += dt
    tiempos.append(t)
#%%
fig = plt.figure(figsize=(5,5))
plt.plot(tiempos,Y_1)
# plt.xlim(0.3, 0.35)
# plt.ylim(-1, 1)
plt.title("$Experimento\ 1:\ y\ vs.\ t$")
plt.xlabel("tiempo\ [s]")
plt.ylabel("altura\ [cm]")
plt.savefig("figura1.png")
#%%
fig = plt.figure(figsize=(5,5))
plt.plot(X_1,Y_1)
plt.title("$Experimento\ 2:\ y\ vs.\ x$")
plt.xlabel("x\ [cm]")
plt.ylabel("y\ [cm]")
plt.savefig("figura2.png")
#%%
