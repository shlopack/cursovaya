# -*- coding: utf-8 -*-

import csv
import os
import sys
import math

def write_formula(name, text):
	open('formulas/{0}.tex'.format(name),'wb').write(text.encode('utf-8'))


with open('data/data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        P_n = float(row[0])
        R_n = float(row[1])
        E_g = float(row[2])
        R_g = float(row[3])
        K_g = float(row[4])/100
        f_l = float(row[5])
        f_h = float(row[6])
        M = float(row[7])
        b = float(row[8])
        T_max = float(row[9])
        group = row[10]


thermo = 1

if (group == '0' or group == '1'):
	group_pic = 2
else:
	group_pic = 1
#calc formulas
K_e = math.sqrt(P_n*R_n)/E_g
F = 0.15/K_g
m = math.pow(10, (b/20))
K_e_tr = K_e*F*m*2
n = math.log(K_e_tr)/math.log(35)
n0 = round(n, 0)
R_vh = 7*R_g


names = [
	'1_1',
	'1_2',
	'1_3',
	'thermo',
	'all_scheme'
]
for name in names:
	command = open('template/{0}.py'.format(name), 'rb').read()
	command = command.decode('utf8')
	exec(command)
	write_formula(name, template)


#2_2

U_nm = math.sqrt(2*P_n*R_n)
I_nm = U_nm/R_n
I_km = I_nm

E_0r = 2*(U_nm+2)
E_00 = 1.1*E_0r
E_0 = round(E_00, 0)

P_k_45 = (E_0*E_0)/(4*math.pi*math.pi*R_n)
h_21 = P_n/0.02

P_k_d = 1.1*P_k_45
I_k_d = 1.1*I_nm
U_ke_d = E_0*1.1
fh_21 = 2*f_h/1000


Rt_kc_1 = (135-T_max)/P_k_45 - 15.6
Rt_kc_2 = (150-T_max)/P_k_45 - 15.6

S_1 = 1400/Rt_kc_1
S_2 = 1400/Rt_kc_2

I_0 = I_nm/math.pi
P_0 = I_0*E_0
eta = P_n/P_0

h_11 = ((1+h_21)*25)/I_0/1000
R_vh = h_11 + (1+h_21)*R_n

R9 = 0.1*R_n
R10 = R9

C_pn = 1/(2*math.pi*f_l*R_n*math.sqrt(1.42*1.42-1))*1000

#2_3

I_o_kz = (2.5*I_nm)/h_21
R7 = 40*R_n
R6 = round(((E_0 - 0.6 - 0.023*R7)/0.02), 2)
R6d = 10*R6
C3 = (5)/(2*math.pi*f_l*(R7+R_n))*1000000
P_k_3_d = 1.3*(E_0*0.02/2)
I_k3m = 0.013 + I_nm/h_21
I_k3d = 1.3*I_k3m
U_ke_3d = 1.3*E_0
f3_h_21 = 2.5*f_h/1000

#formula 3_17
K = (h_21*R_n)/0.625

h_21_3 = 80

#2_4
I_0k1 = 7*0.024 / h_21_3
I_k_dop = 1.1 * I_0k1
fh_21_ = 8*f_h / 1000

h_21_1 = 50
R2 = 0.7 / (I_0k1 - (I_0k1/h_21_3))
R3 = (E_0 - 0.7)/(2*(I_0k1 + I_0k1/h_21_1)) / 1000

F = 25
K_ok = 1
R_vh_3 = 51
R_kn1 = R2 * R_vh_3 / (R2 + R_vh_3)
K_pok = 631

R5 = 5000
R1 = 5000

R_eg = (R1 * R_g)/(R1 + R_g)
R = 2 * h_11 + R_eg
R4 = ((F-1) * R * R5) / (h_21_1 * R_kn1 * K_pok - (F-1) * (R + R5))
R_ekv = (R4 * R)/(R4+R)

beta = (R_ekv/(R5 + R_ekv)) * (600/R)
K_vk = R_kn1 * I_0k1 / 0.025
K_p = beta * K_vk * K_pok * K_ok

h_11_1 = (1 + h_21_1)*0.025/I_0k1

R_vhvk = (R1 * (2*h_11_1 + R4) * F) / (R1 + (2*h_11_1 + R4) * F)


C2 = (R2 + R_vh_3) / (2*math.pi*f_h*K_pok * R2 * R_vh_3 * R3 * 10) * math.pow(10, 12)
C1 = 1/(2*math.pi * f_l * R4 * math.sqrt(M * M - 1)) * math.pow(10, 6)

K_um = 1 / beta
K_um_1 = K_vk * K_pok * K_ok / (1 + K_p)
U_vhvk = U_nm / K_um

print(C2,K_pok, R_vh_3, R3)
names = ['2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8',
'2_9', '2_10', '2_11', '2_14', '2_15', '2_16', '2_17', '2_18',
'2_19', '2_20', '2_21', '2_22', '3_1', '3_2', '3_3', '3_4', '3_5',
'3_6', '3_7', '3_8', '3_9', '3_10', '3_17', '4_1', '4_1dop',
'4_2', '4_3', '4_4', '4_5', '4_6', '4_7', '4_9', '4_10', '4_13',
'4_14', '4_15', '4_16', '4_18', '4_19', '4_20', '4_21', '4_22', '4_23']
for name in names:
	command = open('template/{0}.py'.format(name), 'rb').read()
	command = command.decode('utf8')
	exec(command)
	write_formula(name, template)

export = [
	['f_h_21', fh_21, '%.2f'],
	['u_k', U_ke_d, '%.0f'],
	['i_k', I_k_d, '%.2f'],
	['h_21', h_21, '%.0f'],
	['p_k', P_k_45, '%.2f'],
	['f_h_21', fh_21, '%.2f'],
	['i_km', I_km, '%.2f'],
	['r_vh', R_vh, '%.2f'],
	['s1', S_1, '%.0f'],
	['s2', S_2, '%.0f']
	]

for var in export:
	open('formulas/{0}.tex'.format(var[0]),'wb').write((var[2]%(var[1])).encode('utf-8'))


	#3_1
#formula 5_2
f0 = math.sqrt(f_l*f_h)
f0_ = f_h/(2*m)
_f0 = 2*m*f_l

R2 = 0.5 * R_vhvk
R5 = R2
R1 = R2 / m
R3 = R1 / m
R4 = 0.1 * R2
C1 = 1 / (2 * math.pi * f_l * m * R2) * math.pow(10, 9)
C2 = m * C1
C3 = (m*m) / (4 * math.pi * f_h * R2) * math.pow(10, 9)
C4 = m * C3
R_vht = R1 + R3
R_viht = R4 + (R1*R3)/(R1+R3)
R_vih_pr = R_viht * 0.2
R__ = (R2*m)/(m*m - 1)
R_ = R2 - R__

K_sr = R3 / (R1+R3)

U_vh_t = U_vhvk / K_sr


#3_2
U_n = U_vhvk
R_n = R_vhvk


U_nm = U_n * math.sqrt(2)
I_nm = U_nm / R_n

I_ok = 10*I_nm
U_ke = U_n + 2
E_0p = 3*U_ke
E_0 = 1.2 * E_0p
R_e = 0.3 * E_0p / I_ok
R3 = (E_0p - U_ke - 3.6) / I_ok

I_km = U_n / (R3)

R_en = R_n * R_e / (R_n + R_e)

P_k = U_ke * I_ok
P_kd = 1.3*P_k

U_ke_ = E_0

I_kd = 1.3*(I_ok + I_km)
fh_21 = 30*f_h
h21 = math.sqrt(40*200)
I_d = 10*I_km/h21

R1 = (E_0 - U_ke - 0.7) / (I_ok / h21 + I_d)
R2 = (0.7 + U_ke)/I_d

r_e = 25/I_0
K = R_en / (R_en + r_e)

U_vh = U_n/K
R_vht = 89 + (1+h21)*R_en
R_vh = 1/(1/R_vht + 1/R1 + 1/R2)

export = [
['3_p_k_1', P_kd*1000, '%.2f'],
['3_p_k_2', P_k*1000, '%.2f'],
['3_i_k_1', I_kd*1000, '%.2f'],
['3_i_k_2', (I_ok + I_km)*1000, '%.2f'],
['3_u_k', U_ke_, '%.2f'],
['3_f_h', fh_21/1000, '%.2f'],
]

for var in export:
	open('formulas/{0}.tex'.format(var[0]),'wb').write((var[2]%(var[1])).encode('utf-8'))

names = ['5_2', '5_4', '5_5', '5_6', '5_7', '5_8', '5_9', '5_10',
'5_11', '5_12', '5_13', '5_14', '5_15', '5_16', '5_17', '5_18', '5_19',
'6_1', '6_2', '6_3', '6_4', '6_5', '6_6', '6_7', '6_8', '6_9']
for name in names:
	command = open('template/{0}.py'.format(name), 'rb').read()
	command = command.decode('utf8')
	exec(command)
	write_formula(name, template)


print('all right')      