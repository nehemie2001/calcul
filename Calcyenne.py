
# coding: utf-8

notema = int(raw_input("entrez votre note en mathématiques: "))
coema = int(raw_input("entrez le coefficient: "))
multma = notema*coema
notephy = int(raw_input("entrez votre note en physique: "))
coephy = int(raw_input("entrez le coefficient: "))
multphy = notephy*coephy
notesvt = int(raw_input("entrez votre note en SVT: "))
coesvt = int(raw_input("entrez le coefficient: "))
multsvt = notesvt*coesvt
result = (multma + multphy + multsvt) / (coema + coephy + coesvt)
print("vous avez {} de moyenne en science".format(result))

