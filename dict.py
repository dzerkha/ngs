#GiuseppeGiordano
scores = { "Antonio" : {"Chimica" : 8, "Fisica" : 7, "Biologia" : 6 , "Storia" : 9 } ,
           "Anna" : {"Chimica" : 6 , "Fisica" : 9, "Inglese" : 7 , "Storia" : 8 },
           "Paolo" : {"Chimica" : 7 , "Italiano" : 10, "Biologia" : 8 , "Storia" : 6 },
           "Maria" : {"Chimica" : 8 , "Fisica" : 7, "Biologia" : 9, "Matematica" : 7 }}
           
somma_std= 0 
media_std = 0


for studente in scores:                          
    print(f"\n Voti di {studente} \n")
    somma_std= 0 
    media_std = 0 
    for subject in scores[studente]:                      #scorro le materie (subject) per studente (scores[studente]) e printo il voto (scores[studente][subject])
        print(subject , scores[studente][subject])
        somma_std += scores[studente][subject]                 #somma e media 
        media_std = somma_std/4
        
        
    print(f"\nla media di {studente} è " , media_std)

#3 (ho diviso in parti per non confondermi)
materie_uniche = []
for studente in scores: 
    
    [materie_uniche.append(subject) for subject in scores[studente] if subject not in materie_uniche]           #appendo ogni materia (subject) a materie_uniche solo se non sono ancora presenti (per non creare duplicati)

print("\nElenco materie uniche: ", materie_uniche, "\n")

#4

for classe in materie_uniche:
    counter_voti = 0 
    somma_classe = 0                                                                 
    for studente in scores :
         if classe in scores[studente]:
             counter_voti +=1
             somma_classe += scores[studente].get(classe)                                  #per ogni studente uso .get() per prendere il voto per ogni materia (classe) e poi sommo ad una variabile somma (che si azzera per ogni materia)
    print(f"la media dei voti di {classe} è" , somma_classe/counter_voti)                  #per fare la media uso un counter che mi dice quanti voti ho per ogni materie e poi divido 
#GiuseppeGiordano 
    
    