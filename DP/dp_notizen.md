
Nehmen wir an, wir haben eine Problemstellung, die sich auf eine Liste von Daten bezieht. Dann sollten wir uns fragen, ob es uns helfen würde, wenn wir (via Rekursion) die Antworten für kleinere Problemgrößen wüßten. Wenn wir zu dem Schluß kommen, das würde uns schon helfen, aber ganz könnten wir damit die Sache nicht lösen, weil uns ein Detail fehlt, dann sind wir auf der richtigen Spur. Dann machen wir nämlich über das Detail, was wir nicht wissen, ein brute force und suchen uns die beste Lösung raus.

#### Typen

    Suffixe mit Listen dp(i): Frog1, Frog2, Bowling, LIS (constraints, bruteforce an 2 stellen)
    Suffixe mit Listen dp(i,k): Cooldown, Vacation (constraint, brute force an 2 stellen)
    Suffixe mit zwei Listen/Strings dp(i,j): Edit Distance, LCS 

Suffixe für Listen:


    dp(i) = Lösung des Problems für Liste a[i:]  
    dp(0) = Lösung des Originalproblems

    n = len(a)
    Falls das Problem für die leere Liste eine sinnvolle Lösung hat:
        Rekursionsbremse = dp(n)  
    Sonst:
        Rekursionsbremse = dp(n-1)   

    Für die Rekursionsbremse dp(n) können wir in der Rekursion folgende Indizes ohne Einschränkungen verwenden:
        a[i], dp[i+1]

    Für die Rekursionsbremse dp(n-1) können wir in der Rekursion folgende Indizes ohne Einschränkungen verwenden:
        a[i+1], dp[i+1]

    Wenn wir höhere Indizes benötigen, müssen wir ungültige Fälle in der Rekursion abfangen oder die Rekursionsbremse
    um weitere Fälle erweitern.

    
Je nachdem, welche Fälle wir in der Rekursionsbremse abfangen, können wir in der Rekursion Indizes ohne weitere Einschränkungen verwenden.

    i == n:    höchster Index für a in der Rekursion: i, höchster Index für dp auf der rechten Seite: i+1
    i == n-1:  höchster Index: a[i+1], dp[i+2]
    i == n-2:  höchster Index für a in der Rekursion: i+2

Wenn wir beispielsweise in der Rekursionsbremse den Fall n-1 abfangen und wir wollen in der Rekursions einen Ausdruck a[i+2] verwenden, dann müssen wir explizit sicherstellen dass i+2 ein gültiger Index ist, also i+2 < n.

Häufig ist das subproblem genau dasselbe wie das Originalproblem, aber manchmal müssen wir es mit einem constraint ändern. In der Regel probieren wir dann alle möglichen Werte für den contraint aus.