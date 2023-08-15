morango = 3
maca = 8

if morango>=5:
    morango_preco = morango*2.20
else:
    morango_preco = morango*2.50
    
if maca>=5:
    maca_preco = maca*1.50
else:
    maca_preco = maca*1.80
    
preco_total_s_desc = maca_preco + morango_preco
    
if morango+maca>=10 or preco_total_s_desc>=20:
    preco_total=preco_total_s_desc*0.9
else:
    preco_total= preco_total_s_desc

print("Preço saem desconto:", preco_total_s_desc)
print("Preço total:", preco_total)