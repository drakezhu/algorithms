for a in A:
    dp |= {a + i for i in dp}
# dp is the set; A is a list; this means that adding different combination of elements in A
