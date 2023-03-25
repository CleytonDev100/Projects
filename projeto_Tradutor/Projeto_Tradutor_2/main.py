from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
import pyautogui

print(pyautogui.position())

lista = []
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
       "v", "w", "x", "y", "z", "á", "à", "â", "ã", "é", "ê", "í", "ó", "ô", "õ", "ú", "!", "?", ".", ",", ";"]
dados1 = []
reader = PdfReader("Documento 10 (41) (3).pdf")
teste = ""
cont = 0

#for pagi in range(0, len(reader.pages)):
texto = reader.pages[0].extract_text() # colocar tudo na lista. tentativa = 3. Concluido. def ???
for c in texto:
    if c.lower() in abc or c.isnumeric():
        teste += c
    if c == " ":
        if teste == "":
            pass
        else:
            cont += 1
            dados1.append(teste)
            teste = ""
            if cont == 12:
                lista.append(dados1.copy())
                dados1.clear()
                cont = 0

print(texto)
print(lista)


# Tentativa 1 == Escrever uma pagina. Falha = Melhor escrever uma linha inteira!
report = canvas.Canvas("Tides_Teste_01.pdf")
for r in range(0, len(lista)):
    for i, c in enumerate(lista[r]):
        if c == "CAPÍTULO":
            report.drawCentredString(350, 750, f"{c} {lista[r][i+1]}")
report.save()

#for c in lista:
#    if c.upper() == "CAPÍTULO":
#        report.setFontSize(32)
#        report.drawCentredString(295, 780, f"{lista[0]} {lista[1]}", charSpace=1)

#report.setFontSize(30)
#report.setFontSize(12)
#report.drawCentredString(200, 750, "Somos britânicos, caramba, e orgulhosos da nossa ortografia!")

#report.save()
