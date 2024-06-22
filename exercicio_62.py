alturas = [165, 170, 180, 175, 160]

total_altura = 0
for altura in alturas:
    total_altura += altura

media_altura = total_altura / len(alturas)
print("A altura média é: " + str(media_altura) + " cm")