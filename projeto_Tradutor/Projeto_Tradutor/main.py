from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas

lista = []
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
       "v", "w", "x", "y", "z", "á", "à", "â", "ã", "é", "ê", "í", "ó", "ô", "õ", "ú", "!", "?", ".", ",", ";"]
dados1 = []
dados2 = []
reader = PdfReader("Documento 10 (41).pdf")

#for pagi in range(0, len(reader.pages)):
texto = reader.pages[0].extract_text()

for c in texto:
    if c.lower() in abc or c.isnumeric():
        dados1.append(c)
        print(dados1)
    elif c == " ":
        for i in dados1:
            if i.lower() in abc or i.isnumeric():
                dados2.append(dados1.copy())
                dados1.clear()
        for r in range(0, len(dados2)):
            if dados2[0][r].lower() in abc or dados2[0][r].isnumeric():
                lista.append(dados2.copy())
                dados2.clear()
            else:
                dados2.clear()

#lista = ["CAPITULO"] #CERTO
#LISTA = [["C", "A"]] #ERRADO
print(lista)

#report = canvas.Canvas("Tides_Teste_01.pdf")

#report.drawCentredString(300, 800, f"{lista[0][0:]}")


#x = 50
#y = 800
#for c in range(0, len(lista)):
#    for r in range(0, len(lista[c])):
#        if lista[c][r] == "CAPITULO":
#            print("CAPITULO FOI")

        #report.drawString(x, y, f"{lista[c][r]:^50}")
        #x += 10

#print(lista[0][0])

#report.save()


