zbozi = ["CPU", "GPU" , "RAM" , "Motherboard" , "Case"]
kosik = []
print(zbozi)
def kupovani(koupě):
   for x in range(len(koupě)):
      print(f"{x+1}: {koupě[x]}")
      print("")


kosik_plus = input("Zadejte zboží, které chcete přidat: ")
zbozi.append(kosik_plus)
kupovani(zbozi)

kosik_minus = (input("Jakou pozici chcete odebrat? "))
zbozi.pop(kosik_minus)
kupovani(zbozi)