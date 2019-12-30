import matplotlib.pyplot as plt
import numpy as np

class Cabezona:
    g = 980.0
    k = 0.0005
    def __init__(self, x0, y0, vx0, vy0, M):
        self.x = x0
        self.y = y0
        self.vx = vx0
        self.vy = vy0
        self.m = M
    def Fuerza(self):
        self.fx = -Cabezona.k * self.m * Cabezona.g * self.vx
        self.fy = -Cabezona.k * self.m * Cabezona.g * self.vy
    def Movelo(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx += (self.fx/self.m)*dt
        self.vy += (self.fy/self.m)*dt

Bola_8 = Cabezona(0.0, 0.0, 10.0, 0.0, 150)
Bola_8.Fuerza()
t = 0
dt = 0.1
t_f = 10
X_1 = [Bola_8.x]
Y_1 = [Bola_8.y]
while t < t_f:
    Bola_8.Fuerza()
    Bola_8.Movelo(dt)
    X_1.append(Bola_8.x)
    Y_1.append(Bola_8.y)
    t += dt
plt.plot(X_1,Y_1)

theta = np.pi/4
Bola_9 = Cabezona(0.0, 0.0, 30.0*np.cos(theta), 30.0*np.sin(theta), 150)
Bola_9.Fuerza()
t = 0
dt = 0.1
t_f = 10
X_1 = [Bola_9.x]
Y_1 = [Bola_9.y]
while t < t_f:
    Bola_9.Fuerza()
    Bola_9.Movelo(dt)
    X_1.append(Bola_9.x)
    Y_1.append(Bola_9.y)
    t += dt
plt.plot(X_1,Y_1)
