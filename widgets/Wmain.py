import sys
sys.path.append("./")
from PyQt5 import QtCore, QtGui, QtWidgets
import utils


class Ui_MainWindow(QtWidgets.QWidget):
    idReunion = None
    idCarrera = None
    nroCarrera = None
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Box de Carga
        self.bcarga = QtWidgets.QGroupBox(self.centralwidget)
        self.bcarga.setGeometry(QtCore.QRect(10, 10, 221, 561))
        self.bcarga.setTitle("")
        self.bcarga.setObjectName("bcarga")
        #Lineas
        self.lines = []
        i = 0
        h = 40
        while(i<16):
            self.lines.append(QtWidgets.QLineEdit(self.bcarga))
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
        while(k<16):
            self.labels.append(QtWidgets.QLabel(self.bcarga))
            self.labels[k].setFont(font)
            if(k<9):
                self.labels[k].setGeometry(QtCore.QRect(80, l, 16, 16))
            else:
                self.labels[k].setGeometry(QtCore.QRect(70, l, 22, 16))
            self.labels[k].setObjectName("c"+str(k))
            k+=1
            l+=30
        
        self.caballos = QtWidgets.QLabel(self.bcarga)
        self.caballos.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.caballos.setFont(font)
        self.caballos.setObjectName("caballos")

        self.montos = QtWidgets.QLabel(self.bcarga)
        self.montos.setGeometry(QtCore.QRect(120, 10, 71, 21))
        self.montos.setFont(font)
        self.montos.setObjectName("montos")

        #Deco
        self.line = QtWidgets.QFrame(self.bcarga)
        self.line.setGeometry(QtCore.QRect(90, 0, 20, 520))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.bcarga)
        self.line_2.setGeometry(QtCore.QRect(0, 510, 221, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        #Boton Descartar
        self.descartar = QtWidgets.QPushButton(self.bcarga)
        self.descartar.setGeometry(QtCore.QRect(0, 530, 101, 31))
        font = QtGui.QFont()
        font.setWeight(50)
        self.descartar.setFont(font)
        self.descartar.setObjectName("descartar")
        self.descartar.clicked.connect()
        #Boton Guardar
        self.guardar = QtWidgets.QPushButton(self.bcarga)
        self.guardar.setGeometry(QtCore.QRect(110, 530, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.guardar.setFont(font)
        self.guardar.setObjectName("guardar")
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
        #Action Reunion
        self.wReunion = None
        self.actionReuniones = QtWidgets.QAction(MainWindow)
        self.actionReuniones.setObjectName("actionReuniones")
        self.actionReuniones.triggered.connect(self.dialogRyC)
        #Action Carrera
        self.wCarrera = None
        self.actionCarreras = QtWidgets.QAction(MainWindow)
        self.actionCarreras.setObjectName("actionCarreras")
        self.actionCarreras.triggered.connect(self.dialogRyC)
        
        

        self.actionCaballos = QtWidgets.QAction(MainWindow)
        self.actionCaballos.setObjectName("actionCaballos")

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
        self.menuMen.addAction(self.actionReuniones)
        self.menuMen.addAction(self.actionCarreras)
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
        MainWindow.setTabOrder(self.guardar, self.descartar)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        m=0
        while(m<len(self.labels)):
            self.labels[m].setText(_translate("MainWindow", str(m+1)))
            m+=1

        self.montos.setText(_translate("MainWindow", "Montos"))
        self.caballos.setText(_translate("MainWindow", "Caballos"))  
        self.descartar.setText(_translate("MainWindow", "Descartar"))
        self.guardar.setText(_translate("MainWindow", "Guardar"))
        self.bcarrera.setTitle(_translate("MainWindow", "Carrera"))
        self.xy.setText(_translate("MainWindow", str(self.nroCarrera)))
        self.bremate.setTitle(_translate("MainWindow", "Remate "))
        self.porcentajes.setTitle(_translate("MainWindow", "Porcentaje"))
        self.diezP.setText(_translate("MainWindow", "10%"))
        self.veinteP.setText(_translate("MainWindow", "20%"))
        self.treintaP.setText(_translate("MainWindow", "30%"))
        self.bsubtotales.setTitle(_translate("MainWindow", "Subtotales"))
        self.subtotales.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Recaudado        $var</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">A Pagar        $var</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">A Rendir        $var</span></p></body></html>"))
        self.bhistorial.setTitle(_translate("MainWindow", "Historial de Carga"))
        self.menuMen.setTitle(_translate("MainWindow", "Parámetros"))
        self.menuAcciones.setTitle(_translate("MainWindow", "Impresiones"))
        self.menuEdicion.setTitle(_translate("MainWindow", "Edición"))
        self.actionReuniones.setText(_translate("MainWindow", "Seleccionar Reunión"))
        self.actionCarreras.setText(_translate("MainWindow", "Seleccionar Carrera"))
        self.actionCaballos.setText(_translate("MainWindow", "Caballos"))
        self.actionImprimir_remates.setText(_translate("MainWindow", "Imprimir Remate"))
        self.actionImprimir_Carrera.setText(_translate("MainWindow", "Imprimir Carrera"))
        self.actionImprimir_Reunion.setText(_translate("MainWindow", "Imprimir Reunión"))
        self.actionEditar_Remate.setText(_translate("MainWindow", "Editar Remate"))
        self.actionEliminar_Caballo.setText(_translate("MainWindow", "Eliminar Caballo"))
        self.actionEliminar_Carrera.setText(_translate("MainWindow", "Eliminar Carrera"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))

    #Metodos
    def closeEvent(self, event):
        close = QtWidgets.QMessageBox.question(self, "Cerrar", "¿Seguro que quiere salir?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def dialogRyC(self):
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

        sess = utils.bd()
        if(self.idReunion is None):
            self.d1.setText("Seleccionar Reunión")
            self.d2.setText("Crear Reunión")
            i = sess.execute("SELECT COUNT(*) FROM reunion").scalar()
        else:
            self.d1.setText("Seleccionar Carrera")
            self.d2.setText("Crear Carrera")
            i = sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar()
        
        self.combo = QtWidgets.QComboBox(self.dlg)
        self.combo.setGeometry(60, 50, 90, 23)
        self.combo.setPlaceholderText("None")

        while(0<i):
            if(self.idReunion is None):
                query = sess.execute("SELECT * FROM reunion WHERE id = :val", {'val' : i})
                res = query.fetchone()
                wanted = res['fecha']
            else:
                query = sess.execute("SELECT * FROM carrera WHERE id = :val", {'val' : i})
                res = query.fetchone()
                wanted = str(res['numero'])
            self.combo.addItem(wanted)
            i-=1
        sess.close()
        self.combo.activated[str].connect(self.seleccion)
        self.combo.activated.connect(self.dlg.close)
        self.dlg.exec_()

    def crear(self):
        sess = utils.bd()
        fec = datetime.date.today()
        if(self.idReunion is None):
            self.idReunion = sess.execute("SELECT COUNT(*) FROM reunion").scalar() + 1
            sess.execute("INSERT INTO reunion(id, fecha) VALUES (:val, :par)", {'val' : self.idReunion, 'par' : fec})
            sess.commit()
        else:
            self.nroCarrera = sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar() + 1
            self.idCarrera = sess.execute("SELECT COUNT(*) FROM carrera").scalar() + 1
            sess.execute("INSERT INTO carrera(id, idReunion, numero) VALUES (:val, :par, :var)", {'val' : self.idCarrera, 'par' : self.idReunion, 'var' : self.nroCarrera})
            sess.commit()
        sess.close()

    def seleccion(self, text):
        sess = utils.bd()
        if(self.idReunion is None):
            self.idReunion = sess.execute("SELECT id FROM reunion WHERE fecha=:val", {'val' : text}).scalar()
        else:
            self.idCarrera = sess.execute("SELECT id FROM carrera WHERE idReunion = :val AND numero=:par", {'val' : self.idReunion, 'par' : text}).scalar()
        sess.close()

    