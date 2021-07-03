from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("pdf/algo.pdf", pagesize=A4)
h, w = A4
c.setFont("Helvetica", 10)
c.drawString(20, 820, "Nro. de Remate: ")
c.drawString(150, 820, "Carrera: ")
c.drawString(220, 820, "dd/mm/aaaa")

xlist = [20, 50, 200, 280]
ylist = [815, 800, 785]
c.grid(xlist, ylist)
c.drawString(30, 803, "N°")
c.drawString(55, 803, "Nombre")
c.drawString(225, 803, "Monto")


c.drawString(310, 820, "Nro. de Remate: ")
c.drawString(440, 820, "Carrera: ")
c.drawString(510, 820, "dd/mm/aaaa")

xlist = [310, 340, 490, 570]
ylist = [815, 800, 785]
c.grid(xlist, ylist)
c.drawString(320, 803, "N°")
c.drawString(345, 803, "Nombre")
c.drawString(515, 803, "Monto")

c.save()