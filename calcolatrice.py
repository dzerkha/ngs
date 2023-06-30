#GiuseppeGiordano
#Funzioni
def moltiplica(a, b):
    return int(a) * int(b)

def dividi(a, b):
    return int(a) / int(b)

def somma(a, b):
    return int(a) + int(b)

def sottrai(a, b):
    return int(a) - int(b)

def potenza(a, b):
    return int(a) ** int(b)

while True:  #serve principalmente per effettuare più operazioni se richiesto dall'utente (riga 46-49)                                                                             
    try:        #richiede la scelta se viene triggherato un ValueError
        scelta = int(input("""   
_________       .__               .__          __         .__              
\_   ___ \_____ |  |   ____  ____ |  | _____ _/  |________|__| ____  ____  
/    \  \/\__  \ |  | _/ ___\/  _ \|  | \__  \\   __\_  __ \  |/ ___\/ __ \ 
\     \____/ __ \|  |_\  \__(  <_> )  |__/ __ \|  |  |  | \/  \  \__\  ___/ 
\______  (____  /____/\___  >____/|____(____  /__|  |__|  |__|\___  >___  >
        \/     \/          \/                \/                    \/    \/ 
Ciao, scegli l'operazione matematica che desideri!
(1 - somma, 2 - sottrazione, 3 - divisione, 4 - moltiplicazione, 5 - potenza): """))
        
        if scelta in [1, 2, 3, 4, 5]:
            num1 = input("Inserisci il primo numero: ")
            num2 = input("Inserisci il secondo numero: ")
           #Calcoli
            if scelta == 1:                              
                print("Risultato:", somma(num1, num2))
            elif scelta == 2:
                print("Risultato:", sottrai(num1, num2))
            elif scelta == 3:
                print("Risultato:", dividi(num1, num2))
            elif scelta == 4:
                print("Risultato:", moltiplica(num1, num2))
            elif scelta == 5:
                print("Risultato:", potenza(num1, num2))
        else:
            print("Scelta non valida.Riprova.")  
            continue     #se il ValueError non viene triggherato (quindi viene inserito un int) ma l'intero non appartiene alle scelte (1,2,3,4,5) il ciclo riparte richiedendo la scelta                                                       

        continua = input("Vuoi eseguire un'altra operazione? (s/n): ")     #richiesta nuova operazione

        if continua != "s":
            break  

    except ValueError:  #avendo usato int() per convertire gli input se l'utente inserisce altri tipi di dato (es. se inserisce caratteri a caso) trigghera un ValueError che fa ripartire il ciclo chiedendo di nuovo la scelta dell'operazione
        print("Input non valido. Riprova.")
        continue
