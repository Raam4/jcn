from escpos.conn import SerialConnection
from escpos.impl.epson import GenericESCPOS

# connect to port 'ttyS5' @ 9600 Bps, assuming RTS/CTS for handshaking
conn = SerialConnection.create('COM1:19200,8,1,N,RTSCTS')
printer = GenericESCPOS(conn)
printer.init()
printer.set_text_size(1, 1)
printer.set_emphasized(True)
printer.text_center('DD/MM/AAA')
printer.text_left('Mesa de Remate N° 2')

printer.set_text_size(0, 0)
printer.set_emphasized(False)
printer.text_left('N° Nombre')
printer.text_right('$ Monto')

printer.text_left('Total')
printer.text_right('$ Monto')

printer.text_left('Descuentos')
printer.text_right('$ Monto')

printer.set_text_size(1, 1)
printer.set_emphasized(True)
printer.text_left('A PAGAR')
printer.text_right('$ Monto')