import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def main():
    st.title('전달함수 분석')
    # 전달함수 계수
    num = [100]
    den = [1, 5, 6]

    # 폐루프 전달함수 계산
    G = signal.TransferFunction(num, den)

    # unit step 입력에 대한 응답곡선 계산
    t, y = signal.step(G)

    # 주파수 응답 계산
    w, mag, phase = signal.bode(G)

    # 그래프 그리기
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))
    fig.suptitle('System Response')

    # 응답곡선 그래프
    axs[0].plot(t, y)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Output')
    axs[0].set_title('Step Response')

    # 주파수 응답 그래프
    axs[1].semilogx(w, mag)
    axs[1].set_xlabel('Frequency')
    axs[1].set_ylabel('Magnitude')
    axs[1].set_title('Bode Plot (Magnitude)')

    axs[2].semilogx(w, phase)
    axs[2].set_xlabel('Frequency')
    axs[2].set_ylabel('Phase')
    axs[2].set_title('Bode Plot (Phase)')

    # 그래프 출력
    st.pyplot(fig)

if __name__ == "__main__":
    main()
