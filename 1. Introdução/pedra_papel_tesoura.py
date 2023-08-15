#pd: 0, pp:1, ts:2
jog_A = 1
jog_B = 1

if (jog_A == 0 and jog_B == 2) or (jog_A == 2 and jog_B == 1) or (jog_A == 1 and jog_B == 0):
    print("Jogador A ganhou do jogador B")
elif jog_A == jog_B:
    print("Empate.")
else:
    print("Jogador B ganhou do jogador A")