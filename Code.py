'''
в файл новые данные
Moon:
    m_o = 597
    m_s = 7.35
    r_o = 384.4
    v_s = 0.00102
    p = 0.3346
    rs = 6.371
Phobos:
    m_o = 62.4
    m_s = 0.00000107
    r_o = 9.4
    v_s = 0.00214
    p = 0.1876
    rs = 3.389
Callisto:
    m_o = 189820
    m_s = 10.759
    r_o = 1882.7
    v_s = 0.00821
    p = 0.1834
Europa:
    m_o = 189820
    m_s = 4.799
    r_o = 670.9
    v_s = 0.01374
    p = 0.3013
    rs = 69.911
Titan:
    m_o = 56834 
    m_s = 13.452
    r_o = 1221.87
    v_s = 0.00557
    p = 0.1879
    rs = 58.232
Tethys:
    m_o = 56834
    m_s = 0.06174
    r_o = 294.619
    v_s = 0.01135
    p = 0.0984
    rs = 58.232
Oberon:
    m_o = 8681 
    m_s = 0.3014
    r_o = 583.52
    v_s = 0.00315
    p = 0.163
    rs = 25.362
Ariel:
    m_o = 8681
    m_s = 0.1353
    r_o = 191.02
    v_s = 0.00551
    p = 0.159
    rs = 25.362
Triton:
    m_o = 10241.3 
    m_s = 2.14
    r_o = 354.759
    v_s = 0.00439
    p = 0.206
    rs = 24.622
Charon:
    m_o = 1.303
    m_s = 0.1586
    r_o = 19.591
    v_s = 0.00021
    p =  0.171
    rs = 1.187
'''

from math import sqrt, pi
import xlsxwriter
from random import randint

def writeInXLSX(a, ws, res, letter):
    ws.write(letter + str(a), str(res))
    a += 1
    return a
data = []
names = []
with open(r'input.dat', 'r') as file:
    for line in file:
        names.append(line[:line.find(' ')])
        data.append([float(x.strip()) for x in line.split(' ') if x.isdigit() or '.' in x])

letter1, letter2 = 'A', 'B'
counter = 0
workbook = xlsxwriter.Workbook(r'C:\Users\gr4m0\Desktop\demo5.xlsx')
worksheet1 = workbook.add_worksheet('F1F0 and rr_o')
worksheet2 = workbook.add_worksheet('distance between planets')
worksheet3 = workbook.add_worksheet('distance to center')
worksheet4 = workbook.add_worksheet('speed')
worksheet5 = workbook.add_worksheet('planet\'s speed')
worksheet6 = workbook.add_worksheet('F1F0 and rr_o2')
worksheet7 = workbook.add_worksheet('distance between planets2')
worksheet8 = workbook.add_worksheet('distance to center2')
worksheet9 = workbook.add_worksheet('speed2')
worksheet10 = workbook.add_worksheet('planet\'s speed2')
worksheet11 = workbook.add_worksheet('planet\'s distance2')


