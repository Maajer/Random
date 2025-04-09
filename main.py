import random
produkty = ["sýr,bicykl,kabát"]

for i in range (10):
 nahodny_produkty1 = random.choice(produkty)
 nahodny_produkty2 = random.choice(produkty)
nahodny_produkty3 = random.choice(produkty)
if nahodny_produkty1 == nahodny_produkty2:
    print("Kupte",nahodny_produkty1)
    print("Ne, Kupte",nahodny_produkty2)
    print("Ne, kupte" , nahodny_produkty3)

