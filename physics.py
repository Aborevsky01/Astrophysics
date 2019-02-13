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


'''
m_o = float(input())
m_s = float(input())
r_o = float(input())
v_s = float(input())
p = float(input())
'''
f2 = 2
workbook = xlsxwriter.Workbook(r'C:\Users\gr4m0\Desktop\demo4.xlsx')
letter1, letter2 = 'A', 'B'
counter = 0
worksheet1 = workbook.add_worksheet('F1F0 and rr_o')
worksheet2 = workbook.add_worksheet('F1 and r')
worksheet3 = workbook.add_worksheet('F2')
worksheet3.write('B1', 'F2')
for elem in data:
    m_o, m_s, r_o, v_s, p = elem
    G = 6.67*(10**-1)
    E_t = (m_s*v_s*v_s / 2) - G*m_s*m_o / r_o
    F0 = m_s / m_o
    F1 = F0
    step = (m_o - m_s) / 50
    
    worksheet1.write(letter1 + '1', names[counter] + ' F1/F0')
    worksheet1.write(letter2 + '1', names[counter] + ' r/r_o')
    worksheet2.write(letter1 + '1', names[counter] + ' F1')
    worksheet2.write(letter2 + '1', names[counter] + ' r')
    
    a1 = 2
    b1 = 2
    a2 = 2
    b2 = 2
    
    
    while F1 < 2/17:
        m_s += step
        #r = (E_t + G*m_s*m_o) * 2 / (m_s*v_s*v_s)
        r = G * m_s * m_o / (m_s * v_s**2 / 2 - E_t)
        
        F1 = m_s / m_o
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)
    d = -0.5 * G*m_o**2 / E_t    
    v_s1 = sqrt(G*m_s**2 / (d*(m_s + m_o)))
    v_o1 = sqrt(G*m_o**2 / (d*(m_s + m_o)))
    v_o2 = v_s1 * v_o1 / v_s
    E = m_o*v_o2**2 / 2 - E_t
    m_smax = sqrt(3 * E**3 / (p * pi * 4 * (G*m_o)**3))
    #print(m_smax)
    
    F2=m_smax/m_o
    #print(F2)
    
    while 2/17 < F1 < 1 and F1 < F2:
        m_s += step
        d = -0.5 * G*m_s*m_o / E_t
        #r = m_o * d / (m_o + m_s) - m_s*d / (m_o + m_s)
        #r = m_s * d / (m_o + m_s)
        #r = G * m_s * m_o / (m_s * v_s**2 / 2 - E_t)
        r = m_o * d / (m_o + m_s)
        F1 = m_s / m_o
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)
        
    '''
    v_s1 = sqrt(G*m_s**2 / (d*(m_s + m_o)))
    v_o1 = sqrt(G*m_o**2 / (d*(m_s + m_o)))
    v_o2 = v_s1 * v_o1 / v_s
    '''
    while 1 <= F1 < 17/2 and F1 < F2:
        m_s += step
        d = -0.5 * G*m_s*m_o / E_t
        #r = m_s * d / (m_o + m_s) - m_o*d / (m_o + m_s)
        #r = G * m_s * m_o / (m_s * v_s**2 / 2 - E_t)
        r = m_o * d / (m_o + m_s)
        F1 = m_s / m_o
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)


    while 17/2 < F1 <= 1/F0 and F1 < F2:
        m_s += step
        #r = (E_t + G*m_s*m_o) * 2 / (m_o*v_o2*v_o2)
        r = G * m_s * m_o / (m_s * v_s**2 / 2 - E_t)
        F1 = m_s / m_o
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)
    '''
    m_smax=E_t*r/(G*m_o)
    print(m_smax)
    r=pow((3*m_smax/(4*pi*p)), 1/3)
    '''
    
    #m_smax=sqrt(((m_o*v_o2**2/2 - E_t)**3)*(3/(4*pi*p)) / (G*m_o)**3)
    '''
    E = m_o*v_o2**2 / 2 - E_t
    m_smax = sqrt(3 * E**3 / (p * pi * 4 * (G*m_o)**3))
    print(m_smax)
    
    F2=m_smax/m_o
    print(F2)
    '''
    while 1/F0 < F1 <= F2 and F1 < F2:
        
        m_s += step
        r = (E_t + G*m_s*m_o) * 2 / (m_o*v_o2*v_o2)
        F1 = m_s / m_o
        a1 = writeInXLSX(a1, worksheet1, F1/F0, letter1)
        b1 = writeInXLSX(b1, worksheet1, r/r_o, letter2)
        a2 = writeInXLSX(a2, worksheet2, F1, letter1)
        b2 = writeInXLSX(b2, worksheet2, r, letter2)
    print('complete')
    writeInXLSX(f2, worksheet3, names[counter], 'A')
    f2 = writeInXLSX(f2, worksheet3, F2, 'B')
    letter1 = chr(ord(letter1) + 2)
    letter2 = chr(ord(letter2) + 2)
    counter += 1
    

workbook.close()

