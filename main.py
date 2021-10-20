def citireLista():
    l = []
    givenString = input("Dati lista, cu elementele separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(float(x))
    return l

def printMenu():
    print("1.Citire lista:")
    print("2.Afisare listei:")
    print("3.Cerinta 3")
    print("4.Cerinta 4")
    print("5.Cerinta 5")
    print("x.Exit")

def cerinta2(l):
    '''
    Afiseaza doar partea intreaga a numerelor.
    :param l: lista data
    :return: o lista doar cu partea intreaga a numerelor
    '''
    lst = []
    for i in l:
        lst.append(int(i))
    return lst

def testcerinta2():
    assert cerinta2([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert cerinta2([1.3, -5.3, 24, -7.8, 10.2]) == [1, -5, 24, -7, 10]

def cerinta3(l, nr1, nr2):
    '''
    Afiseaza numerele din lista care se afla in intervalul dat.
    :param l: lista data
    :param nr1: primul numar
    :param nr2: al doilea numar
    :return: o lista cu numerele din intervalul dat
    '''
    lst = []
    if nr2 < nr1:
        aux = nr1
        nr1 = nr2
        nr2 = aux
    for i in l:
        if i > nr1 and i < nr2:
            lst.append(i)
    return lst

def testcerinta3():
    assert cerinta3([1.5, -3.3, 8, 9.8, 3.2], -4, 5) == [1.5, -3.3, 3.2]
    assert cerinta3([1.5, -3.3, 3.2, 10.5, 8.7, -5.9, -12.3], 9, -8) == [1.5, -3.3, 3.2, 8.7, -5.9]

def cerinta4(l):
    '''
    Afiseaza numerele a caror parte fractionara este divizibila cu partea intreaga.
    :param l: lista data
    :return: o alta lista care contine numerele care indeplinesc conditia data
    '''
    lst = []
    for i in l:
        s = str(i)
        if s == '-':
            s = s[1:]
        parts = s.split('.')
        parte_intraga = int(parts[0])
        parte_fract = int(parts[1])
        if parte_fract % parte_intraga == 0 and parte_fract != 0:
            lst.append(i)
    return lst

def testcerinta4():
    assert cerinta4([1.5, -3.3, 9.8, 3.2]) == [1.5, -3.3]

def cerinta5(l):
    '''
    Afiseaza numerele in cuvinte care le descriu caracter cu caracter.
    :param l: lista data
    :return: o lista cu numerele sub forma de cuvant
    '''
    lst = []
    for i in l:
        stringList = ''
        s = str(i)
        length = len(s)
        i = 0
        while i < length:
            if s[i] == '-':
                stringList += 'minus'
            elif s[i] == '.':
                stringList += 'virgula'
            elif s[i] == '1':
                stringList += 'unu'
            elif s[i] == '2':
                stringList += 'doi'
            elif s[i] == '3':
                stringList += 'trei'
            elif s[i] == '4':
                stringList += 'patru'
            elif s[i] == '5':
                stringList += 'cinci'
            elif s[i] == '6':
                stringList += 'sase'
            elif s[i] == '7':
                stringList += 'sapte'
            elif s[i] == '8':
                stringList += 'opt'
            elif s[i] == '9':
                stringList += 'noua'
            else:
                stringList += 'zero'
            i += 1
        lst.append(stringList)
    return lst


def testcerinta5():
    assert cerinta5([1.5, -3.3, 9.8, 3.2, 14.52]) == ["unuvirgulacinci", "minustreivirgulatrei",
                                                        "nouavirgulaopt", "treivirguladoi", "unupatruvirgulacincidoi"]

def main():
    testcerinta2()
    testcerinta3()
    testcerinta4()
    testcerinta5()
    l = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(cerinta2(l))
        elif optiune == "3":
            nr1 = int(input("Primul numar:"))
            nr2 = int(input("Al doilea numar:"))
            print(cerinta3(l, nr1, nr2))
        elif optiune == "4":
            print(cerinta4(l))
        elif optiune == "5":
            print(cerinta5(l))
        elif optiune == "x":
            break

main()