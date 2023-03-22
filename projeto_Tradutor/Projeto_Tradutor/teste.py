from reportlab.pdfgen import canvas

report = canvas.Canvas("Tides_Teste_01.pdf")

report.drawString(50, 800, "Primeira pagina")
report.showPage()

report.drawString(50, 800, "Segunda pagina")
report.showPage()

report.save()
