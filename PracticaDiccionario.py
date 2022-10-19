midiccionario={"Alemania":"Berlín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
midiccionario["Colombia"]="Lisboa"
print(midiccionario)
midiccionario["Colombia"]="Bogotá"
print(midiccionario)
del midiccionario["Reino Unido"]
print(midiccionario)

midiccionario2={"Perú":"Lima",23:"Jordan","Mosqueteros":3}
print(midiccionario2)

mitupla=["España","Francia","Reino Unido","Alemania"]
midiccionario3={mitupla[0]:"Madrid",mitupla[1]:"París",mitupla[2]:"Londres",mitupla[3]:"Berlín"}
print(midiccionario3)

print(midiccionario3["Francia"])

midiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario4)
print(midiccionario4["Equipo"])
print(midiccionario4["anillos"])

print(midiccionario4.keys())
print(midiccionario4.values())
print(len(midiccionario4))