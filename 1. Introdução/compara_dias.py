dia_1 = 10
mes_1 = 12
ano_1 = 73
ac_dc_1 = "dc"

dia_2 = 10
mes_2 = 12
ano_2 = 1873
ac_dc_2 = "dc"

if ac_dc_1 == "ac":
    ano_1 = - ano_1

if ac_dc_2 == "ac":
    ano_2 = - ano_2

if ano_1 == ano_2:
    if mes_1 == mes_2:
        if dia_1 > dia_2:
            print(dia_1, mes_1, ano_1)
        else:
            print(dia_2, mes_2, ano_2)
    elif mes_1 > mes_2:
        print(dia_1, mes_1, ano_1)
    else:
        print(dia_2, mes_2, ano_2)
elif ano_1 > ano_2:
    print(dia_1, mes_1, ano_1)
else:
    print(dia_2, mes_2, ano_2)
