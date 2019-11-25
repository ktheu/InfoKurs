from liste_mit_list import Liste

li = Liste()
assert li.empty()
assert li.endpos()
li.insert('A')
assert not li.empty()
assert not li.endpos()
assert li.elem() == 'A'
li.advance()
assert li.endpos()
li.insert('B')
assert not li.endpos()
li.advance()
li.insert('C')
li.reset()
assert li.elem() == 'A'
li.advance()
li.delete()
assert li.elem() == 'C'
li.delete()
assert li.endpos()
li.reset()
li.delete()
assert li.empty()

