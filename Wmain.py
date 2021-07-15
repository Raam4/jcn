from os import error
from re import sub
import sys
sys.path.append("./")
from PyQt5 import QtCore, QtGui, QtWidgets
import utils
import datetime
from reportlab.pdfgen import canvas
from escpos.conn import SerialConnection
from escpos.impl.epson import GenericESCPOS

class Ui_MainWindow(QtWidgets.QWidget):
    idCarrera = None
    nroCarrera = None
    cantCaballos = None
    idRemate = None
    nroRemate = None
    cajaCarga = None
    strNames = ""
    txt = ""
    sess = utils.bd()
    fec = datetime.date.today()
    try:
        idReunion = sess.execute("SELECT COUNT(*) FROM reunion").scalar() + 1
        sess.execute("INSERT INTO reunion(id, fecha) VALUES (:val, :par)", {'val' : idReunion, 'par' : fec})
        sess.commit()
        sess.close()
    except:
        idReunion = sess.execute("SELECT id FROM reunion WHERE fecha = :var", {'var' : fec}).scalar()
        sess.close()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Remates JCN")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Box Carrera
        self.bcarrera = QtWidgets.QGroupBox(self.centralwidget)
        self.bcarrera.setGeometry(QtCore.QRect(490, 0, 101, 51))
        self.bcarrera.setObjectName("bcarrera")
        self.xy = QtWidgets.QLabel(self.bcarrera)
        self.xy.setGeometry(QtCore.QRect(30, 20, 41, 16))
        fontxy = QtGui.QFont()
        fontxy.setFamily("Verdana")
        fontxy.setPointSize(12)
        fontxy.setBold(True)
        fontxy.setWeight(75)
        self.xy.setFont(fontxy)
        self.xy.setAlignment(QtCore.Qt.AlignCenter)
        self.xy.setObjectName("xy")
        #Box Remate
        self.bremate = QtWidgets.QGroupBox(self.centralwidget)
        self.bremate.setGeometry(QtCore.QRect(240, 0, 251, 51))
        self.bremate.setObjectName("bremate")
        self.lremate = QtWidgets.QLineEdit(self.bremate)
        self.lremate.setGeometry(QtCore.QRect(10, 20, 231, 20))
        self.lremate.setObjectName("lremate")
        #Box Porcentajes
        self.porcentajes = QtWidgets.QGroupBox(self.centralwidget)
        self.porcentajes.setGeometry(QtCore.QRect(240, 50, 91, 111))
        self.porcentajes.setObjectName("porcentajes")
        self.diezP = QtWidgets.QRadioButton(self.porcentajes)
        self.diezP.setGeometry(QtCore.QRect(20, 20, 65, 20))
        fontp = QtGui.QFont()
        fontp.setFamily("Verdana")
        fontp.setPointSize(12)
        fontp.setBold(True)
        fontp.setWeight(75)
        self.diezP.setFont(fontp)
        self.diezP.setChecked(False)
        self.diezP.setAutoRepeat(False)
        self.diezP.setObjectName("diezP")
        self.veinteP = QtWidgets.QRadioButton(self.porcentajes)
        self.veinteP.setGeometry(QtCore.QRect(20, 50, 65, 20))
        self.veinteP.setFont(fontp)
        self.veinteP.setChecked(False)
        self.veinteP.setAutoRepeat(False)
        self.veinteP.setObjectName("veinteP")
        self.treintaP = QtWidgets.QRadioButton(self.porcentajes)
        self.treintaP.setGeometry(QtCore.QRect(20, 80, 65, 20))
        self.treintaP.setFont(fontp)
        self.treintaP.setChecked(False)
        self.treintaP.setAutoRepeat(False)
        self.treintaP.setObjectName("treintaP")
        #Box Subtotales
        self.bsubtotales = QtWidgets.QGroupBox(self.centralwidget)
        self.bsubtotales.setGeometry(QtCore.QRect(340, 50, 251, 111))
        self.bsubtotales.setObjectName("bsubtotales")
        self.subtotales = QtWidgets.QTextBrowser(self.bsubtotales)
        self.subtotales.setGeometry(QtCore.QRect(10, 20, 231, 81))
        self.subtotales.setObjectName("subtotales")
        #Box Historial
        self.bhistorial = QtWidgets.QGroupBox(self.centralwidget)
        self.bhistorial.setGeometry(QtCore.QRect(240, 170, 351, 340))
        self.bhistorial.setObjectName("bhistorial")
        self.whistorial = QtWidgets.QWidget(self.bhistorial)
        self.whistorial.setGeometry(QtCore.QRect(10, 20, 331, 310))
        self.whistorial.setObjectName("whistorial")
        self.txtHistorial = QtWidgets.QTextBrowser(self.whistorial)
        self.txtHistorial.setGeometry(QtCore.QRect(0, 0, 331, 310))
        self.txtHistorial.setObjectName("txtHistorial")
        #Botón Fin Carrera
        self.finCarreraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.finCarreraBtn.setGeometry(QtCore.QRect(240, 520, 350, 50))
        fontend = QtGui.QFont()
        fontend.setBold(True)
        fontend.setWeight(75)
        self.finCarreraBtn.setFont(fontend)
        self.finCarreraBtn.setObjectName("finCarreraBtn")
        self.finCarreraBtn.clicked.connect(self.finCarrera)

        MainWindow.setCentralWidget(self.centralwidget)
        #Barra Superior
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMen = QtWidgets.QMenu(self.menuBar)
        self.menuMen.setObjectName("menuMen")
        self.menuAcciones = QtWidgets.QMenu(self.menuBar)
        self.menuAcciones.setObjectName("menuAcciones")
        self.menuEdicion = QtWidgets.QMenu(self.menuBar)
        self.menuEdicion.setObjectName("menuEdicion")
        MainWindow.setMenuBar(self.menuBar)
        #Action Carrera
        self.actionCarreras = QtWidgets.QAction(MainWindow)
        self.actionCarreras.setObjectName("actionCarreras")
        self.actionCarreras.triggered.connect(self.dialogCarrera)

        self.actionCaballos = QtWidgets.QAction(MainWindow)
        self.actionCaballos.setObjectName("actionCaballos")
        self.actionCaballos.triggered.connect(self.horses)

        self.actionImprimir_remates = QtWidgets.QAction(MainWindow)
        self.actionImprimir_remates.setObjectName("actionImprimir_remates")
        self.actionImprimir_remates.triggered.connect(self.imprimeRemates)
        
        self.actionImprimir_Carrera = QtWidgets.QAction(MainWindow)
        self.actionImprimir_Carrera.setObjectName("actionImprimir_Carrera")
        self.actionImprimir_Carrera.triggered.connect(self.imprimeCarrera)

        self.actionTicket = QtWidgets.QAction(MainWindow)
        self.actionTicket.setObjectName("actionTicket")
        self.actionTicket.triggered.connect(self.buscador)

        self.actionEliminar_Caballo = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Caballo.setObjectName("actionEliminar_Caballo")
        self.actionEliminar_Caballo.triggered.connect(lambda: self.eliminador('cab'))

        self.actionEliminar_Remate = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Remate.setObjectName("actionEliminar_Remate")
        self.actionEliminar_Remate.triggered.connect(lambda: self.eliminador('rem'))

        self.actionEliminar_Carrera = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Carrera.setObjectName("actionEliminar_Carrera")
        self.actionEliminar_Carrera.triggered.connect(lambda: self.eliminador('car'))

        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.triggered.connect(self.close)
        self.menuMen.addAction(self.actionCarreras)
        self.menuMen.addAction(self.actionCaballos)
        self.menuMen.addAction(self.actionSalir)
        self.menuAcciones.addAction(self.actionImprimir_remates)
        self.menuAcciones.addAction(self.actionImprimir_Carrera)
        self.menuAcciones.addAction(self.actionTicket)
        self.menuEdicion.addAction(self.actionEliminar_Caballo)
        self.menuEdicion.addAction(self.actionEliminar_Remate)
        self.menuEdicion.addAction(self.actionEliminar_Carrera)
        self.menuBar.addAction(self.menuMen.menuAction())
        self.menuBar.addAction(self.menuAcciones.menuAction())
        self.menuBar.addAction(self.menuEdicion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Remates JCN", "Remates JCN"))
        self.bcarrera.setTitle(_translate("Remates JCN", "Carrera"))
        self.bremate.setTitle(_translate("Remates JCN", "Remate "))
        self.porcentajes.setTitle(_translate("Remates JCN", "Porcentaje"))
        self.diezP.setText(_translate("Remates JCN", "10%"))
        self.veinteP.setText(_translate("Remates JCN", "20%"))
        self.treintaP.setText(_translate("Remates JCN", "30%"))
        self.bsubtotales.setTitle(_translate("Remates JCN", "Subtotales"))
        self.bhistorial.setTitle(_translate("Remates JCN", "Historial de Carga"))
        self.finCarreraBtn.setText(_translate("Remates JCN", "Finalizar Carrera"))
        self.menuMen.setTitle(_translate("Remates JCN", "Parámetros"))
        self.menuAcciones.setTitle(_translate("Remates JCN", "Impresiones"))
        self.menuEdicion.setTitle(_translate("Remates JCN", "Edición"))
        self.actionCarreras.setText(_translate("Remates JCN", "Seleccionar Carrera"))
        self.actionCaballos.setText(_translate("Remates JCN", "Caballos"))
        self.actionImprimir_remates.setText(_translate("Remates JCN", "Imprimir Remates"))
        self.actionImprimir_Carrera.setText(_translate("Remates JCN", "Imprimir Carrera"))
        self.actionTicket.setText(_translate("Remates JCN", "Imprimir Ticket"))
        self.actionEliminar_Remate.setText(_translate("Remates JCN", "Eliminar Remate"))
        self.actionEliminar_Caballo.setText(_translate("Remates JCN", "Eliminar Caballo"))
        self.actionEliminar_Carrera.setText(_translate("Remates JCN", "Eliminar Carrera"))
        self.actionSalir.setText(_translate("Remates JCN", "Salir"))

    def retranslate_2(self):
        _translate = QtCore.QCoreApplication.translate
        m=0
        while(m<len(self.labels)):
            self.labels[m].setText(_translate("SubWidget", str(m+1)))
            m+=1
        self.montos.setText(_translate("SubWidget", "Montos"))
        self.caballos.setText(_translate("SubWidget", "Caballos"))  
        self.descartar.setText(_translate("SubWidget", "Descartar"))
        self.guardar.setText(_translate("SubWidget", "Guardar"))

    #Metodos
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self, "Cerrar", "¿Seguro que quiere salir?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def dialogCarrera(self):
        self.dlg = QtWidgets.QDialog()
        self.dlg.resize(372, 102)
        self.d1 = QtWidgets.QLabel(self.dlg)
        self.d1.setGeometry(QtCore.QRect(20, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.d1.setFont(font)
        self.d1.setAlignment(QtCore.Qt.AlignCenter)
        self.d1.setObjectName("label")
        self.d2 = QtWidgets.QLabel(self.dlg)
        self.d2.setGeometry(QtCore.QRect(210, 10, 151, 31))
        self.d2.setFont(font)
        self.d2.setAlignment(QtCore.Qt.AlignCenter)
        self.d2.setObjectName("montos")
        self.d3 = QtWidgets.QFrame(self.dlg)
        self.d3.setGeometry(QtCore.QRect(180, -10, 20, 131))
        self.d3.setFrameShape(QtWidgets.QFrame.VLine)
        self.d3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.d3.setObjectName("line")
        self.creaB = QtWidgets.QPushButton(self.dlg)
        self.creaB.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.creaB.setObjectName("creaB")
        self.creaB.setText("Crear")
        self.creaB.clicked.connect(self.crear)
        self.creaB.clicked.connect(self.dlg.close)
        self.d1.setText("Seleccionar Carrera")
        self.d2.setText("Crear Carrera")
        idsCar = self.sess.execute("SELECT id FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).fetchall()
        self.combo = QtWidgets.QComboBox(self.dlg)
        self.combo.setGeometry(60, 50, 90, 23)
        self.combo.setPlaceholderText("None")
        for id in idsCar:
            query = self.sess.execute("SELECT numero FROM carrera WHERE idReunion = :reu AND id = :val", {'reu': self.idReunion, 'val' : id[0]}).scalar()
            if(query is not None):
                self.combo.addItem(str(query))
        self.sess.close()
        self.combo.activated[str].connect(self.seleccion)
        self.combo.activated.connect(self.dlg.close)
        self.dlg.exec_()

    def crear(self):
        try:
            self.idCarrera = self.sess.execute("SELECT id FROM carrera WHERE ROWID IN (SELECT max( ROWID ) FROM carrera)").scalar() + 1
        except:
            self.idCarrera = 1
        try:
            self.nroCarrera = self.sess.execute("SELECT numero FROM carrera WHERE ROWID IN (SELECT max( ROWID ) FROM carrera WHERE idReunion = :val)", {'val' : self.idReunion}).scalar() + 1
        except:
            self.nroCarrera = 1
        self.sess.execute("INSERT INTO carrera(id, idReunion, numero) VALUES (:val, :par, :var)", {'val' : self.idCarrera, 'par' : self.idReunion, 'var' : self.nroCarrera})
        self.sess.commit()
        self.sess.close()
        self.horses()
        self.xy.setText(str(self.nroCarrera))

    def seleccion(self, text):
        qry = self.sess.execute("SELECT * FROM carrera WHERE idReunion = :val AND numero=:par", {'val' : self.idReunion, 'par' : text}).fetchall()
        self.idCarrera = qry[0][0]
        rems = self.sess.execute("SELECT COUNT(*) FROM remate WHERE idCarrera = :car", {'car':self.idCarrera})
        self.nroCarrera = int(text)
        totalCarrera = qry[0][4]
        if(totalCarrera is not None):
            totalARendir = qry[0][6]
            totalAPagar = qry[0][5]
            self.subtotales.setText("<b>"+str(rems)+" Remates - Total $"+str(totalCarrera)+"</b><br><br><b>A Rendir</b> $"+str(round(totalARendir, 2))+"<br><br><b>A Pagar</b> $"+str(round(totalAPagar, 2)))
        else:
            self.subtotales.setText("<b>Aún no se cargaron remates</b>")
        try:
            self.cantCaballos = self.sess.execute("SELECT cantCaballos FROM carrera WHERE id = :id", {'id' : self.idCarrera}).scalar()
            self.showCaja()
            self.setPorcentaje()
        except:
            self.horses()
        self.sess.close()
        self.xy.setText(str(self.nroCarrera))

    def horses(self):
        self.cabs = QtWidgets.QDialog()
        self.cabs.resize(270, 90)
        self.cabs.setMinimumSize(QtCore.QSize(270, 90))
        self.cabs.setMaximumSize(QtCore.QSize(270, 90))
        self.labelCab = QtWidgets.QLabel(self.cabs)
        self.labelCab.setGeometry(QtCore.QRect(30, 10, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCab.setFont(font)
        self.labelCab.setObjectName("labelCab")
        self.labelCab.setText("Cantidad de caballos en carrera")
        self.lineCab = QtWidgets.QLineEdit(self.cabs)
        self.lineCab.setGeometry(QtCore.QRect(130, 40, 40, 20))
        self.lineCab.setObjectName("labelCab")
        self.lineCab.setValidator(QtGui.QIntValidator())
        self.lineCab.returnPressed.connect(self.setCabs)
        self.lineCab.returnPressed.connect(self.cabs.close)
        self.lineCab.returnPressed.connect(self.showCaja)
        self.cabs.exec_()

    def setCabs(self):
        self.cantCaballos = int(self.lineCab.text())
        sess = utils.bd()
        sess.execute("UPDATE carrera SET cantCaballos = :cab WHERE id = :reu", {'cab' : self.cantCaballos, 'reu' : self.idCarrera})
        sess.commit()
        sess.close()
        self.setPorcentaje()
        self.cabsNameW()

    def cabsNameW(self):
        cant = int(self.cantCaballos)
        self.cabsName = QtWidgets.QDialog()
        self.cabsName.resize(360, 130+((cant-2)*30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelName = QtWidgets.QLabel(self.cabsName)
        self.labelName.setGeometry(QtCore.QRect(10, 0, 341, 41))
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName("label")
        self.labelName.setText("Ingrese los nombres de los caballos en carrera")
        self.cabsNames = []
        self.cabsNumber = []
        i = 0
        h = 40
        while(i<cant):
            self.cabsNames.append(QtWidgets.QLineEdit(self.cabsName))
            self.cabsNames[i].setGeometry(QtCore.QRect(100, h, 171, 20))
            self.cabsNumber.append(QtWidgets.QLabel(self.cabsName))
            self.cabsNumber[i].setGeometry(QtCore.QRect(70, h, 16, 16))
            self.cabsNumber[i].setFont(font)
            self.cabsNumber[i].setAlignment(QtCore.Qt.AlignCenter)
            self.cabsNumber[i].setObjectName("nro"+str(i+1))
            self.cabsNumber[i].setText(str(i+1))
            i += 1
            h += 30
        self.pushButton = QtWidgets.QPushButton(self.cabsName)
        self.pushButton.setGeometry(QtCore.QRect(140, h, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Confirmar")
        self.pushButton.clicked.connect(self.saveNames)
        self.pushButton.clicked.connect(self.cabsName.close)
        self.cabsName.exec_()

    def saveNames(self):
        i = 0
        self.strNames = ""
        while(i<len(self.cabsNames)):
            nombre = self.cabsNames[i].text()
            if(nombre != ""):
                self.strNames += nombre
            else:
                self.strNames += "Sin nombre"
            if(i!=len(self.cabsNames)-1):
                self.strNames += "|"
            i += 1
        self.sess.execute("UPDATE carrera SET names = :nom WHERE id = :car", {'nom':self.strNames, 'car':self.idCarrera})
        self.sess.commit()
        self.sess.close()

    def setPorcentaje(self):
        if(self.cantCaballos==2):
            self.diezP.setChecked(True)
        elif(self.cantCaballos==3):
            self.veinteP.setChecked(True)
        else:
            self.treintaP.setChecked(True)   

    def boxCarga(self):
        self.caja = QtWidgets.QGroupBox(self.centralwidget)
        self.caja.setGeometry(QtCore.QRect(10, 10, 221, 561))
        self.caja.setTitle("")
        self.caja.setObjectName("bcarga")
        #Lineas
        self.lines = []
        i = 0
        h = 40
        while(i<int(self.cantCaballos)):
            self.lines.append(QtWidgets.QLineEdit(self.caja))
            self.lines[i].setGeometry(QtCore.QRect(110, h, 101, 20))
            self.lines[i].setObjectName('line{}'.format(i))
            self.lines[i].setValidator(QtGui.QIntValidator())
            i+=1
            h+=30
        #Labels
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labels = []
        k = 0
        l = 40
        while(k<int(self.cantCaballos)):
            self.labels.append(QtWidgets.QLabel(self.caja))
            self.labels[k].setFont(font)
            if(k<9):
                self.labels[k].setGeometry(QtCore.QRect(80, l, 16, 16))
            else:
                self.labels[k].setGeometry(QtCore.QRect(70, l, 22, 16))
            self.labels[k].setObjectName("c"+str(k))
            k+=1
            l+=30
        
        self.caballos = QtWidgets.QLabel(self.caja)
        self.caballos.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.caballos.setFont(font)
        self.caballos.setObjectName("caballos")

        self.montos = QtWidgets.QLabel(self.caja)
        self.montos.setGeometry(QtCore.QRect(120, 10, 71, 21))
        self.montos.setFont(font)
        self.montos.setObjectName("montos")

        #Deco
        self.line = QtWidgets.QFrame(self.caja)
        self.line.setGeometry(QtCore.QRect(90, 0, 20, 520))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.caja)
        self.line_2.setGeometry(QtCore.QRect(0, 510, 221, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        #Boton Descartar
        self.descartar = QtWidgets.QPushButton(self.caja)
        self.descartar.setGeometry(QtCore.QRect(0, 530, 101, 31))
        font = QtGui.QFont()
        font.setWeight(50)
        self.descartar.setFont(font)
        self.descartar.setObjectName("descartar")
        self.descartar.clicked.connect(self.clearAll)
        #Boton Guardar
        self.guardar = QtWidgets.QPushButton(self.caja)
        self.guardar.setGeometry(QtCore.QRect(110, 530, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.guardar.setFont(font)
        self.guardar.setObjectName("guardar")
        self.guardar.setAutoDefault(True)
        self.guardar.clicked.connect(self.saveOrUpd)
        self.retranslate_2()
        QtCore.QMetaObject.connectSlotsByName(self.caja)
        self.caja.setTabOrder(self.lremate, self.lines[0])
        k=0
        while(k<len(self.lines)-1):
            self.setTabOrder(self.lines[k], self.lines[k+1])
            k+=1
        self.setTabOrder(self.lines[k], self.guardar)
        self.setTabOrder(self.guardar, self.descartar)
        return self.caja

    def showCaja(self):
        if(self.cajaCarga is not None):
            self.cajaCarga.close()
        self.cajaCarga = self.boxCarga()
        self.cajaCarga.show()

    def clearAll(self, checked=False):
        for field in self.lines:
            field.clear()

    def saveOrUpd(self):
        nro = self.lremate.text()
        self.idRemate = self.sess.execute("SELECT id FROM remate WHERE numero = :num AND idCarrera = :car", {'num':nro, 'car':self.idCarrera}).scalar()
        if(nro == ""):
            QtWidgets.QMessageBox.about(self, "Remate", "Debe ingresar el número de remate")
        elif(self.idRemate is not None):
            self.nroRemate = int(nro)
            self.updRemate()
        else:
            self.nroRemate = int(nro)
            self.save()
            self.clearAll()

    def save(self):
        self.lines[0].setFocus()
        i = 1
        noms = self.sess.execute("SELECT names FROM carrera WHERE id = :car", {'car':self.idCarrera}).fetchall()
        noms = noms[0][0].split(sep='|')
        try:
            self.idRemate = self.sess.execute("SELECT id FROM remate WHERE ROWID IN ( SELECT max( ROWID ) FROM remate )").scalar() + 1
        except:
            self.idRemate = 1
        self.txt += "<p style=\"font-size: 20px\">"
        self.txt += "<b>Remate "+str(self.nroRemate)+"</b><br>"
        if(self.diezP.isChecked()):
            porc = 0.127
            self.txt += "Porcentaje 10%"
        if(self.veinteP.isChecked()):
            porc = 0.224
            self.txt += "Porcentaje 20%"
        if(self.treintaP.isChecked()):
            porc = 0.321
            self.txt += "Porcentaje 30%"
        self.sess.execute("INSERT INTO remate(id, idCarrera, numero, porcentaje) VALUES (:val, :par, :var, :car)", {'val' : self.idRemate, 'par' : self.idCarrera, 'var' : self.nroRemate, 'car' : porc})
        for it in self.lines:
            self.rmt = it.text()
            if(self.rmt == ""):
                self.rmt = None
                self.txt += "<br>"+str(i)+")"+noms[i-1]+" ---> $0"
            else:
                self.rmt = int(self.rmt)
                self.txt += "<br>"+str(i)+")"+noms[i-1]+" ---> $"+str(self.rmt)
            try:
                self.idCaballo = self.sess.execute("SELECT id FROM caballo WHERE ROWID IN (SELECT max(ROWID) FROM caballo)").scalar() + 1
            except:
                self.idCaballo = 1
            self.sess.execute("INSERT INTO caballo(id, idCarrera, idRemate, numero, monto) VALUES (:val, :par, :rem, :var, :car)", {'val' : self.idCaballo, 'par' : self.idCarrera, 'rem' : self.idRemate, 'var' : i, 'car' : self.rmt})
            i+=1
        total = self.sess.execute("SELECT SUM(monto) FROM caballo WHERE idRemate = :var", {'var' : self.idRemate}).scalar()
        self.sess.execute("UPDATE remate SET total = :tot WHERE id = :rem", {'tot' : total, 'rem' : self.idRemate})
        self.cuentasRemate(self.idCarrera, self.idRemate)
        self.cuentasCarrera(self.idCarrera)
        self.sess.commit()
        self.sess.close()
        self.txt += "</p><br>"
        self.txtHistorial.append(self.txt)
        self.txt = ""
        self.lremate.setText(str(self.nroRemate + 1))

    def updRemate(self):
        noms = self.sess.execute("SELECT names FROM carrera WHERE id = :car", {'car':self.idCarrera}).fetchall()
        noms = noms[0][0].split(sep='|')
        self.idRemate = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car AND numero = :rem", {'car' : self.idCarrera, 'rem' : self.nroRemate}).scalar()
        self.txt += "<p style=\"font-size: 20px\">"
        self.txt += "<b>Remate "+str(self.nroRemate)+"</b> (Actualizado)<br>"
        if(self.diezP.isChecked()):
            porc = 0.127
            self.txt += "Porcentaje 10%"
        if(self.veinteP.isChecked()):
            porc = 0.224
            self.txt += "Porcentaje 20%"
        if(self.treintaP.isChecked()):
            porc = 0.321
            self.txt += "Porcentaje 30%"
        i = 1
        for it in self.lines:
            self.rmt = it.text()
            if(self.rmt == ""):
                self.rmt = None
                self.txt += "<br>"+str(i)+")"+noms[i-1]+" ---> $0"
            else:
                self.rmt = int(self.rmt)
                self.txt += "<br>"+str(i)+")"+noms[i-1]+" ---> $"+str(self.rmt)
            self.idCaballo = self.sess.execute("SELECT id FROM caballo WHERE idRemate = :rem AND numero = :num", {'rem' : self.idRemate, 'num' : i}).scalar()
            self.sess.execute("UPDATE caballo SET monto = :mon WHERE id = :cab", {'mon' : self.rmt, 'cab' : self.idCaballo})
            i+=1
        total = self.sess.execute("SELECT SUM(monto) FROM caballo WHERE idRemate = :var", {'var' : self.idRemate}).scalar()
        self.sess.execute("UPDATE remate SET porcentaje = :por, total = :tot WHERE id = :rem", {'por' : porc, 'tot' : total, 'rem' : self.idRemate})
        msg = QtWidgets.QMessageBox.question(self, "Actualizar", "El remate ya se encuentra cargado, actualizar?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg == QtWidgets.QMessageBox.Yes:
            self.cuentasRemate(self.idCarrera, self.idRemate)
            self.cuentasCarrera(self.idCarrera)
            self.sess.commit()
            self.sess.close()
            self.txt += "</p><br>"
            self.txtHistorial.append(self.txt)
            self.txt = ""
            self.clearAll()
            self.lremate.setText(str(self.nroRemate + 1))
        else:
            self.sess.rollback()
            self.txt = ""
            self.sess.close()

    def eliminador(self, _str):
        self.elimina = QtWidgets.QDialog()
        self.elimina.resize(270, 90)
        self.elimina.setMinimumSize(QtCore.QSize(270, 90))
        self.elimina.setMaximumSize(QtCore.QSize(270, 90))
        self.labelElimina = QtWidgets.QLabel(self.elimina)
        self.labelElimina.setGeometry(QtCore.QRect(30, 10, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelElimina.setFont(font)
        self.labelElimina.setObjectName("labelDel")
        self.lineElimina = QtWidgets.QLineEdit(self.elimina)
        self.lineElimina.setGeometry(QtCore.QRect(130, 40, 40, 20))
        self.lineElimina.setObjectName("labelDel")
        self.lineElimina.setValidator(QtGui.QIntValidator())
        if(_str=='cab'):
            self.labelElimina.setText("Ingrese el numero de caballo:")
            self.lineElimina.returnPressed.connect(self.eliminaCaballo)
        if(_str=='rem'):
            self.labelElimina.setText("Ingrese el numero de remate:")
            self.lineElimina.returnPressed.connect(self.eliminaRemate)
        if(_str=='car'):
            self.labelElimina.setText("Ingrese el numero de carrera:")
            self.lineElimina.returnPressed.connect(self.eliminaCarrera)
        self.elimina.show()

    def eliminaRemate(self):
        rem = int(self.lineElimina.text())
        qry = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car AND numero = :rem", {'car':self.idCarrera, 'rem':int(rem)}).scalar()
        if(qry is None):
            QtWidgets.QMessageBox.about(self, "Remate", "El remate no existe en esta carrera")
        else:
            self.sess.execute("DELETE FROM caballo WHERE idCarrera = :car AND idRemate = :rem", {'car':self.idCarrera, 'rem':qry})
            self.sess.execute("DELETE FROM remate WHERE idCarrera = :car AND id = :idr", {'car':self.idCarrera, 'idr':qry})
            msg = QtWidgets.QMessageBox.question(self, "Eliminar", "El remate se eliminará, proceder?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if msg == QtWidgets.QMessageBox.Yes:
                self.cuentasCarrera(self.idCarrera)
                self.sess.commit()
            else:
                self.sess.rollback()
        self.sess.close()
        self.elimina.close()

    def eliminaCaballo(self):
        cab = int(self.lineElimina.text())
        qry = self.sess.execute("SELECT cantCaballos FROM carrera WHERE id = :car", {'car':self.idCarrera}).scalar()
        if(qry<cab):
            QtWidgets.QMessageBox.about(self, "Caballo", "El caballo no existe en esta carrera")
        else:
            self.sess.execute("UPDATE caballo SET monto = NULL WHERE idCarrera = :car AND numero = :cab", {'car':self.idCarrera, 'cab':cab})
            msg = QtWidgets.QMessageBox.question(self, "Eliminar", "El caballo se eliminará de todos los remates en esta carrera, proceder?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if msg == QtWidgets.QMessageBox.Yes:
                ids = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car", {'car':self.idCarrera})
                ids = ids.fetchall()
                for rem in ids:
                    tot = self.sess.execute("SELECT SUM(monto) FROM caballo WHERE idCarrera = :var AND idRemate = :rem", {'var' : self.idCarrera, 'rem':rem[0]}).scalar()
                    porc = 0.321
                    z = 1
                    c = 0
                    while(z<=qry):
                        cont = self.sess.execute("SELECT monto FROM caballo WHERE idCarrera = :car AND idRemate = :rem AND numero = :num",{'car':self.idCarrera, 'rem':rem[0], 'num':z}).scalar()
                        if(cont is not None):
                            c+=1
                        z+=1
                    if(c==2):
                        porc = 0.127
                    if(c==3):
                        porc = 0.224
                    self.sess.execute("UPDATE remate SET porcentaje = :por, total = :tot WHERE id = :rem", {'por':porc, 'tot' : tot, 'rem' : rem[0]})
                    self.cuentasRemate(self.idCarrera, rem[0])
                    self.cuentasCarrera(self.idCarrera)
                self.sess.commit()
            else:
                self.sess.rollback()
        self.sess.close()
        self.elimina.close()

    def eliminaCarrera(self):
        car = int(self.lineElimina.text())
        qry = self.sess.execute("SELECT id FROM carrera WHERE idReunion = :reu AND numero = :num",{'reu':self.idReunion, 'num':car}).scalar()
        if(qry is None):
            QtWidgets.QMessageBox.about(self, "Carrera", "La carrera no existe")
        else:
            self.sess.execute("DELETE FROM caballo WHERE idCarrera = :car", {'car':qry})
            self.sess.execute("DELETE FROM remate WHERE idCarrera = :car", {'car':qry})
            self.sess.execute("DELETE FROM carrera WHERE id = :car", {'car':qry})
            msg = QtWidgets.QMessageBox.question(self, "Eliminar", "La carrera y todos sus remates se eliminarán, proceder?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if msg == QtWidgets.QMessageBox.Yes:
                self.sess.commit()
                if(qry == self.idCarrera):
                    self.idCarrera = None
                    self.nroCarrera = None
                    self.cantCaballos = None
                    self.idRemate = None
                    self.nroRemate = None
                    self.cajaCarga.close()
                    self.cajaCarga = None
                    self.strNames = ""
                    self.xy.setText("")
                    self.subtotales.setText("")
                    self.txtHistorial.setText("")
                    self.sess.close()
                    self.elimina.close()
                    self.dialogCarrera()
            else:
                self.sess.rollback()
                self.sess.close()
                self.elimina.close()

    def cuentasRemate(self, idCar, idRem):
        totalRemate = self.sess.execute("SELECT total FROM remate WHERE idCarrera = :car AND id = :rem", {'car':idCar, 'rem':idRem}).scalar()
        porc = self.sess.execute("SELECT porcentaje FROM remate WHERE idCarrera = :car AND id = :rem", {'car':idCar, 'rem':idRem}).scalar()
        aRendir = totalRemate * porc
        aPagar = totalRemate - aRendir
        self.sess.execute("UPDATE remate SET aPagar = :apa, aRendir = :are WHERE idCarrera = :car AND id = :rem", {'apa':aPagar, 'are':aRendir, 'car':idCar, 'rem':idRem})
       
    def cuentasCarrera(self, idCar):
        rems = self.sess.execute("SELECT COUNT(*) FROM remate WHERE idCarrera = :car", {'car':idCar}).scalar()
        totalCarrera = self.sess.execute("SELECT SUM(total) FROM remate WHERE idCarrera = :car", {'car':idCar}).scalar()
        self.sess.execute("UPDATE carrera SET total = :tot WHERE id = :car", {'tot':totalCarrera, 'car':idCar})
        totalAPagar = self.sess.execute("SELECT SUM(aPagar) FROM remate WHERE idCarrera = :car", {'car':idCar}).scalar()
        totalARendir = self.sess.execute("SELECT SUM(aRendir) FROM remate WHERE idCarrera = :car", {'car':idCar}).scalar()
        self.sess.execute("UPDATE carrera SET aRendir = :are, aPagar = :apa WHERE id = :car AND idReunion = :reu", {'are':totalARendir, 'apa':totalAPagar, 'car':idCar, 'reu':self.idReunion})
        self.subtotales.setText("<b>"+str(rems)+" Remates - Total $"+str(totalCarrera)+"</b><br><br><b>A Rendir</b> $"+str(round(totalARendir, 2))+"<br><br><b>A Pagar</b> $"+str(round(totalAPagar, 2)))
        
    def resetPdfVars(self):
        self.fontPdf = "Courier"
        self.sizePdf = 10
        self.ydata = 820 #pos y de datos globales
        self.xdatalft = [20, 105, 220] #pos x de datos globales izq
        self.xdatargt = [310, 395, 510] #pos x de datos globalez der
        self.xcablft = [30, 55, 225] #pos x cabecera de tabla izq
        self.xcabrgt = [320, 345, 515] #pos x cabecera de tabla der
        self.ygrid = [] #eje y de primera linea de los grid
        self.xgridlft = [20, 50, 200, 280] #eje x de lineas verticales de grid izq
        self.xgridrgt = [310, 340, 490, 570] #eje x de lineas verticales de grid der
    
    def imprimeRemates(self):
        self.resetPdfVars()
        mesa = self.sess.execute("SELECT mesa FROM reunion WHERE id = :reu", {'reu':self.idReunion}).scalar()
        idRems = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car", {'car':self.idCarrera}).fetchall()
        cantCabs = self.sess.execute("SELECT cantCaballos FROM carrera WHERE id = :car", {'car':self.idCarrera}).scalar()
        nombres = self.sess.execute("SELECT names FROM carrera WHERE id = :car", {'car':self.idCarrera}).fetchall()
        nombres = nombres[0][0].split(sep='|')
        i = 0
        c = canvas.Canvas("pdfs/remates/remates_carrera_"+str(self.nroCarrera)+".pdf")
        c.setFont(self.fontPdf, self.sizePdf)
        #linea vertical
        c.saveState()
        c.setDash(1, 2)
        c.line(295, 825, 295, 5)
        c.restoreState()
        #fin linea vertical
        largo = 0
        for id in idRems:
            nroRem = self.sess.execute("SELECT numero FROM remate WHERE id = :rem", {'rem':id[0]}).scalar()
            start = self.ydata
            self.ygrid = []
            if(start - largo < 0):
                c.showPage()
                self.resetPdfVars()
                start = self.ydata
                c.setFont(self.fontPdf, self.sizePdf)
                #linea vertical
                c.saveState()
                c.setDash(1, 2)
                c.line(295, 825, 295, 5)
                c.restoreState()
                #fin linea vertical
            if(i%2==0):
                xtop = 95
                xdata = self.xdatalft
                xcab = self.xcablft
                xgrid = self.xgridlft
                xtot = 20
            else:
                xtop = 385
                xdata = self.xdatargt
                xcab = self.xcabrgt
                xgrid = self.xgridrgt
                xtot = 310
            c.saveState()
            c.setFont("Courier-Bold", 10)
            c.drawString(xtop, self.ydata, "Mesa de Remates N° "+str(mesa))
            self.ydata -= 15
            c.drawString(xdata[0], self.ydata, "Carrera " + str(self.nroCarrera) + "  //")
            c.drawString(xdata[1], self.ydata, "Remate N°" + str(nroRem))
            c.drawString(xdata[2], self.ydata, str(self.fec))
            self.ydata -= 22
            c.drawString(xcab[0], self.ydata + 3, "N°")
            c.drawString(xcab[1], self.ydata + 3, "Nombre")
            c.drawString(xcab[2], self.ydata + 3, "Monto")
            c.restoreState()
            self.ygrid.append(self.ydata + 15)
            j = 0
            while(j<cantCabs):
                j += 1
                self.ygrid.append(self.ydata)
                self.ydata -= 15
                if(j<10):
                    c.drawString(xcab[0]+3, self.ydata + 3, str(j))
                else:
                    c.drawString(xcab[0], self.ydata + 3, str(j))
                c.drawString(xcab[1], self.ydata + 3, nombres[j-1])
                monto = self.sess.execute("SELECT monto FROM caballo WHERE idRemate = :rem AND numero = :num", {'rem':id[0], 'num':j}).scalar()
                if(monto is None):
                    c.drawString(xcab[2] - 5, self.ydata + 3, "$0")
                else:
                    c.drawString(xcab[2] - 5, self.ydata + 3, "$" + str(monto))
            montos = self.sess.execute("SELECT total, aPagar, aRendir FROM remate WHERE id = :rem", {'rem':id[0]}).fetchall()
            total = montos[0][0]
            apagar = montos[0][1]
            arendir = montos[0][2]
            self.ygrid.append(self.ydata)
            c.grid(xgrid, self.ygrid)
            self.ygrid = []
            self.ydata -= 15
            c.drawString(xtot, self.ydata, "Total Remate: $" + str(round(total, 2)))
            self.ydata -= 15
            c.drawString(xtot, self.ydata, "Descuentos: $" + str(round(arendir, 2)))
            c.saveState()
            c.setFont("Courier-Bold", 11)
            self.ydata -= 15
            c.drawString(xtot, self.ydata, "TOTAL A PAGAR: $" + str(round(apagar, 2)))
            c.restoreState()
            self.ydata -= 10
            if(i==0):
                largo = start - self.ydata
            if(i%2==0):
                #linea horizonal
                c.saveState()
                c.setDash(1, 2)
                c.line(15, self.ydata, 575, self.ydata)
                c.restoreState()
                #fin linea horizonal
                self.ydata = start
            else:
                self.ydata -= 15
            i += 1
        self.sess.close()
        c.save()

    def imprimeCarrera(self):
        recaudado = 0
        total = 0
        adm = 0
        sub = 0
        subtotal = 0
        descuento = 0
        apagar = 0
        arendir = 0
        idrems = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car", {'car':self.idCarrera})
        mesa = self.sess.execute("SELECT mesa FROM reunion WHERE id = :reu", {'reu':self.idReunion}).scalar()
        c = canvas.Canvas("pdfs/carreras/rendimiento_carrera_"+str(self.nroCarrera)+".pdf")
        c.setFont("Courier-Bold", 10)
        y = 820
        c.drawString(20, y, "Carrera "+str(self.nroCarrera) + " //")
        c.drawString(100, y, "Mesa de Remate N° "+str(mesa))
        c.drawString(340, y, "Fecha: "+str(self.fec))
        y -= 20
        c.drawString(25, y, "N° Remate")
        c.drawString(85, y, "Recaudado")
        c.drawString(165, y, "Adm")
        c.drawString(225, y, "Subtotal")
        c.drawString(300, y, "Descuentos")
        c.drawString(380, y, "A Pagar")
        y -= 10
        xgridr = [20, 80, 145, 210, 290, 365, 440]
        ygridr = []
        ygridr.append(y + 25)
        for id in idrems:
            dataRem = self.sess.execute("SELECT * FROM remate WHERE id = :rem", {'rem':id[0]}).fetchall()
            recaudado = dataRem[0][4]
            total += recaudado
            porc = dataRem[0][3]
            tresP = (recaudado * 0.03)
            adm += tresP
            sub = recaudado - tresP
            subtotal += sub
            if(porc == 0.127):
                desc = sub * 0.1
                descuento += desc
            if(porc == 0.224):
                desc = sub * 0.2
                descuento += desc
            if(porc == 0.321):
                desc = sub * 0.3
                descuento += desc
            apagar += dataRem[0][5]
            arendir += dataRem[0][6]
            ygridr.append(y)
            y -= 15
            c.drawString(25, y + 3.5, str(dataRem[0][2]))
            c.drawString(90, y + 3.5, "$"+str(dataRem[0][4]))
            c.drawString(160, y + 3.5, "$"+str(round(tresP, 2)))
            c.drawString(225, y + 3.5, "$"+str(round(sub, 2)))
            c.drawString(305, y + 3.5, "$"+str(round(desc, 2)))
            c.drawString(380, y + 3.5, "$"+str(round(dataRem[0][5], 2)))
        self.sess.close()
        ygridr.append(y)
        y -= 15
        c.drawString(25, y + 3.5, "TOTALES")
        c.drawString(90, y + 3.5, "$"+str(round(total, 2)))
        c.drawString(160, y + 3.5, "$"+str(round(adm, 2)))
        c.drawString(225, y + 3.5, "$"+str(round(subtotal, 2)))
        c.drawString(305, y + 3.5, "$"+str(round(descuento, 2)))
        c.drawString(380, y + 3.5, "$"+str(round(apagar, 2)))
        ygridr.append(y)
        c.grid(xgridr, ygridr)
        y -= 20
        c.setFont("Courier-Bold", 12)
        c.drawString(20, y, "TOTAL A RENDIR $"+str(round(arendir, 2)))
        c.save()

    def finCarrera(self):
        msg = QtWidgets.QMessageBox.question(self, "Finalizar", "Desea finalizar esta carrera?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg == QtWidgets.QMessageBox.Yes:
            try:
                self.imprimeRemates()
                self.imprimeCarrera()
                self.idCarrera = None
                self.nroCarrera = None
                self.cantCaballos = None
                self.idRemate = None
                self.nroRemate = None
                self.cajaCarga.close()
                self.cajaCarga = None
                self.strNames = ""
                self.xy.setText("")
                self.subtotales.setText("")
                self.txtHistorial.setText("")
                msg = QtWidgets.QMessageBox.question(self, "Crear o cerrar", "Desea crear una nueva carrera?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
                if msg == QtWidgets.QMessageBox.Yes:
                    self.crear()
                else:
                    self.dialogCarrera()
            except Exception as e:
                if(e):
                    print(e)
                    QtWidgets.QMessageBox.about(self, "Atención", "No hay ninguna carrera seleccionada.")
                else:
                    QtWidgets.QMessageBox.about(self, "Atención", "Recuerde cerrar los pdf's abiertos.")
        else:
            pass

    def buscador(self):
        self.busca = QtWidgets.QDialog()
        self.busca.resize(270, 90)
        self.busca.setMinimumSize(QtCore.QSize(270, 90))
        self.busca.setMaximumSize(QtCore.QSize(270, 90))
        self.labelBusca = QtWidgets.QLabel(self.busca)
        self.labelBusca.setGeometry(QtCore.QRect(30, 10, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelBusca.setFont(font)
        self.labelBusca.setObjectName("labelBus")
        self.labelBusca.setText("Ingrese el numero de remate:")
        self.lineBusca = QtWidgets.QLineEdit(self.busca)
        self.lineBusca.setGeometry(QtCore.QRect(130, 40, 40, 20))
        self.lineBusca.setObjectName("labelBus")
        self.lineBusca.setValidator(QtGui.QIntValidator())
        self.lineBusca.returnPressed.connect(self.buscaRemate)
        self.busca.show()

    def buscaRemate(self):
        rem = int(self.lineBusca.text())
        qry = self.sess.execute("SELECT * FROM remate WHERE idCarrera = :car AND numero = :rem", {'car':self.idCarrera, 'rem':rem}).fetchall()
        try:
            conn = SerialConnection.create('COM1:19200,8,1,N,RTSCTS')
            printer = GenericESCPOS(conn)
            printer.init()
        except:
            QtWidgets.QMessageBox.about(self, "Impresora", "La impresora está apagada o desconectada")
            self.busca.close()
        else:
            if(qry is None):
                QtWidgets.QMessageBox.about(self, "Remate", "El remate no existe")
            else:
                cabs = self.sess.execute("SELECT * FROM caballo WHERE idRemate = :rem", {'rem':qry[0][0]}).fetchall()
                names = self.sess.execute("SELECT names FROM carrera WHERE id = :car", {'car':self.idCarrera}).fetchall()
                nombres = names[0][0].split(sep='|')
                printer.set_text_size(1, 1)
                printer.set_emphasized(True)
                printer.text_center(str(self.fec))
                printer.text_left('Mesa de Remate N° 2')
                printer.set_text_size(0, 0)
                printer.set_emphasized(False)
                for cab in cabs:
                    numero = cab[3]
                    monto = cab[4]
                    nombre = nombres[numero - 1]
                    printer.text_left(str(numero)+ " " + nombre)
                    printer.text_right("$"+str(monto))
                recaudado = qry[0][4]
                desc = qry[0][6]
                apagar = qry[0][5]
                printer.text_left('Total')
                printer.text_right('$'+str(recaudado))
                printer.text_left('Descuentos')
                printer.text_right('$'+str(desc))
                printer.set_text_size(1, 1)
                printer.set_emphasized(True)
                printer.text_left('A PAGAR')
                printer.text_right('$'+str(apagar))
                self.lineBusca.clear()