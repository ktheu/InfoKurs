class Eintrag:
    def __init__(self):
        self.inhalt = None
        self.next = None


class Schlange:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def enq(self, x):
        tmp = Eintrag()
        tmp.inhalt = x
        if self.empty():
            self.head = tmp
            self.tail = tmp
        else:
            self.tail.next = tmp
            self.tail = tmp
    
    def deq(self):
        if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def front(self):
        if self.empty(): raise RuntimeError("Fehler: Schlange ist leer")
        return self.head.inhalt


import unittest
class MyTest(unittest.TestCase):
    def test_Schlange(self):
        q = Schlange()
        self.assertTrue(q.empty())
        q.enq(12)
        self.assertFalse(q.empty())
        self.assertEqual(q.front(),12)
        q.enq(42)
        self.assertEqual(q.front(),12)
        q.deq()
        self.assertEqual(q.front(),42)
        q.deq()
        self.assertTrue(q.empty())


if __name__ == '__main__':
    #unittest.main(argv=[''], exit=False)  
    unittest.main()                # in idle oder thonny
    