uloziste = []
tazaci = ['How', 'When', 'Why','What', "Where"]

def vypisVse(uloziste):
    for i in uloziste:
        print(i)

while True:
    inputUzivatele = input("Write something: ")
    if inputUzivatele == '\exit':
        break

    output = inputUzivatele.capitalize()
    firstWord = output.split()[0]
    
    if firstWord in tazaci:
        output += '?'
    else:
        output += '.'

    uloziste.append(output)

#vypisVse(uloziste)
print(" ".join(uloziste))