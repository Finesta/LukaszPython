def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn *= i
        return iloczyn
 
print(ciag())
print(ciag(10,11,12))
