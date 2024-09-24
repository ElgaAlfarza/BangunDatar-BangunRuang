import streamlit as st
import math
from streamlit_option_menu import option_menu

# Navigasi sidebar
with st.sidebar:
    selected = option_menu('Hitung Luas Bangun by: BIGBOZ',
                           ['Hitung Luas Persegi Panjang',
                            'Hitung Luas Segitiga',
                            'Hitung Luas Lingkaran',
                            'Hitung Luas Balok',
                            'Hitung Luas Kubus'],
                           default_index=0)  # Perbaiki 'defaul_index' menjadi 'default_index'

# Halaman hitung persegi panjang
if selected == 'Hitung Luas Persegi Panjang':
    st.title('Hitung Luas Persegi Panjang')

    panjang = st.slider("Masukan Nilai Panjang", 0)
    lebar = st.slider("Masukan Nilai Lebar", 0)
    hitung = st.button("Hitung Luas")
    k = st.button("hitung Keliling")

    if hitung:
        luas = panjang * lebar
        st.write("Luas Persegi Panjang Adalah = ", luas)
        st.success(f"Luas Persegi Panjang Adalah = {luas}")
        
    if k:
        keliling = 2*(panjang+lebar)
        st.write("Keliling Persegi Panjang Adalah =", keliling)
        st.success(f"Keliling Persegi Panjang Adalah = {keliling}")
        
# Halaman hitung segitiga
if selected == 'Hitung Luas Segitiga':
    st.title('Hitung Luas Segitiga')
    
    alas = st.slider ("Masukan Nilai Alas", 0, 100)
    tinggi = st.slider ("Masukan Nilai tinggi", 0, 100)
    sisiA= st.slider ("Masukan Nilai Sisi A :",0, 100)
    sisiB= st.slider ("Masukan Nilai Sisi B :",0, 100)
    sisiC= st.slider ("Masukan Nilai Sisi C :",0, 100)
    hitung = st.button("Hitung Luas")
    k =st.button("Hitung Keliling")
    
    if hitung:
        luas = 0.5 * alas*tinggi
        st.write("Luas Persegitiga Adalah =", luas)
        st.success(f"Luas Persegitiga Adalah = {luas}")
        
    if k:
        keliling = sisiA + sisiB + sisiC
        st.write("Keliling Persegitiga Adalah =", keliling)
        st.success(f"Keliling Persegitiga Adalah = {keliling}")
        
# Halaman hitung lingkaran
if selected == 'Hitung Luas Lingkaran':
    st.title('Hitung Luas Lingkaran')
    
    jariJari = st.slider("Masukkan Jari-Jari Lingkaran:", 0, 100)
    diameter = st.slider("Masukkan Diameter Lingkaran:", 0, 100)
    
    d = st.button("Hitung Diameter")
    j = st.button("Hitung Jari-Jari")
    l = st.button("Hitung Luas")
    k = st.button("Hitung Keliling")
    
    if d:
        diameter = 2 * jariJari
        st.success(f"Diameter Lingkaran Adalah = {diameter:.2f} cm")
        
    if j:
        jarijari = diameter / 2
        st.success(f"Jari-Jari Lingkaran Adalah = {jarijari:.2f} cm")
        
    if l:
        luas = 3.142857142857143 * jariJari ** 2
        st.success(f"Luas Lingkaran Adalah = {luas:.2f} cm²")
        
    if k:
        if jariJari > 0:
            kelilingJarijari = 2 * 3.142857142857143 * jariJari
            st.success(f"Keliling Lingkaran Berdasarkan Jari-Jari adalah = {kelilingJarijari:.2f} cm")
        
        if diameter > 0:
            kelilingDiameter = 3.142857142857143 * diameter
            st.success(f"Keliling Lingkaran Berdasarkan Diameter adalah = {kelilingDiameter:.2f} cm")
            
if selected == ('Hitung Luas Balok'):
    st.title('Hitung Luas Balok')
    
    panjang = st.slider('Masukan Panjang Balok',0,100)
    lebar = st.slider('Masukan lebar Balok',0,100)
    tinggi = st.slider('Masukan tinggi Balok',0,100)
    
    luas =st.button('Hitung Luas')
    volume =st.button('Hitung Volume')
    diagonal =st.button('Hitung Diagonal')
    
    if luas > 0:
        l = ((panjang * lebar)+(panjang * tinggi) + (lebar * tinggi))*2
        st.success(f"Luas Balok Adalah = {l}")    
    if volume > 0:
        v = panjang*lebar*tinggi
        st.success(f"Volume Balok Adalah = {v}")
    if diagonal > 0:
        d = math.sqrt(panjang**2 + lebar**2 + tinggi**2)
        st.success(f"Diagonal Balok Adalah = {d}")
        
if selected == ('Hitung Luas Kubus'):
    st.title('Hitung Luas Kubus')
    sisi = st.slider('Masukan Panjang Sisi Kubus',0,100)
    
    luas = st.button('Hitung Luas')
    volume = st.button('Hitung Volume')
    diagonal =st.button('Hitung Diagonal')
    
    if luas >0:
        l = 6 * (sisi**2)
        st.success(f"Luas Kubus Adalah ={l} cm")
    if volume >0:
        v = sisi**3
        st.success(f"Volume Kubus Adalah = {v} cm")
    if diagonal >0:
        d = sisi * 1.732
        st.success(f"Volume Kubus Adalah = {d} cm")
    
    