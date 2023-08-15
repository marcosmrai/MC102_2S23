comp_e_1 = 45
comp_e_2 = 55
comp_a_1 = 100
comp_a_2 = 100
comp_b_1 = 30
comp_b_2 = 100
comp_c_1 = 50
comp_c_2 = 50

dominado = False

if comp_e_1 >= comp_a_1 and comp_e_2 >= comp_a_2:
    dominado = True
if comp_e_1 >= comp_b_1 and comp_e_2 >= comp_b_2:
    dominado = True
if comp_e_1 >= comp_c_1 and comp_e_2 >= comp_c_2:
    dominado = True
    
if dominado:
    print("Computador não útil")
else:
    print("Computador útil")