for elem in range(len(data)):
    m_o, m_s, r_o, v_s, p, rs = data[elem]
    G = 0.00000667
    E_t = (m_s*v_s**2 / 2) - G*m_s*m_o / r_o
    F0 = m_s / m_o
    F1 = F0
    c = 0
    r = r_o
    worksheet1.write(letter1 + '1', names[counter] + ' F1/F0')
    worksheet1.write(letter2 + '1', names[counter] + ' r/r_o')
    worksheet2.write(letter1 + '1', names[counter] + ' F1')
    worksheet2.write(letter2 + '1', names[counter] + ' r')
    worksheet3.write(letter1 + '1', names[counter] + ' F1')
    worksheet3.write(letter2 + '1', names[counter] + ' d')
    worksheet4.write(letter1 + '1', names[counter] + ' F1')
    worksheet4.write(letter2 + '1', names[counter] + ' v_s')
    worksheet5.write(letter1 + '1', names[counter] + ' F1')
    worksheet5.write(letter2 + '1', names[counter] + ' v_o')
    worksheet6.write(letter1 + '1', names[counter] + ' F1/F0')
    worksheet6.write(letter2 + '1', names[counter] + ' r/r_o')
    worksheet7.write(letter1 + '1', names[counter] + ' F1')
    worksheet7.write(letter2 + '1', names[counter] + ' r')
    worksheet8.write(letter1 + '1', names[counter] + ' F1')
    worksheet8.write(letter2 + '1', names[counter] + ' d')
    worksheet9.write(letter1 + '1', names[counter] + ' F1')
    worksheet9.write(letter2 + '1', names[counter] + ' v_s')
    worksheet10.write(letter1 + '1', names[counter] + ' F1')
    worksheet10.write(letter2 + '1', names[counter] + ' v_o')
    worksheet11.write(letter1 + '1', names[counter] + ' F1')
    worksheet11.write(letter2 + '1', names[counter] + ' R')
    a1 = a2 = a3 = b1 = b2 = b3 = a4 = b4 = a5 = b5 = a6 = a7 = a8 = b6 = b7 = b8 = a9 = b9 = a10 = b10 = a11 = b11 = 2

    tmp_m_s = m_s
    step = (m_o-m_s)/10000
    r1 = m_s *r / (m_o+m_s)
    while r1 < rs:
        m_s += step
        d = -0.5*G*m_s*m_o / E_t
        F1 = m_s / m_o
        r=abs(2*G*m_s*m_o/(m_s*v_s**2-2*E_t))
        v_s = sqrt(G*m_o/r)
        c += 1
        r1 = m_s *r / (m_o+m_s)
        if rs > r:
            F2 = m_s/m_o
            print ('F2 exists and is equal to', F2) 
            print(f'F2 = {F2}')
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)
        a3 = writeInXLSX(a3, worksheet3, F1, letter1)
        b3 = writeInXLSX(b3, worksheet3, r, letter2)
        a4 = writeInXLSX(a4, worksheet4, F1, letter1)
        b4 = writeInXLSX(b4, worksheet4, v_s, letter2)
        a6 = writeInXLSX(a6, worksheet6, F1/F0, letter1)
        b6 = writeInXLSX(b6, worksheet6, r/r_o, letter2)
        a7 = writeInXLSX(a7, worksheet7, F1, letter1)
        b7 = writeInXLSX(b7, worksheet7, d, letter2)
        a8 = writeInXLSX(a8, worksheet8, F1, letter1)
        b8 = writeInXLSX(b8, worksheet8, r, letter2)
        a9 = writeInXLSX(a9, worksheet9, F1, letter1)
        b9 = writeInXLSX(b9, worksheet9, v_s, letter2)
        
    print(f'First loop for {names[counter]}, iterations: {c}')
    step = (m_o-tmp_m_s)/50
    while F1 <= 1:
        m_s += step
        d = -0.5*G*m_s*m_o / E_t
        v_s = sqrt(G*(m_o**2) / (d * (m_s + m_o)))
        v_o = sqrt(G*(m_s**2) / (d * (m_s + m_o)))
        r = m_o * d / (m_o + m_s)
        R = m_s * d / (m_o + m_s)
        F1 = m_s / m_o
        c += 1
        if r - R < pow(3*m_s / (4*pi*p), 1/3)+rs:
            F2=m_s/m_o
            print ('F2 exists and is equal to', F2)  
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, d, letter2)
        a3 = writeInXLSX(a3, worksheet3, F1, letter1)
        b3 = writeInXLSX(b3, worksheet3, r, letter2)
        a4 = writeInXLSX(a4, worksheet4, F1, letter1)
        b4 = writeInXLSX(b4, worksheet4, v_s, letter2)
        a5 = writeInXLSX(a5, worksheet5, F1, letter1)
        b5 = writeInXLSX(b5, worksheet5, v_o, letter2)
        a6 = writeInXLSX(a6, worksheet6, F1/F0, letter1)
        b6 = writeInXLSX(b6, worksheet6, r/r_o, letter2)
        a7 = writeInXLSX(a7, worksheet7, F1, letter1)
        b7 = writeInXLSX(b7, worksheet7, d, letter2)
        a8 = writeInXLSX(a8, worksheet8, F1, letter1)
        b8 = writeInXLSX(b8, worksheet8, r, letter2)
        a9 = writeInXLSX(a9, worksheet9, F1, letter1)
        b9 = writeInXLSX(b9, worksheet9, v_s, letter2)
        a10 = writeInXLSX(a10, worksheet10, F1, letter1)
        b10 = writeInXLSX(b10, worksheet10, v_o, letter2)
        a11 = writeInXLSX(a11, worksheet11, F1, letter1)
        b11 = writeInXLSX(b11, worksheet11, R, letter2)
    print(f'Second loop for {names[counter]}, iterations: {c}')
        
    step = (m_o-tmp_m_s)
    while r**3 > (3*m_s / (4*pi*p)) and F1 < 50:
        m_s += step
        d = abs(-0.5 * G*m_s*m_o / E_t)
        c += 1
        r = m_o * d / (m_o + m_s)
        v_o = sqrt(G*(m_s**2) / (d * (m_s + m_o)))
        v_s = sqrt(G*(m_o**2) / (d * (m_s + m_o)))
        F1 = m_s/m_o
        R = m_s * d / (m_o + m_s)
        if R - r < pow(3*m_s / (4*pi*p), 1/3)+rs:
            F2=m_s/m_o
            print ('F2 exists and is equal to', F2)
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, d, letter2)
        a3 = writeInXLSX(a3, worksheet3, F1, letter1)
        b3 = writeInXLSX(b3, worksheet3, r, letter2)
        a4 = writeInXLSX(a4, worksheet4, F1, letter1)
        b4 = writeInXLSX(b4, worksheet4, v_s, letter2)
        a5 = writeInXLSX(a5, worksheet5, F1, letter1)
        b5 = writeInXLSX(b5, worksheet5, v_o, letter2)
        a6 = writeInXLSX(a6, worksheet6, F1/F0, letter1)
        b6 = writeInXLSX(b6, worksheet6, r/r_o, letter2)
        a7 = writeInXLSX(a7, worksheet7, F1, letter1)
        b7 = writeInXLSX(b7, worksheet7, d, letter2)
        a8 = writeInXLSX(a8, worksheet8, F1, letter1)
        b8 = writeInXLSX(b8, worksheet8, r, letter2)
        a9 = writeInXLSX(a9, worksheet9, F1, letter1)
        b9 = writeInXLSX(b9, worksheet9, v_s, letter2)
        a10 = writeInXLSX(a10, worksheet10, F1, letter1)
        b10 = writeInXLSX(b10, worksheet10, v_o, letter2)
        a11 = writeInXLSX(a11, worksheet11, F1, letter1)
        b11 = writeInXLSX(b11, worksheet11, R, letter2)
    print(f'Third loop for {names[counter]}, iterations: {c}')
    if names[counter] == 'Mars_and_Phobos':
        l = 10**20
    elif names[counter] == 'Saturn_and_Tethys':
        l = 10**12
    elif elem != 0:
        l = 1000000000
    else:
        l = 10
    step = m_s*l
    while r**3 > (3*m_s / (4*pi*p)) and F1 >= 50:
        m_s += step
        d = abs(-0.5 * G*m_s*m_o / E_t)
        c += 1
        r = m_o * d / (m_o + m_s)
        v_o = sqrt(G*(m_s**2) / (d * (m_s + m_o)))
        v_s = sqrt(G*(m_o**2) / (d * (m_s + m_o)))
        F1 = m_s/m_o
        R = m_s * d / (m_o + m_s)
        if R - r < pow(3*m_s / (4*pi*p), 1/3)+rs:
            F2=m_s/m_o
            print ('F2 exists and is equal to', F2)
        a6 = writeInXLSX(a6, worksheet6, F1/F0, letter1)
        b6 = writeInXLSX(b6, worksheet6, r/r_o, letter2)
        a7 = writeInXLSX(a7, worksheet7, F1, letter1)
        b7 = writeInXLSX(b7, worksheet7, d, letter2)
        a8 = writeInXLSX(a8, worksheet8, F1, letter1)
        b8 = writeInXLSX(b8, worksheet8, r, letter2)
        a9 = writeInXLSX(a9, worksheet9, F1, letter1)
        b9 = writeInXLSX(b9, worksheet9, v_s, letter2)
        a10 = writeInXLSX(a10, worksheet10, F1, letter1)
        b10 = writeInXLSX(b10, worksheet10, v_o, letter2)
        a11 = writeInXLSX(a11, worksheet11, F1, letter1)
        b11 = writeInXLSX(b11, worksheet11, R, letter2)
    print(f'ThirdB loop for {names[counter]}, iterations: {c}')
    a = F1 * 200*l
    r=abs(G*m_s*m_o/(2*E_t))
    r=abs(G*m_s*m_o/(2*E_t))
    step = m_s*l*4
    while r**3 > (3*m_s / (4*pi*p)) and F1 < a:
        m_s+=step
        v_s=0
        r=abs(2*G*m_s*m_o/(m_o*v_o**2-2*E_t))
        r1 = m_o *r / (m_o+m_s)
        v_o=sqrt(G*m_s/r)
        c+=1
        F1=m_s/m_o
        if r < pow(3*m_s / (4*pi*p),1/3):
            F2=m_s/m_o
            print ('F2 exists and is equal to', F2)
        a6 = writeInXLSX(a6, worksheet6, F1/F0, letter1)
        b6 = writeInXLSX(b6, worksheet6, r/r_o, letter2)
        a7 = writeInXLSX(a7, worksheet7, F1, letter1)
        b7 = writeInXLSX(b7, worksheet7, r, letter2)
        a8 = writeInXLSX(a8, worksheet8, F1, letter1)
        b8 = writeInXLSX(b8, worksheet8, r1, letter2)
        a10 = writeInXLSX(a10, worksheet10, F1, letter1)
        b10 = writeInXLSX(b10, worksheet10, v_o, letter2)
        a11 = writeInXLSX(a11, worksheet11, F1, letter1)
        b11 = writeInXLSX(b11, worksheet11, r, letter2)
    print(f'Fourth loop for {names[counter]}, iterations: {c}')
    letter1 = chr(ord(letter1) + 2)
    letter2 = chr(ord(letter2) + 2)
    counter += 1
workbook.close()
