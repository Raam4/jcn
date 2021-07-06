from reportlab.pdfgen import canvas

remates = 10
c = canvas.Canvas("pdfs/carreras/rendimiento_carrera_1.pdf")
c.setFont("Courier-Bold", 10)
y = 820
c.drawString(20, y, "Carrera 15")
c.drawString(400, y, "Fecha: DD/MM/AAAA")
y -= 20
c.drawString(25, y-5, "Remate")
c.drawString(75, y-5, "Recaudado")
c.drawString(140, y, "Propietario")
c.drawString(215, y, "Organizador")
c.drawString(295, y, "Rematador")
c.drawString(360, y, "Gastos Org.")
c.drawString(440, y, "A Pagar")
y -= 10
c.drawString(165, y, "10%")
c.drawString(240, y, "9%")
c.drawString(315, y, "2%")
c.drawString(380, y, "10%")
c.drawString(450, y, "69%")
y -= 5
i=0
xgrid = [20, 70, 135, 210, 290, 355, 430, 500]
ygrid = []
ygrid.append(y + 25)
while(i<remates):
    ygrid.append(y)
    y -= 15
    c.drawString(25, y + 3.5, str(i+1))
    c.drawString(80, y + 3.5, "$999999")
    c.drawString(150, y + 3.5, "$9999.00")
    c.drawString(225, y + 3.5, "$9999.00")
    c.drawString(300, y + 3.5, "$9999.00")
    c.drawString(370, y + 3.5, "$9999.00")
    c.drawString(440, y + 3.5, "$99999.00")
    i+=1

ygrid.append(y)
c.grid(xgrid, ygrid)

c.save()


