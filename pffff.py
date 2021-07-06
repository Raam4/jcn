from reportlab.pdfgen import canvas


c = canvas.Canvas("pdfs/carreras/rendimiento_carrera_1.pdf")
c.setFont("Courier-Bold", 10)
y = 820
c.drawString(20, y, "Carrera 15")
c.drawString(400, y, "Fecha: DD/MM/AAAA")
y -= 20
c.drawString(20, y, "Remate")
c.drawString(150, y, "Recaudado")
c.drawString(300, y, "Pagar")
c.drawString(450, y, "Rendir")
y -= 20

c.save()


