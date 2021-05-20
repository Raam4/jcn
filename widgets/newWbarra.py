from PyQt5 import QtCore, QtGui, QtWidgets
import sys
sys.path.append("./")
import utils
import datetime


#WidgetReunion
class Wreunion(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #Atributos
    idReunion = None
    idCarrera = None

    def setupUi(self, reunionW):
        reunionW.setObjectName("reunionW")
        reunionW.setEnabled(True)
        reunionW.resize(350, 120)
        reunionW.setMinimumSize(QtCore.QSize(250, 100))
        reunionW.setMaximumSize(QtCore.QSize(350, 150))
        
        self.label = QtWidgets.QLabel(reunionW)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.line = QtWidgets.QFrame(reunionW)
        self.line.setGeometry(QtCore.QRect(160, 0, 20, 151))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.label_2 = QtWidgets.QLabel(reunionW)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        #Boton de Crear
        self.creaBtt = QtWidgets.QPushButton(reunionW)
        self.creaBtt.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.creaBtt.setObjectName("creaBtt")
        self.creaBtt.clicked.connect(self.crea)
        self.creaBtt.clicked.connect(self.clear)
        #Combo de Seleccion
        self.buscaC = self.lista()
        self.buscaC.setGeometry(QtCore.QRect(200, 60, 121, 20))
        self.buscaC.activated[str].connect(self.seleccion)
        self.buscaC.activated.connect(self.clear)
        
        self.retranslateUi(reunionW)
        QtCore.QMetaObject.connectSlotsByName(reunionW)

    def retranslateUi(self, reunionW):
        _translate = QtCore.QCoreApplication.translate
        reunionW.setWindowTitle(_translate("reunionW", "Form"))
        self.creaBtt.setText(_translate("reunionW", "Crear"))
        if (self.idReunion == None):
            self.label.setText(_translate("reunionW", "Crear Nueva Reunion"))
            self.label_2.setText(_translate("reunionW", "Seleccionar Reunion"))
        else:
            self.label.setText(_translate("carreraW", "Crear Nueva Carrera"))
            self.label_2.setText(_translate("carreraW", "Abrir Carrera Existente"))

    def crea(self):
        sess = utils.bd()
        if(self.idReunion==None):
            nrnn = sess.execute("SELECT COUNT(*) FROM reunion").scalar() + 1
            fec = datetime.date.today()
            sess.execute("INSERT INTO reunion(id, fecha) VALUES (:val, :par)", {'val' : nrnn, 'par' : fec})
            self.idReunion = nrnn
        else:
            ncrr = sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar() + 1
            self.idCarrera = sess.execute("SELECT COUNT(*) FROM carrera").scalar() + 1
            sess.execute("INSERT INTO carrera(id, idReunion, numero) VALUES (:val, :par, :var)", {'val' : self.idCarrera, 'par' : self.idReunion, 'var' : ncrr})
        sess.commit()
        sess.close()

    def lista(self):
        sess = utils.bd()
        if(self.idReunion==None):
            i = sess.execute("SELECT COUNT(*) FROM reunion").scalar()
        else:
            i = sess.execute("SELECT COUNT(*) FROM carrera WHERE idReunion = :val", {'val' : self.idReunion}).scalar()
        combo = QtWidgets.QComboBox(self)
        combo.setPlaceholderText("None")
        while(0<i):
            if(self.idReunion==None):
                query = sess.execute("SELECT * FROM reunion WHERE id = :val", {'val' : i})
                query = query.fetchone()
                item = query['fecha']
            else:
                query = sess.execute("SELECT * FROM carrera WHERE id = :val", {'val' : i})
                query = query.fetchone()
                item = query['numero']
            combo.addItem(item)
            i-=1
        sess.close()
        return combo

    def seleccion(self, text):
        sess = utils.bd()
        if(self.idReunion==None):
            self.idReunion = sess.execute("SELECT id FROM reunion WHERE fecha=:val", {'val' : text}).scalar()
        else:
            self.idCarrera = sess.execute("SELECT id FROM carrera WHERE idReunion = :val AND numero=:par", {'val' : self.idReunion, 'par' : text}).scalar()
        sess.close()

