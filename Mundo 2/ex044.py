preco = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
op = int(input('Qual é a opção? '))

if op == 1:
    total = preco - (preco * 0.10)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
elif op == 2:
    total = preco - (preco * 0.05)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
elif op == 3:
    total = preco
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(preco, total))
else:
   par = int(input('Quantas prcelas? '))
   total = preco + (preco * 0.20)
   v_par = total/par
   print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(par, v_par))
   print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
   
