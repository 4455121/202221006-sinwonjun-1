# 202221006-sinwonjun-1

import numpy as np
import matplotlib.pyplot as plt
import control

# 전달함수 정의
num = [100]
den = [1, 5, 6]  # (s+2)(s+3) = s^2 + 5s + 6
G = control.TransferFunction(num, den)

# 폐루프 전달함수 계산
Gc = G * 1

# 시간 범위 설정
t = np.linspace(0, 10, 1000)

# 단위 계단 입력 생성
u = np.ones_like(t)

# 시스템 응답 계산
t, y = control.step_response(Gc, T=t, input=u)

# 응답 곡선 그리기
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid(True)
plt.show()

# 주파수 응답 계산
omega, mag, phase = control.bode(Gc)

# 주파수 응답 그래프 그리기
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
