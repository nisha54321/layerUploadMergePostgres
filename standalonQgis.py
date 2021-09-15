from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication , QMainWindow
from PyQt5 import QtGui, QtCore, QtWidgets

app = QgsApplication([], False)
app.setPrefixPath("/usr/share/qgis", True)
app.initQgis()
canvas = QgsMapCanvas()
canvas.setWindowTitle("Running Standalone Application")
canvas.setCanvasColor(Qt.cyan)
layer =  QgsVectorLayer('LineString?crs=epsg:4326', 'MyLine' , "memory")
pr = layer.dataProvider()
linstr = QgsFeature()

geom = QgsGeometry.fromWkt("LINESTRING(74.396668 27.626205,74.4010230000001 27.631432999,74.4024820000001 27.6326120000001,74.4029511850001 27.632939091,74.4041990000001 27.633809001,74.4058729990001 27.6349310000001,74.4087480000001 27.6380290000001,74.4083190010001 27.6386380000001,74.4074390000001 27.639284,74.407697001 27.6399490000001,74.406688 27.641127999,74.406409001 27.6418880000001,74.4093700000001 27.6420209990001,74.412367654 27.642091963,74.4173960000001 27.642211,74.431485507 27.6453753970001,74.435678001 27.6463170000001,74.4367930000001 27.6467920000001,74.4377160000001 27.6478000000001,74.4430380000001 27.6579300010001,74.4462780000001 27.6642590000001,74.4467930000001 27.6658170000001,74.4470930000001 27.667224,74.44705 27.6706060010001,74.4469191540001 27.671042157)")
linstr.setGeometry(geom)
pr.addFeatures([linstr])
layer.updateExtents()

QgsProject.instance().addMapLayer(layer)
canvas.setExtent(layer.extent())
canvas.setLayers([layer])

canvas.zoomToFullExtent()
canvas.freeze(True)
canvas.show()
canvas.refresh()
canvas.freeze(False)
canvas.repaint()


exitcode = app.exec()
QgsApplication.exitQgis()
sys.exit(exitcode)
