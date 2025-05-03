for numero in range(0, 31):
    
    
    if numero % 2 == 0:
        
        if numero == 10:
            print("Esse não vou mostra!")
            continue  
        elif numero == 20:
            print("Esse é secreto!")
            continue  
        elif numero == 30:
            print("esse é o ultimo da lista é também esta oculto")
            continue 
        else:
            
            print(numero)

print("Pronto! Vimos todos os números pares exeto os banidos pelo Professor!")





