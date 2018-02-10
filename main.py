import sys
from PyQt4 import QtGui
import numpy as np
import cv2 as cv
import ezdxf as dxf

def gui_init():
	app = QtGui.QApplication(sys.argv)

	window = QtGui.QWidget()
	window.setGeometry(50,50,500,400)
	window.setWindowTitle("EBL Drawing")
	window.show()

	return app,window

def dxf_init(version='R2010'):
	drawing = dxf.new(dxfversion=version)

	drawing.layers.new('Layer0', dxfattribs={'color': 7})
	drawing.layers.new('Layer1', dxfattribs={'color': 150})
	drawing.layers.new('Layer2', dxfattribs={'color': 102})
	drawing.layers.new('Layer3', dxfattribs={'color': 132})
	drawing.layers.new('Layer7', dxfattribs={'color': 9})
	drawing.layers.remove('Defpoints')
	drawing.layers.remove('View port')
	modelspace = drawing.modelspace()

	return drawing,modelspace

app,window = gui_init()
dwg,msp = dxf_init()
dwg.saveas('test.dxf')

print('Done')


sys.exit(app.exec_()) #hold the window