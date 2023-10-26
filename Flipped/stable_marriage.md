### Stable Marriage Problem

[Problemstellung](https://youtu.be/LMQ4d7biEuQ) - [Beispiel](https://youtu.be/pg_WADq6P90)

Finde nach dem Algorithmus aus dem Unterricht ein stabiles Matching für folgende Situationen:

**A1**

    Präferenzen:
    
    0: e c b a d
    1: e c d b a
    2: b c e a d
    3: c d b e a
    4: e b d a c
    
    a: 2 4 1 3 0
    b: 3 1 0 2 4
    c: 3 0 2 4 1
    d: 2 3 1 0 4
    e: 3 1 2 0 4

----

**A2**

    Präferenzen:
    
    0: a d g e h f b c
    1: e f b a d g h c
    2: f a d b c e h g
    3: e d b c h a f g
    4: h e d a g f c b
    5: e h c b f d g a
    6: h a f e c d g b
    7: g b a f d h e c
    
    a: 2 3 4 7 1 0 5 6
    b: 2 6 1 7 3 5 4 0
    c: 4 1 7 5 6 0 3 2
    d: 4 1 5 6 7 3 2 0
    e: 6 1 0 4 5 7 2 3
    f: 1 2 3 5 7 4 6 0
    g: 4 7 3 6 5 0 2 1
    h: 7 3 1 6 2 4 5 0

----

**Lösungen**

    A1: 0-b 1-e 2-a 3-c 4-d
    A2: 0-a 1-e 2-f 3-b 4-d 5-c 6-h 7-g 