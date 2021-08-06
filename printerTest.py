from escpos.conn import SerialConnection
from escpos.impl.epson import GenericESCPOS, TMT20

# connect to port 'ttyS5' @ 9600 Bps, assuming RTS/CTS for handshaking
conn = SerialConnection.create('COM3:9600,8,1,N')
printer = GenericESCPOS(conn)
printer.init()
printer.textout("Hello World!")