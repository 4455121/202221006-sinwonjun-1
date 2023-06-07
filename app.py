pip install streamlit

import numpy as np
import matplotlib.pyplot as plt
import control
main(void) {
num = [100]
den = [1, 5, 6]  # (s+2)(s+3) = s^2 + 5s + 6
G = control.TransferFunction(num, den)

Gc = G * 1

t = np.linspace(0, 10, 1000)

u = np.ones_like(t)

t, y = control.step_response(Gc, T=t, input=u)

plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

omega, mag, phase = control.bode(Gc)

plt.figure()
plt.semilogx(omega, mag)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Magnitude (dB)')
plt.title('Frequency Response')
plt.grid(True)

plt.figure()
plt.semilogx(omega, phase)
plt.xlabel('Frequency (rad/s)')
plt.ylabel('Phase (degrees)')
plt.title('Phase Response')
plt.grid(True)

plt.show()
}
