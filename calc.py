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
]
for name in names:
	command = open('template/{0}.py'.format(name), 'rb').read()
	command = command.decode('utf8')
	exec(command)
	write_formula(name, template)


#2

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

#3

I_o_kz = (2.5*I_nm)/h_21
R7 = 40*R_n
R6 = round(((E_0 - 0.6 - 0.023*R7)/0.02), 2)
R6d = 10*R6
C3 = (5)/(2*math.pi*f_l*(R7+R_n))*1000000
P_k_3_d = 1.3*(E_0*0.02/2)
I_k3m = 0.013 + I_nm/h_21

print(eta)

names = ['2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8', 
'2_9', '2_10', '2_11', '2_14', '2_15', '2_16', '2_17',  '2_19', '2_20', '2_21', '2_22']
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


print('all right')      