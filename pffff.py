from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def newPage():
    global fontPdf, sizePdf, ydata, xdatalft, xdatargt, xcablft, xcabrgt, ygrid, xgridlft, xgridrgt
    fontPdf = "Helvetica"
    sizePdf = 10
    ydata = 820 #pos y de datos globales
    xdatalft = [20, 150, 220] #pos x de datos globales izq
    xdatargt = [310, 440, 510] #pos x de datos globalez der
    xcablft = [30, 55, 225] #pos x cabecera de tabla izq
    xcabrgt = [320, 345, 515] #pos x cabecera de tabla der
    ygrid = [] #eje y de primera linea de los grid
    xgridlft = [20, 50, 200, 280] #eje x de lineas verticales de grid izq
    xgridrgt = [310, 340, 490, 570] #eje x de lineas verticales de grid der

rem = 17
cab = 16
i = 0
k = 0
c = canvas.Canvas("pdf/algo.pdf", pagesizePdf=A4)
h, w = A4
fontPdf = "Helvetica"
sizePdf = 10
c.setfontPdf(fontPdf, sizePdf)
#linea vertical
c.saveState()
c.setDash(1, 2)
c.line(295, 825, 295, 5)
c.restoreState()
#fin linea vertical
ydata = 820 #pos y de datos globales
xdatalft = [20, 150, 220] #pos x de datos globales izq
xdatargt = [310, 440, 510] #pos x de datos globalez der
xcablft = [30, 55, 225] #pos x cabecera de tabla izq
xcabrgt = [320, 345, 515] #pos x cabecera de tabla der
xgridlft = [20, 50, 200, 280] #eje x de lineas verticales de grid izq
xgridrgt = [310, 340, 490, 570] #eje x de lineas verticales de grid der
largo = 0
while(i<rem):
    start = ydata
    ygrid = []
    if(start - largo < 0):
        c.showPage()
        newPage()
        start = ydata
        c.setfontPdf(fontPdf, sizePdf)
        #linea vertical
        c.saveState()
        c.setDash(1, 2)
        c.line(295, 825, 295, 5)
        c.restoreState()
        #fin linea vertical
    if(i%2==0):
        xdata = xdatalft
        xcab = xcablft
        xgrid = xgridlft
    else:
        xdata = xdatargt
        xcab = xcabrgt
        xgrid = xgridrgt
    j = 0
    c.drawString(xdata[0], ydata, "Nro. de Remate: ")
    c.drawString(xdata[1], ydata, "Carrera: ")
    c.drawString(xdata[2], ydata, "dd/mm/aaaa")
    ydata -= 22
    c.drawString(xcab[0], ydata + 3, "N°")
    c.drawString(xcab[1], ydata + 3, "Nombre")
    c.drawString(xcab[2], ydata + 3, "Monto")
    ygrid.append(ydata + 15)
    while(j<cab):
        j += 1
        ygrid.append(ydata)
        ydata -= 15
        if(j<10):
            c.drawString(xcab[0]+3, ydata + 3, str(j))
        else:
            c.drawString(xcab[0], ydata + 3, str(j))
        c.drawString(xcab[1], ydata + 3, "nombre")
        c.drawString(xcab[2] - 5, ydata + 3, "$99999")
    ygrid.append(ydata)
    c.grid(xgrid, ygrid)
    ygrid = []
    ydata -= 15
    c.drawString(20, ydata, "Totales")
    ydata -= 10
    if(i==0):
        largo = start - ydata
    if(i%2==0):
        #linea horizonal
        c.saveState()
        c.setDash(1, 2)
        c.line(15, ydata, 575, ydata)
        c.restoreState()
        #fin linea horizonal
        ydata = start
    else:
        ydata -= 15
    i += 1
c.save()


