kilos = float ( input ( f"Digite a quantidae de quilos do saco; ") )
gramas = kilos * 1000
gato1 = float ( input ( f"Digite em gramas quanto o gato 1 consome por dia: " ) )
gato2 = float ( input ( f"Digite em gramas quanto o gato 2 consome por dia: " ) )
tot5d = gramas - (gato1 * 5 + gato2 * 5)
print( f"O restante após 5 dias é : { tot5d } gramas. " )