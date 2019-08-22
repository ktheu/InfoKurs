def status(eingang, gang, ausgang):
    eingangs = ' '.join([str(x) for x in eingang])
    ausgangs = ' '.join([str(x) for x in ausgang[::-1]])
    gangs = ' '.join([str(x) for x in gang[::-1]])
    print("{:>30} : {:30}\n{:30} : {:30}".format(eingangs,gangs,'',ausgangs))
    
       
reihenfolge = [7, 6, 5, 4, 3, 2, 8, 9, 1]
anzahl = len(reihenfolge)  
siege = {k:0 for k in range(1,anzahl+1)}
niederlagen = {k:0 for k in range(1,anzahl+1)}

ausgang = reihenfolge[::-1] 
eingang = list(range(anzahl,0,-1))
gang = []
 
fertig = False
fehler = False

status(eingang,gang,ausgang) 
while not fertig and not fehler:
    
    if not eingang and not gang and not ausgang:
        fertig = True
    
    # Wenn der Gang leer ist und im Eingang noch eine
    # Maus sitzt, wird sie in den Gang versetzt
    if eingang and not gang:
        gang.append(eingang.pop())
        status(eingang,gang,ausgang)
    
    # Wenn der Eingang leer ist, der Gang aber nicht,    
    # dann muss die oberste Maus im Gang mit der                      
    # ersten Maus im Ausgang übereinstimmen, sonst               
    # kann die Reihenfolge nicht rekonstruiert werden.                
    # Wenn das der Fall ist, wird die Maus vom Gang und               
    # dem Ausgang entfernt.                                           

    if not eingang and gang:
        if not ausgang:
            fehler = True
        else:              # kein Kampf
            m1 = gang.pop()
            m2 = ausgang.pop()
            if m1 != m2:
                fehler = True
        status(eingang,gang,ausgang)
        
    if eingang and gang and ausgang:
        me = eingang[-1]
        mg = gang[-1]
        ma = ausgang[-1]
        
        if mg == ma:
            siege[mg] +=1
            niederlagen[me] +=1
            gang.pop()
            ausgang.pop()
        
        else:
            niederlagen[mg] += 1
            siege[me] += 1
            eingang.pop()
            gang.append(me)
        
        status(eingang,gang,ausgang)
    
if not fehler:
    for k in range(1,anzahl+1):
        print("Maus {} - Siege: {}, Niederlagen: {}".format(k,siege[k], niederlagen[k]))
        
else:
    print("Fehlerhafte Eingabe")
        
        