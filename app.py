import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control

def main():
    st.title('전달함수 분석')

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

    # 그래프를 스트림릿에 표시
    fig1, ax1 = plt.subplots()
    ax1.plot(t, u)
    ax1.set(xlabel='Time', ylabel='Input', title='Step Input')
    ax1.grid(True)
    st.pyplot(fig1)

    # 주파수 응답 계산
    omega, mag, phase = control.bode(Gc)

    # 주파수 응답 그래프 그리기
    fig2, (ax2, ax3) = plt.subplots(2, 1)
    ax2.semilogx(omega, mag)
    ax2.set(xlabel='Frequency (rad/s)', ylabel='Magnitude (dB)', title='Magnitude Response')
    ax2.grid(True)

    ax3.semilogx(omega, phase)
    ax3.set(xlabel='Frequency (rad/s)', ylabel='Phase (degrees)', title='Phase Response')
    ax3.grid(True)
    st.pyplot(fig2)

if __name__ == '__main__':
    main()
