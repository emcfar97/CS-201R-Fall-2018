from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QTableView, QLabel, QLabel, QFormLayout, QLineEdit, QRadioButton, QComboBox, QMessageBox, QDesktopWidget, QStatusBar
from PyQt5.QtCore import Qt, QTimer, QSize, QUrl
from PyQt5.QtGui import QImage, QPixmap, QMovie

from datetime import date
from cv2 import VideoCapture
import mysql.connector as sql

DATAB = sql.connect(
    user='root', password='SchooL1@', database='userData', 
    host='192.168.1.43' if __file__.startswith(('e:\\', 'e:/')) else '127.0.0.1'
    )
CURSOR = DATAB.cursor(buffered=True)
BASE = 'SELECT path, tags, artist, stars, rating, type FROM imageData'
UPDATE = f'UPDATE imageData SET date_used="{date.today()}" WHERE path=%s'
MODIFY = 'UPDATE imageData SET {} WHERE path=%s'
DELETE = 'DELETE FROM imageData WHERE path=%s'
NEZUMI = r'C:\Program Files (x86)\Lazy Nezumi Pro\LazyNezumiPro.exe'

if __file__.startswith(('e:\\','e:/')):

    BASE = BASE.replace('path','REPLACE(path, "C:", "E:")')
    UPDATE = UPDATE.replace('%s', "REPLACE(%s, 'E:', 'C:')")
    MODIFY = MODIFY.replace('%s', "REPLACE(%s, 'E:', 'C:')")
    DELETE = DELETE.replace('%s', "REPLACE(%s, 'E:', 'C:')")