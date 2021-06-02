import sys
sys.path.append("./")
from PyQt5 import QtCore, QtGui, QtWidgets
import utils
import datetime

class Ui_MainWindow(QtWidgets.QWidget):
    idCarrera = None
    nroCarrera = None
    cantCaballos = None
    idRemate = None
    nroRemate = None
    cajaCarga = None
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
        self.bhistorial.setGeometry(QtCore.QRect(240, 170, 351, 401))
        self.bhistorial.setObjectName("bhistorial")
        self.whistorial = QtWidgets.QWidget(self.bhistorial)
        self.whistorial.setGeometry(QtCore.QRect(10, 20, 331, 371))
        self.whistorial.setObjectName("whistorial")
        self.pdfHistorial = QtWidgets.QTextBrowser(self.whistorial)
        self.pdfHistorial.setGeometry(QtCore.QRect(0, 0, 331, 371))
        self.pdfHistorial.setObjectName("pdfHistorial")
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
        self.actionImprimir_Carrera = QtWidgets.QAction(MainWindow)
        self.actionImprimir_Carrera.setObjectName("actionImprimir_Carrera")
        self.actionImprimir_Reunion = QtWidgets.QAction(MainWindow)
        self.actionImprimir_Reunion.setObjectName("actionImprimir_Reunion")
        self.actionEditar_Remate = QtWidgets.QAction(MainWindow)
        self.actionEditar_Remate.setObjectName("actionEditar_Remate")
        self.actionEliminar_Caballo = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Caballo.setObjectName("actionEliminar_Caballo")
        self.actionEliminar_Carrera = QtWidgets.QAction(MainWindow)
        self.actionEliminar_Carrera.setObjectName("actionEliminar_Carrera")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionSalir.triggered.connect(self.close)
        self.menuMen.addAction(self.actionCarreras)
        self.menuMen.addAction(self.actionCaballos)
        self.menuMen.addAction(self.actionSalir)
        self.menuAcciones.addAction(self.actionImprimir_remates)
        self.menuAcciones.addAction(self.actionImprimir_Carrera)
        self.menuAcciones.addAction(self.actionImprimir_Reunion)
        self.menuEdicion.addAction(self.actionEditar_Remate)
        self.menuEdicion.addAction(self.actionEliminar_Caballo)
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
        self.subtotales.setHtml(_translate("Remates JCN", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Recaudado        $var</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">A Pagar        $var</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">A Rendir        $var</span></p></body></html>"))
        self.bhistorial.setTitle(_translate("Remates JCN", "Historial de Carga"))
        self.menuMen.setTitle(_translate("Remates JCN", "Parámetros"))
        self.menuAcciones.setTitle(_translate("Remates JCN", "Impresiones"))
        self.menuEdicion.setTitle(_translate("Remates JCN", "Edición"))
        self.actionCarreras.setText(_translate("Remates JCN", "Seleccionar Carrera"))
        self.actionCaballos.setText(_translate("Remates JCN", "Caballos"))
        self.actionImprimir_remates.setText(_translate("Remates JCN", "Imprimir Remate"))
        self.actionImprimir_Carrera.setText(_translate("Remates JCN", "Imprimir Carrera"))
        self.actionImprimir_Reunion.setText(_translate("Remates JCN", "Imprimir Reunión"))
        self.actionEditar_Remate.setText(_translate("Remates JCN", "Editar Remate"))
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
        i = self.sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar()
        self.combo = QtWidgets.QComboBox(self.dlg)
        self.combo.setGeometry(60, 50, 90, 23)
        self.combo.setPlaceholderText("None")
        while(0<i):
            query = self.sess.execute("SELECT * FROM carrera WHERE id = :val", {'val' : i})
            res = query.fetchone()
            wanted = str(res['numero'])
            self.combo.addItem(wanted)
            i-=1
        self.sess.close()
        self.combo.activated[str].connect(self.seleccion)
        self.combo.activated.connect(self.dlg.close)
        self.dlg.exec_()

    def crear(self):
        self.nroCarrera = self.sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar() + 1
        self.idCarrera = self.sess.execute("SELECT COUNT(*) FROM carrera").scalar() + 1
        self.sess.execute("INSERT INTO carrera(id, idReunion, numero) VALUES (:val, :par, :var)", {'val' : self.idCarrera, 'par' : self.idReunion, 'var' : self.nroCarrera})
        self.sess.commit()
        self.sess.close()
        self.horses()
        self.xy.setText(str(self.nroCarrera))

    def seleccion(self, text):
        self.idCarrera = self.sess.execute("SELECT id FROM carrera WHERE idReunion = :val AND numero=:par", {'val' : self.idReunion, 'par' : text}).scalar()
        self.nroCarrera = int(text)
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
        i = 1
        self.idRemate = self.sess.execute("SELECT COUNT(*) FROM remate").scalar() + 1
        if(self.diezP.isChecked()):
            porc = 0.1
        if(self.veinteP.isChecked()):
            porc = 0.2
        if(self.treintaP.isChecked()):
            porc = 0.3
        self.sess.execute("INSERT INTO remate(id, idCarrera, numero, porcentaje) VALUES (:val, :par, :var, :car)", {'val' : self.idRemate, 'par' : self.idCarrera, 'var' : self.nroRemate, 'car' : porc})
        for it in self.lines:
            self.rmt = it.text()
            if(self.rmt == ""):
                self.rmt = 0
            else:
                self.rmt = int(self.rmt)
            self.idCaballo = self.sess.execute("SELECT COUNT(*) FROM caballo").scalar() + 1
            self.sess.execute("INSERT INTO caballo(id, idCarrera, idRemate, numero, monto) VALUES (:val, :par, :rem, :var, :car)", {'val' : self.idCaballo, 'par' : self.idCarrera, 'rem' : self.idRemate, 'var' : i, 'car' : self.rmt})
            i+=1
        total = self.sess.execute("SELECT SUM(monto) FROM caballo WHERE idRemate = :var", {'var' : self.idRemate}).scalar()
        self.sess.execute("UPDATE remate SET total = :tot WHERE id = :rem", {'tot' : total, 'rem' : self.idRemate})
        self.sess.commit()
        self.sess.close()
        self.lremate.setText(str(self.nroRemate + 1))

    def updRemate(self):
        self.idRemate = self.sess.execute("SELECT id FROM remate WHERE idCarrera = :car AND numero = :rem", {'car' : self.idCarrera, 'rem' : self.nroRemate}).scalar()
        if(self.diezP.isChecked()):
            porc = 0.1
        if(self.veinteP.isChecked()):
            porc = 0.2
        if(self.treintaP.isChecked()):
            porc = 0.3
        i = 1
        for it in self.lines:
            self.rmt = it.text()
            if(self.rmt == ""):
                self.rmt = 0
            else:
                self.rmt = int(self.rmt)
            self.idCaballo = self.sess.execute("SELECT id FROM caballo WHERE idRemate = :rem AND numero = :num", {'rem' : self.idRemate, 'num' : i}).scalar()
            self.sess.execute("UPDATE caballo SET monto = :mon WHERE id = :cab", {'mon' : self.rmt, 'cab' : self.idCaballo})
            i+=1
        total = self.sess.execute("SELECT SUM(monto) FROM caballo WHERE idRemate = :var", {'var' : self.idRemate}).scalar()
        self.sess.execute("UPDATE remate SET porcentaje = :por, total = :tot WHERE id = :rem", {'por' : porc, 'tot' : total, 'rem' : self.idRemate})
        msg = QtWidgets.QMessageBox.question(self, "Actualizar", "El remate ya se encuentra cargado, actualizar?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if msg == QtWidgets.QMessageBox.Yes:
            self.sess.commit()
            self.sess.close()
            self.clearAll()
            self.lremate.setText(str(self.nroRemate + 1))
        else:
            self.sess.rollback()
            self.sess.close()