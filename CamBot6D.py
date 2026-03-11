################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################


import multiprocessing
from multiprocessing import Process, Queue

from configparser import ConfigParser
import paho.mqtt.client as mqtt
import os

import pyttsx3
# GUI FILE
if __name__ != "__mp_main__":
    import sys
    import platform
    from scipy import interpolate
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent, Slot, Signal)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
    from PySide2.QtWidgets import *
    import time
    from threading import Thread
    from app_modules import *
    import numpy as np
    import win32api
    import win32con
    import win32gui
    import win32com.client

    import mmap
    from dataclasses import dataclass
    import struct

    import math
    import socket as _socket
    import select as _select
    import secrets as _secrets
    import subprocess
    import cambot_protocol

    try:
        import pyi_splash
    except:
        print ('dev mode')


try:
    # Update the text on the splash screen
    pyi_splash.update_text("Opening GUI")
    # Close the splash screen. It does not matter when the call
    # to this function is made, the splash screen remains open until
    # this function is called or the Python program is terminated.
except:
    print ('dev mode')




###

mqtt_thread = None

engine = pyttsx3.init() # object creation


#DEFAULTS
voice = ''
voice_id = ''
rate = 200
volume = 0.75
hotkey_enable = False
voice_enable = False
mqtt_enable = False
mqtt_ip = ''
mqtt_ip_default = '127.0.0.1'
mqtt_port = ''
mqtt_port_default = '1883'
mqtt_user = ''
mqtt_pass = ''
opentrack_ip = ''
opentrack_port = ''
dualpc_role = 0          # 0=disabled, 1=Gaming PC, 2=Controller PC
dualpc_port = 4343
dualpc_derived_key = b''
dualpc_key_salt = b''
dualpc_running = False
dualpc_seq = 0
#

path_time = 3.0
path_ease_selection = 1
spatial_selection = 1
temporal_selection = 0
point_time = 1.0
point_ease_selection = 0

#

joystick_value = None
joystickNames = []
joystickIds = []
joystickUids = []
controller_id = False
controller_name = False
controllers_count = 0

#
tts = ''
ttsQ = ''
all_processes = []

q = Queue()

###

#config file
config = ConfigParser()

controllerTest = False
controller_test = ''

voices = []



#opentrack
x = 0
y = 0
z = 0
yaw = 0
pitch = 0
roll = 0



#camera bot
path_x = [] #[left .. right]
path_y = [] #[down .. up]
path_z = [] #[backwards .. forwards]
path_yaw = [] #[-180 .. 180]
path_pitch = [] #[-180 .. 180]
path_roll = [] #[-180 .. 180]

joystickIds = ()
joystickUids = ()
joystickNames = ()


controller = "keyboardandmouse"
joystick_loop = True
#keyboard
keyboard_motion = 1
keyboard_wrap_rotation = True
keyboard_invert_pitch = False
keyboard_invert_yaw = False
keyboard_invert_roll = False
#spacemouse
joystick = None
spacemouse_motion = 1
spacemouse_wrap_rotation = True
spacemouse_invert_pitch = True
spacemouse_invert_yaw = False
spacemouse_invert_roll = False
#xboxone
gamepad = None
xboxone_motion = 1
xboxone_wrap_rotation = True
xboxone_invert_pitch = True
xboxone_invert_yaw = False
xboxone_invert_roll = False

#mqtt
client = mqtt.Client("P1") #create new instance

os.chdir(os.path.dirname(os.path.abspath(__file__)))

display = 0 #display for camera control window
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"


#pygame.display.set_mode((400, 400), flags=pygame.HIDDEN | pygame.NOFRAME, display=display)


#to change the display, call quit first and set again
#pygame.display.quit()
#pygame.display.set_mode((640, 640), flags=pygame.HIDDEN, display=0)

def CSS_buttonActive(icon):
    return(u"QPushButton {\n"
           "	border: 2px solid rgb(255, 255, 255);\n"
           "	border-radius: 5px;	\n"
           "	background-color: rgb(85, 170, 255);\n"
           "	background-image: url("+icon+");\n"
           "}")
def CSS_button(icon):
    return(u"QPushButton {\n"
           "	border: 2px solid rgb(52, 59, 72);\n"
           "	border-radius: 5px;	\n"
           "	background-color: rgb(52, 59, 72);\n"
           "	background-image: url("+icon+");\n"
           "}\n"
           "QPushButton:hover {\n"
           "	background-color: rgb(57, 65, 80);\n"
           "	border: 2px solid rgb(61, 70, 86);\n"
           "}\n"
           "QPushButton:pressed {	\n"
           "	background-color: rgb(35, 40, 49);\n"
           "	border: 2px solid rgb(43, 50, 61);\n"
           "}")

def wraparound(old, new):
    old_btm = round(old/2-0.25) #required for wrap around of nipple (with negative buffer)
    old_top = round(old/2+0.25) #required for wrap around of nipple (with positive buffer)

    if (old > 0 and new * old < 0) or (old < 0 and new * old >= 0): #if different signs (and not zero) for positive, or same signe (or zero) if negative
        return new + old_top * 2 #add the floor * 2
    else:
        return new + old_btm * 2 #add the floor * 2

def increment(old, new):

    return old + new

if __name__ != "__mp_main__":
    def _check_firewall_block():
        """Return True if a Windows Firewall inbound Block rule targets python or CamBot."""
        try:
            ps = (
                '(Get-NetFirewallRule -Direction Inbound -Action Block -Enabled True |'
                ' Get-NetFirewallApplicationFilter |'
                ' Where-Object { $_.Program -like "*python*" -or $_.Program -like "*CamBot*" }).Count'
            )
            result = subprocess.run(
                ['powershell', '-NoProfile', '-NonInteractive', '-Command', ps],
                capture_output=True, text=True, timeout=8)
            return int(result.stdout.strip() or '0') > 0
        except Exception:
            return False

    class MainWindow(QMainWindow):

        # Signals for thread-safe cross-thread calls (from UDP threads → Qt main thread)
        dualpc_status_signal = Signal(str, str, str)   # text, color, tooltip
        dualpc_bind_error_signal = Signal()
        dualpc_firewall_warning_signal = Signal()

        def __init__(self):

            global mqtt_ip
            global mqtt_port
            global mqtt_user
            global mqtt_pass

            global path_time
            global path_ease_selection
            global spatial_selection
            global temporal_selection
            global point_ease_selection
            global point_time

            global opentrack_ip
            global opentrack_port
            global voice_enable
            global joystick_value

            global keyboard_motion
            global keyboard_wrap_rotation
            global keyboard_invert_pitch
            global keyboard_invert_yaw
            global keyboard_invert_roll
            global spacemouse_motion
            global spacemouse_wrap_rotation
            global spacemouse_invert_pitch
            global spacemouse_invert_yaw
            global spacemouse_invert_roll
            global xboxone_motion
            global xboxone_wrap_rotation
            global xboxone_invert_pitch
            global xboxone_invert_yaw
            global xboxone_invert_roll



            # Close the splash screen. It does not matter when the call
            # to this function is made, the splash screen remains open until
            # this function is called or the Python program is terminated.
            try:
                pyi_splash.close()
            except:
                print ('dev mode')


            #global send_to_opentrack
            #send_to_opentrack = Thread(target=self.send_to_opentrack_thread, args=("Thread",))
            #send_to_opentrack.start()


            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            F = Functions(self, UIFunctions, self.ui, pygame)
            self.F = F

            joystick_value = Thread(target=self.joystick_thread)
            joystick_value.start()


            self.mqtt_flag = None
            self.mqtt_connected = False

            self.ui.controllerSelection.addItem("")
            self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select a device)", None))
            self.ui.controllerSelection.addItem("")
            self.ui.controllerSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard Keyboard and mouse HID", None))
            self.ui.controllerSelection.setCurrentIndex(1)
            self.ui.controllerSelection.currentIndexChanged.connect(self.on_controllerSelection_changed)

            self.ui.controllerUpdateButton.clicked.connect(self.on_controllerUpdate_clicked)

            #self.ui.pushButton.setText(QCoreApplication.translate("MainWindow", u"test", None))




            self.ui.controllerTestButton.clicked.connect(self.on_test_clicked)


            ##
            n = 0
            for voiceChoice in voices:
                self.ui.voiceSelection.addItem("")
                print(voiceChoice)
                self.ui.voiceSelection.setItemText(n, QCoreApplication.translate("MainWindow", voiceChoice.name, None))
                n = n+1

            if voice:
                n = 0
                for thisvoice in voices:
                    if thisvoice.id == voice:
                        self.ui.voiceSelection.setCurrentIndex(n)
                    n = n+1

            self.ui.voiceSelection.currentIndexChanged.connect(self.on_voiceSelection_changed)
            ##

            self.ui.hotkeyCheckBox.stateChanged.connect(self.on_hotkeyEnable_changed)
            self.ui.hotkeyCheckBox.setChecked(hotkey_enable)
            self.ui.voiceCheckBox.stateChanged.connect(self.on_voiceEnable_changed)
            self.ui.voiceCheckBox.setChecked(voice_enable)
            self.ui.MQTTCheckBox.stateChanged.connect(self.on_mqttEnable_changed)
            self.ui.MQTTCheckBox.setChecked(mqtt_enable)

            self.ui.xBoxButton.clicked.connect(self.on_xBoxButton_clicked)
            self.ui.spaceMouseButton.clicked.connect(self.on_spaceMouseButton_clicked)
            self.ui.keyboardAndMouseButton.clicked.connect(self.on_keyboardAndMouseButton_clicked)

            self.ui.motionSelection.currentIndexChanged.connect(self.on_motionSelection_changed)
            self.ui.wrapRotationCheckBox.stateChanged.connect(self.on_wrapRotationCheckBox_changed)
            self.ui.invertRollCheckBox.stateChanged.connect(self.on_invertRollCheckBox_changed)
            self.ui.invertPitchCheckBox.stateChanged.connect(self.on_invertPitchCheckBox_changed)
            self.ui.invertYawCheckBox.stateChanged.connect(self.on_invertYawCheckBox_changed)

            match controller:
                case "xboxone":
                    self.ui.xBoxButton.click()
                case "spacemouse":
                    self.ui.spaceMouseButton.click()
                case "keyboardandmouse":
                    self.ui.keyboardAndMouseButton.click()

            #camera dropdowns
            self.ui.easeSelection.setCurrentIndex(path_ease_selection)
            self.ui.easeSelection.currentIndexChanged.connect(self.on_easeSelection_changed)
            self.ui.skipEaseSelection.setCurrentIndex(point_ease_selection)
            self.ui.skipEaseSelection.currentIndexChanged.connect(self.on_skipEaseSelection_changed)
            self.ui.spatialInterpolationSelection.setCurrentIndex(spatial_selection)
            self.ui.spatialInterpolationSelection.currentIndexChanged.connect(self.on_spatialInterpolationSelection_changed)
            self.ui.temporalInterpolationSelection.setCurrentIndex(temporal_selection)
            self.ui.temporalInterpolationSelection.currentIndexChanged.connect(self.on_temporalInterpolationSelection_changed)

            ## PRINT ==> SYSTEM
            print('System: ' + platform.system())
            print('Version: ' + platform.release())

            ########################################################################
            ## START - WINDOW ATTRIBUTES
            ########################################################################

            ## REMOVE ==> STANDARD TITLE BAR
            UIFunctions.removeTitleBar(True)
            ## ==> END ##

            ## SET ==> WINDOW TITLE
            self.setWindowTitle('CamBot 6D')
            self.setWindowIcon(QIcon('images/icon.png'))
            UIFunctions.labelTitle(self, 'CamBot 6D')
            UIFunctions.labelDescription(self, 'six degrees of freedom spline interpolation with opentrack UDP-over-network output')
            ## ==> END ##

            ## WINDOW SIZE ==> DEFAULT SIZE
            startSize = QSize(800, 600)
            self.resize(startSize)
            self.setMinimumSize(startSize)
            UIFunctions.enableMaximumSize(self, 800, 600)
            ## ==> END ##

            ## ==> CREATE MENUS
            ########################################################################

            ## ==> TOGGLE MENU SIZE
            self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
            ## ==> END ##

            ## ==> ADD CUSTOM MENUS
            self.ui.stackedWidget.setMinimumWidth(20)
            UIFunctions.addNewMenu(self, "CAMERA", "btn_main", "url(:/20x20/icons/20x20/cil-video.png)", True)
            UIFunctions.addNewMenu(self, "CONTROLLERS", "btn_controllers", "url(:/20x20/icons/20x20/cil-gamepad.png)", True)
            UIFunctions.addNewMenu(self, "INFO", "btn_info", "url(:/20x20/icons/20x20/cil-description.png)", True)
            UIFunctions.addNewMenu(self, "SETTINGS", "btn_settings", "url(:/20x20/icons/20x20/cil-equalizer.png)", False)
            ## ==> END ##

            # START MENU => SELECTION
            UIFunctions.selectStandardMenu(self, "btn_main")
            ## ==> END ##

            ## ==> START PAGE
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
            ## ==> END ##

            ## USER ICON ==> SHOW HIDE
            UIFunctions.userIcon(self, "WM", "", False)
            ## ==> END ##

            ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
            ########################################################################
            def moveWindow(event):
                # IF MAXIMIZED CHANGE TO NORMAL
                if UIFunctions.returStatus() == 1:
                    UIFunctions.maximize_restore(self)

                # MOVE WINDOW
                if event.buttons() == Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.dragPos)
                    self.dragPos = event.globalPos()
                    event.accept()

            # WIDGET TO MOVE
            self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
            ## ==> END ##

            ## ==> LOAD DEFINITIONS
            ########################################################################
            UIFunctions.uiDefinitions(self)
            ## ==> END ##

            ########################################################################
            ## END - WINDOW ATTRIBUTES
            ############################## ---/--/--- ##############################




            ########################################################################
            #                                                                      #
            ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
            #                                                                      #
            ## ==> USER CODES BELLOW                                              ##
            ########################################################################


            ## ==> QTableWidget RARAMETERS
            ########################################################################
            self.ui.tableWidget_waypoints.hide()
            self.ui.frame_div_table_widget_M1.setMaximumSize(16777215, 50)
            self.ui.tableWidget_waypoints.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            self.ui.tableWidget_waypoints.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            self.ui.tableWidget_waypoints.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            self.ui.tableWidget_waypoints.setColumnWidth(0, QtWidgets.QHeaderView.Stretch)
            self.ui.tableWidget_waypoints.setColumnWidth(1, 120)
            self.ui.tableWidget_waypoints.setColumnWidth(2, 50)
            delegate = AlignDelegate(self.ui.tableWidget_waypoints)
            self.ui.tableWidget_waypoints.setItemDelegateForColumn(1, delegate)
            self.ui.tableWidget_waypoints.setItemDelegateForColumn(2, delegate)
            ## ==> END ##

            ## ==> DELETE ALL WAYPOINTS
            self.ui.pushButton_delete_all.clicked.connect(lambda: F.deleteAll(q, config))

            ## ==> play sample voice line
            self.ui.voiceTestButton.clicked.connect(lambda: q.put('This is a test of the CamBot 6D audio feedback system.'))

            self.ui.remoteIPEdit.setText(QCoreApplication.translate("MainWindow", str(opentrack_ip), None))
            self.ui.remoteIPEdit.textChanged.connect(self.opentrack_ip_changed)

            self.ui.opentrackPortEdit.setText(QCoreApplication.translate("MainWindow", str(opentrack_port), None))
            self.ui.opentrackPortEdit.textChanged.connect(self.opentrack_port_changed)

            self.ui.dualPCPasswordEdit.editingFinished.connect(self.on_dualpc_password_set)

            self.ui.remoteSelection.setCurrentIndex(dualpc_role)
            self.ui.remoteSelection.currentIndexChanged.connect(self.on_remoteSelection_changed)

            # Wire dual-PC signals (thread-safe cross-thread calls)
            self.dualpc_status_signal.connect(self._dualpc_update_status)
            self.dualpc_bind_error_signal.connect(self._dualpc_host_bind_error)
            self.dualpc_firewall_warning_signal.connect(self._show_firewall_warning)

            # Auto-start dual-PC mode if configured
            if dualpc_role == 1 and dualpc_derived_key:
                self.start_dualpc_host()
            elif dualpc_role == 2 and dualpc_derived_key:
                self.start_dualpc_controller()

            hostname = socket.gethostname()
            local_ip = socket.gethostbyname(hostname)
            self.ui.label_ip_info.setText(QCoreApplication.translate("MainWindow", str(local_ip), None))

            self.ui.MQTTIPEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_ip), None))
            self.ui.MQTTIPEdit.textChanged.connect(self.mqtt_ip_changed)

            self.ui.MQTTPortEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_port), None))
            self.ui.MQTTPortEdit.textChanged.connect(self.mqtt_port_changed)

            self.ui.MQTTUserEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_user), None))
            self.ui.MQTTUserEdit.textChanged.connect(self.mqtt_user_changed)

            self.ui.MQTTPassEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_pass), None))
            self.ui.MQTTPassEdit.textChanged.connect(self.mqtt_pass_changed)

            self.ui.MQTTTestButton.clicked.connect(self.start_mqtt)

            self.ui.pathtimeEdit.setValue(path_time)
            self.ui.pathtimeEdit.valueChanged.connect(self.path_time_changed)

            self.ui.skiptimeEdit.setValue(point_time)
            self.ui.skiptimeEdit.valueChanged.connect(self.skip_time_changed)


            self.ui.pushButton_forward.clicked.connect(lambda: self.goForward(q, config))
            self.ui.pushButton_backward.clicked.connect(lambda: F.pathBackward(q, config))
            self.ui.pushButton_next.clicked.connect(lambda: F.skipToNext(q, config))
            self.ui.pushButton_prev.clicked.connect(lambda: F.skipToPrev(q, config))




            ## ==> ADD NEW WAYPOINT
            self.ui.pushButton_add_waypoint.clicked.connect(lambda: F.newWaypoint(q, config))

            ## ==> GO HOME
            self.ui.pushButton_home.clicked.connect(lambda: F.goHome(q, config))

            ## ==> QTableWidget RARAMETERS
            ########################################################################
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            ## ==> END ##



            ########################################################################
            #                                                                      #
            ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
            #                                                                      #
            ############################## ---/--/--- ##############################

            self.show()

        def showForeground(self):
            self.F.showForeground()

        def goForward(self, q, config):
            self.F.pathForward(q, config)

        def goBackward(self, q, config):
            self.F.pathBackward(q, config)

        def opentrack_ip_changed(self, text):
            global opentrack_ip
            config.set('dualpc', 'ip', str(text))
            self.write_config()
            opentrack_ip = text

        def opentrack_port_changed(self, text):
            global opentrack_port
            config.set('dualpc', 'port', str(text))
            self.write_config()
            opentrack_port = text


        def mqtt_ip_changed(self, text):
            global mqtt_ip
            config.set('mqtt', 'ip', str(text))
            self.write_config()
            mqtt_ip = text

        def mqtt_port_changed(self, text):
            global mqtt_port
            config.set('mqtt', 'port', str(text))
            self.write_config()
            mqtt_port = text

        def mqtt_user_changed(self, text):
            global mqtt_user
            config.set('mqtt', 'user', str(text))
            self.write_config()
            mqtt_user = text

        def mqtt_pass_changed(self, text):
            global mqtt_pass
            config.set('mqtt', 'pass', str(text))
            self.write_config()
            mqtt_pass = text


        def path_time_changed(self, double):
            global path_time
            config.set('speed', 'path', str(double))
            self.write_config()
            path_time = double

        def skip_time_changed(self, double):
            global point_time
            config.set('speed', 'point', str(double))
            self.write_config()
            point_time = double

        def write_config(self):
            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def stop_controller_test(self):
            global controller_test
            global controllerTest
            controllerTest = False
            if controller_test and controller_test.is_alive():
                controller_test.join()

            x_test = self.ui.tableWidget.item(0, 0)
            x_test.setText(QCoreApplication.translate("MainWindow", "", None))
            y_test = self.ui.tableWidget.item(0, 1)
            y_test.setText(QCoreApplication.translate("MainWindow", "", None))
            z_test = self.ui.tableWidget.item(0, 2)
            z_test.setText(QCoreApplication.translate("MainWindow", "", None))
            yaw_test = self.ui.tableWidget.item(0, 3)
            yaw_test.setText(QCoreApplication.translate("MainWindow", "", None))
            pitch_test = self.ui.tableWidget.item(0, 4)
            pitch_test.setText(QCoreApplication.translate("MainWindow", "", None))
            roll_test = self.ui.tableWidget.item(0, 5)
            roll_test.setText(QCoreApplication.translate("MainWindow", "", None))

            stop_icon = QIcon()
            stop_icon.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.controllerTestButton.setIcon(stop_icon)
            self.ui.controllerTestButton.setText(QCoreApplication.translate("MainWindow", u" TEST", None))
            self.ui.controllerTestButton.setStyleSheet(u"QPushButton {\n"
            "	margin-left: 5px;\n"
            "	border: 2px solid rgb(52, 59, 72);\n"
            "	border-radius: 5px;	\n"
            "	background-color: rgb(52, 59, 72);\n"
            "}\n"
            "QPushButton:hover {\n"
            "	background-color: rgb(57, 65, 80);\n"
            "	border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "QPushButton:pressed {	\n"
            "	background-color: rgb(35, 40, 49);\n"
            "	border: 2px solid rgb(43, 50, 61);\n"
            "}")



        def controller_test_thread(self, threadname):
            global x
            global y
            global z
            global yaw
            global pitch
            global roll
            global controllerTest

            x_snap = x
            y_snap = y
            z_snap = z
            yaw_snap = yaw
            pitch_snap = pitch
            roll_snap = roll

            while controllerTest:
                #print(x,y,z,yaw,pitch,roll)
                time.sleep(0.02) #50 fps (ish)
                x_test = self.ui.tableWidget.item(0, 0)
                x_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                x_test.setText(QCoreApplication.translate("MainWindow", str(round((x-x_snap)*-1000)), None))
                y_test = self.ui.tableWidget.item(0, 1)
                y_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                y_test.setText(QCoreApplication.translate("MainWindow", str(round((y-y_snap)*1000)), None))
                z_test = self.ui.tableWidget.item(0, 2)
                z_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                z_test.setText(QCoreApplication.translate("MainWindow", str(round((z-z_snap)*-1000)), None))
                yaw_test = self.ui.tableWidget.item(0, 3)
                yaw_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                yaw_test.setText(QCoreApplication.translate("MainWindow", str(round((yaw-yaw_snap)*1000)), None))
                pitch_test = self.ui.tableWidget.item(0, 4)
                pitch_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                pitch_test.setText(QCoreApplication.translate("MainWindow", str(round((pitch-pitch_snap)*-1000)), None))
                roll_test = self.ui.tableWidget.item(0, 5)
                roll_test.setTextAlignment(Qt.AlignCenter | Qt.AlignVCenter)
                roll_test.setText(QCoreApplication.translate("MainWindow", str(round((roll-roll_snap)*-1000)), None))

        def on_test_clicked(self):

            global controllerTest
            global controller_test

            if not controllerTest:
                controllerTest = True
                controller_test = Thread(target=self.controller_test_thread, args=("Thread",))
                controller_test.start()
                stop_icon = QIcon()
                stop_icon.addFile(u":/16x16/icons/16x16/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.controllerTestButton.setIcon(stop_icon)
                self.ui.controllerTestButton.setText(QCoreApplication.translate("MainWindow", u" Stop", None))
                self.ui.controllerTestButton.setStyleSheet(u"QPushButton {\n"
                "	margin-left: 5px;\n"
                "	border: 2px solid rgb(124, 29, 0);\n"
                "	border-radius: 5px;	\n"
                "	background-color: rgb(124, 29, 0);\n"
                "}\n"
                "QPushButton:hover {\n"
                "	background-color: rgb(137, 32, 0);\n"
                "	border: 2px solid rgb(147, 33, 0);\n"
                "}\n"
                "QPushButton:pressed {	\n"
                "	background-color: rgb(84, 19, 0);\n"
                "	border: 2px solid rgb(104, 20, 0);\n"
                "}")
            else:
                self.stop_controller_test()

        def repopulate_controllers_dropdown(self):
            global controller
            global joystickNames
            global joystickUids
            global controller_id
            global controller_name
            global joystickNames
            global joystickUids
            global joystickIds

            joystickNames = [pygame.joystick.Joystick(x).get_name() for x in range(pygame.joystick.get_count())]
            joystickIds = [pygame.joystick.Joystick(x).get_instance_id() for x in range(pygame.joystick.get_count())]
            joystickUids = [pygame.joystick.Joystick(x).get_guid() for x in range(pygame.joystick.get_count())]

            print(joystickIds, pygame.joystick.get_count())

            controller_id = False
            controller_name = False
            controller_found = -1

            if controller == "xboxone":
                if config.has_option('controllers', 'xboxone_id'):
                    controller_id = config.get('controllers', 'xboxone_id')
                if config.has_option('controllers', 'xboxone_name'):
                    controller_name = config.get('controllers', 'xboxone_name')
                self.ui.controllerSelection.clear()
                self.ui.controllerSelection.addItem("")
                self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select your Xbox gamepad)", None))
            elif controller == "spacemouse":
                if config.has_option('controllers', 'spacemouse_id'):
                    controller_id = config.get('controllers', 'spacemouse_id')
                if config.has_option('controllers', 'spacemouse_name'):
                    controller_name = config.get('controllers', 'spacemouse_name')
                self.ui.controllerSelection.clear()
                self.ui.controllerSelection.addItem("")
                self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select your SpaceMouse)", None))
            else:
                self.ui.controllerSelection.clear()
                self.ui.controllerSelection.addItem("")
                self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select a device)", None))
                self.ui.controllerSelection.addItem("")
                self.ui.controllerSelection.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard Keyboard and mouse HID", None))
                self.ui.controllerSelection.setCurrentIndex(1)

            print("ID", controller_id)

            if controller == "xboxone" or controller == "spacemouse":
                n = 0
                for x in joystickIds:
                    self.ui.controllerSelection.addItem("")
                    self.ui.controllerSelection.setItemText(n+1, QCoreApplication.translate("MainWindow", joystickNames[n], None))
                    print(joystickUids[n])
                    if controller_id == joystickUids[n]:
                        controller_found = n
                    n = n+1

                print("FOUND", controller_found)

                if controller_found >= 0:
                    print("SETTING TO", controller_found+1)
                    self.ui.controllerSelection.setCurrentIndex(controller_found+1)
                elif controller_id:
                    self.ui.controllerSelection.addItem("")
                    if controller_name:
                        self.ui.controllerSelection.setItemText(n+1, QCoreApplication.translate("MainWindow", controller_name + u" [disconnected]", None))
                    else:
                        self.ui.controllerSelection.setItemText(n+1, QCoreApplication.translate("MainWindow", u"UNKNOWN [disconnected]", None))
                    self.ui.controllerSelection.setCurrentIndex(n+1)
                else:
                    self.ui.controllerSelection.setCurrentIndex(0)


        def on_xBoxButton_clicked(self):
            global controller
            self.stop_controller_test()
            #self.joystick_reinit()

            controller = "xboxone"
            config.set('controllers', 'type', 'xboxone')

            self.ui.motionSelection.setCurrentIndex(xboxone_motion)
            self.on_motionSelection_changed(xboxone_motion)

            self.ui.wrapRotationCheckBox.setChecked(xboxone_wrap_rotation)
            self.ui.invertRollCheckBox.setChecked(xboxone_invert_roll)
            self.ui.invertPitchCheckBox.setChecked(xboxone_invert_pitch)
            self.ui.invertYawCheckBox.setChecked(xboxone_invert_yaw)
            self.on_wrapRotationCheckBox_changed(xboxone_wrap_rotation)
            self.on_invertRollCheckBox_changed(xboxone_invert_roll)
            self.on_invertPitchCheckBox_changed(xboxone_invert_pitch)
            self.on_invertYawCheckBox_changed(xboxone_invert_yaw)

            self.repopulate_controllers_dropdown()

            self.ui.labelStreamDeck.setVisible(False)
            self.ui.tableWidget.setVisible(True)
            self.ui.controllerTestButton.setVisible(True)
            self.ui.controllerTestButton.setEnabled(True)
            self.ui.keyMapImage.setStyleSheet(u"QPushButton {\n"
            "	background-color: rgb(41, 46, 57);\n"
            "	border-radius: 0px;	\n"
            "	background-image: url(images/xbox-map.png);\n"
            "}")


            self.ui.xBoxButton.setStyleSheet(CSS_buttonActive("images/controllers-02.png"))
            self.ui.keyboardAndMouseButton.setStyleSheet(CSS_button("images/controllers-04.png"))
            self.ui.spaceMouseButton.setStyleSheet(CSS_button("images/controllers-01.png"))
            self.ui.label_controller_info.setText(QCoreApplication.translate("MainWindow", u"CamBot 6D is compatible with Microsoft Xbox Series X, Xbox Series S, and Xbox One gamepads.\n\nNote: Works in fullscreen mode. Can only support 5 analog axis, roll is controlled digitally. Make sure the particular controller has no keybindings set in Star Citizen.", None))
            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_keyboardAndMouseButton_clicked(self):
            global controller
            self.stop_controller_test()

            controller = "keyboardandmouse"
            config.set('controllers', 'type', 'keyboardandmouse')

            self.ui.motionSelection.setCurrentIndex(keyboard_motion)
            self.on_motionSelection_changed(keyboard_motion)

            self.ui.wrapRotationCheckBox.setChecked(keyboard_wrap_rotation)
            self.ui.invertRollCheckBox.setChecked(keyboard_invert_roll)
            self.ui.invertPitchCheckBox.setChecked(keyboard_invert_pitch)
            self.ui.invertYawCheckBox.setChecked(keyboard_invert_yaw)
            self.on_wrapRotationCheckBox_changed(keyboard_wrap_rotation)
            self.on_invertRollCheckBox_changed(keyboard_invert_roll)
            self.on_invertPitchCheckBox_changed(keyboard_invert_pitch)
            self.on_invertYawCheckBox_changed(keyboard_invert_yaw)

            self.repopulate_controllers_dropdown()

            self.ui.labelStreamDeck.setVisible(True)
            self.ui.tableWidget.setVisible(False)
            self.ui.controllerTestButton.setVisible(False)
            self.ui.controllerTestButton.setEnabled(False)
            self.ui.keyMapImage.setStyleSheet(u"QPushButton {\n"
            "	background-color: rgb(41, 46, 57);\n"
            "	border-radius: 0px;	\n"
            "	background-image: url(images/keyboard-map.png);\n"
            "}")

            self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select your controller)", None))
            self.ui.xBoxButton.setStyleSheet(CSS_button("images/controllers-02.png"))
            self.ui.keyboardAndMouseButton.setStyleSheet(CSS_buttonActive("images/controllers-04.png"))
            self.ui.spaceMouseButton.setStyleSheet(CSS_button("images/controllers-01.png"))
            self.ui.label_controller_info.setText(QCoreApplication.translate("MainWindow", u"CamBot 6D is compatible with any regular keyboard and mouse.\n\nNote: Does not work in fullscreen mode. Will display an overlay window that captures all mouse and keyboard input while setting waypoints. Can be activated via graphical user interface or Stream Deck MQTT remote.", None))
            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_spaceMouseButton_clicked(self):
            global controller
            self.stop_controller_test()
            #self.joystick_reinit()

            controller = "spacemouse"
            config.set('controllers', 'type', 'spacemouse')

            self.ui.motionSelection.setCurrentIndex(spacemouse_motion)
            self.on_motionSelection_changed(spacemouse_motion)

            self.ui.wrapRotationCheckBox.setChecked(spacemouse_wrap_rotation)
            self.ui.invertRollCheckBox.setChecked(spacemouse_invert_roll)
            self.ui.invertPitchCheckBox.setChecked(spacemouse_invert_pitch)
            self.ui.invertYawCheckBox.setChecked(spacemouse_invert_yaw)
            self.on_wrapRotationCheckBox_changed(spacemouse_wrap_rotation)
            self.on_invertRollCheckBox_changed(spacemouse_invert_roll)
            self.on_invertPitchCheckBox_changed(spacemouse_invert_pitch)
            self.on_invertYawCheckBox_changed(spacemouse_invert_yaw)

            self.repopulate_controllers_dropdown()

            self.ui.labelStreamDeck.setVisible(False)
            self.ui.tableWidget.setVisible(True)
            self.ui.controllerTestButton.setVisible(True)
            self.ui.controllerTestButton.setEnabled(True)
            self.ui.keyMapImage.setStyleSheet(u"QPushButton {\n"
            "	background-color: rgb(41, 46, 57);\n"
            "	border-radius: 0px;	\n"
            "	background-image: url(images/spacemouse-map.png);\n"
            "}")

            self.ui.xBoxButton.setStyleSheet(CSS_button("images/controllers-02.png"))
            self.ui.keyboardAndMouseButton.setStyleSheet(CSS_button("images/controllers-04.png"))
            self.ui.spaceMouseButton.setStyleSheet(CSS_buttonActive("images/controllers-01.png"))
            self.ui.label_controller_info.setText(QCoreApplication.translate("MainWindow", u"CamBot 6D is compatible with 3Dconnexion SpaceMouse Enterprise, Pro, and Compact 3D mice.\n\nNote: Works in fullscreen mode if combined with Stream Deck MQTT remote. Allows for analog control of all 6 axis, but has no decoupled control of individual axis.", None))
            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def on_controllerUpdate_clicked(self):
            self.repopulate_controllers_dropdown()


        def on_controllerSelection_changed(self, i):
            global controller_id
            global controller_name
            global joystick
            global gamepad

            print ("Current index",i,"selection changed ",self.ui.controllerSelection.currentText())
            print("Count", pygame.joystick.get_count())

            match controller:
                case "xboxone": # We test for different values and print different messages
                    if i > 0 and i <= pygame.joystick.get_count():
                        config.set('controllers', 'xboxone_id', joystickUids[i-1])
                        config.set('controllers', 'xboxone_name', joystickNames[i-1])
                        gamepad = joystickUids[i-1]
                    elif i == 0:
                        config.set('controllers', 'xboxone_id', '')
                        config.set('controllers', 'xboxone_name', '')
                        gamepad = None
                    else:
                        config.set('controllers', 'xboxone_id', str(controller_id))
                        config.set('controllers', 'xboxone_name', str(controller_name))
                        gamepad = controller_id
                case "spacemouse": # We test for different values and print different messages
                    if i > 0 and i <= pygame.joystick.get_count():
                        config.set('controllers', 'spacemouse_id', joystickUids[i-1])
                        config.set('controllers', 'spacemouse_name', joystickNames[i-1])
                        joystick = joystickUids[i-1]
                    elif i == 0:
                        config.set('controllers', 'spacemouse_id', '')
                        config.set('controllers', 'spacemouse_name', '')
                        joystick = None
                    else:
                        config.set('controllers', 'spacemouse_id', str(controller_id))
                        config.set('controllers', 'spacemouse_name', str(controller_name))
                        joystick = controller_id
                case "keyboardandmouse":
                    self.ui.controllerSelection.setCurrentIndex(1)

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

            print('gamepad', gamepad)
            print('joystick', joystick)

        def on_hotkeyEnable_changed(self, i):

            value = 'true'
            if i == 0:
                value = 'false'
                self.F.stop_hotkey()
            else:
                self.F.start_hotkey()

            config.set('main', 'hotkey', value )

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def on_wrapRotationCheckBox_changed(self, i):

            global xboxone_wrap_rotation
            global spacemouse_wrap_rotation
            global keyboard_wrap_rotation

            value = 'true'
            valueBol = True
            if i == 0:
                value = 'false'
                valueBol = False

            match controller:
                case "xboxone":
                    config.set('controllers', 'xboxone_wrap_rotation', value)
                    xboxone_wrap_rotation = valueBol
                case "spacemouse":
                    config.set('controllers', 'spacemouse_wrap_rotation', value)
                    spacemouse_wrap_rotation = valueBol
                case "keyboardandmouse":
                    config.set('controllers', 'keyboard_wrap_rotation', value)
                    keyboard_wrap_rotation = valueBol

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def on_invertRollCheckBox_changed(self, i):

            global xboxone_invert_roll
            global spacemouse_invert_roll
            global keyboard_invert_roll

            value = 'true'
            valueBol = True
            if i == 0:
                value = 'false'
                valueBol = False

            match controller:
                case "xboxone":
                    config.set('controllers', 'xboxone_invert_roll', value)
                    xboxone_invert_roll = valueBol
                case "spacemouse":
                    config.set('controllers', 'spacemouse_invert_roll', value)
                    spacemouse_invert_roll = valueBol
                case "keyboardandmouse":
                    config.set('controllers', 'keyboard_invert_roll', value)
                    keyboard_invert_roll = valueBol

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])



        def on_invertPitchCheckBox_changed(self, i):

            global xboxone_invert_pitch
            global spacemouse_invert_pitch
            global keyboard_invert_pitch

            value = 'true'
            valueBol = True
            if i == 0:
                value = 'false'
                valueBol = False

            match controller:
                case "xboxone":
                    config.set('controllers', 'xboxone_invert_pitch', value)
                    xboxone_invert_pitch = valueBol
                case "spacemouse":
                    config.set('controllers', 'spacemouse_invert_pitch', value)
                    spacemouse_invert_pitch = valueBol
                case "keyboardandmouse":
                    config.set('controllers', 'keyboard_invert_pitch', value)
                    keyboard_invert_pitch = valueBol

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def on_invertYawCheckBox_changed(self, i):

            global xboxone_invert_yaw
            global spacemouse_invert_yaw
            global keyboard_invert_yaw

            value = 'true'
            valueBol = True
            if i == 0:
                value = 'false'
                valueBol = False

            match controller:
                case "xboxone":
                    config.set('controllers', 'xboxone_invert_yaw', value)
                    xboxone_invert_yaw = valueBol
                case "spacemouse":
                    config.set('controllers', 'spacemouse_invert_yaw', value)
                    spacemouse_invert_yaw = valueBol
                case "keyboardandmouse":
                    config.set('controllers', 'keyboard_invert_yaw', value)
                    keyboard_invert_yaw = valueBol

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def on_voiceEnable_changed(self, i):
            global voice_enable

            value = 'true'
            if i == 0:
                value = 'false'
                voice_enable = False
            else:
                voice_enable = True

            voice = False
            if config.has_option('voice', 'id'):
                voice = config.get('voice', 'id')

            restart_tts(voice,rate,volume)

            print ("Voice enable",voice_enable)

            config.set('main', 'voice', value)

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_mqttEnable_changed(self, i):

            value = 'true'
            if i == 0:
                value = 'false'
                self.stop_mqtt()
            else:
                self.start_mqtt()

            config.set('main', 'mqtt', value)

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_motionSelection_changed(self, i):

            global xboxone_motion
            global spacemouse_motion
            global keyboard_motion

            match controller:
                case "xboxone":
                    config.set('controllers', 'xboxone_motion', str(i))
                    xboxone_motion = i
                case "spacemouse":
                    config.set('controllers', 'spacemouse_motion', str(i))
                    spacemouse_motion = i
                case "keyboardandmouse":
                    config.set('controllers', 'keyboard_motion', str(i))
                    keyboard_motion = i

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_easeSelection_changed(self, i):
            global path_ease_selection

            path_ease_selection = i
            config.set('speed', 'path_ease', str(path_ease_selection))

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_skipEaseSelection_changed(self, i):
            global point_ease_selection

            point_ease_selection = i
            config.set('speed', 'point_ease', str(point_ease_selection))

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_spatialInterpolationSelection_changed(self, i):
            global spatial_selection

            spatial_selection = i
            config.set('speed', 'spatial', str(spatial_selection))

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])

        def on_temporalInterpolationSelection_changed(self, i):
            global temporal_selection

            if i > 1:
                temporal_selection = 0
                self.ui.temporalInterpolationSelection.setCurrentIndex(temporal_selection)
            else:
                temporal_selection = i
            config.set('speed', 'temporal', str(temporal_selection))

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])



        def on_voiceSelection_changed(self, i):

            print ("Current index",i,"selection changed ",self.ui.voiceSelection.currentText())

            restart_tts(voices[i].id,rate,volume)

            config.set('voice', 'id', voices[i].id)

            try:
                with open(configIni, 'w') as f:
                    config.write(f)
            except OSError as error:
                print(sys.exc_info()[0])


        def connect_to_mqtt(self, name):
            global mqtt_ip
            global mqtt_port
            global mqtt_user
            global mqtt_pass
            global mqtt_ip_default
            global mqtt_port_default
            print('STARTING MQTT client')
            # client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
            client.on_connect = self.on_connect  # Define callback function for successful connection
            client.on_disconnect = self.on_disconnect  # Define callback function for disconnect
            client.on_message = self.on_message  # Define callback function for receipt of a message
            print('user/pass', mqtt_user, mqtt_pass)
            if mqtt_user or mqtt_pass:
                client.username_pw_set(mqtt_user, mqtt_pass)
            else:
                client.username_pw_set(None, None)
            ip = mqtt_ip_default
            port = mqtt_port_default
            if mqtt_ip:
                ip = mqtt_ip
            if mqtt_port:
                port = mqtt_port
            print(ip, port)
            client.connect(ip, int(port))
            client.loop_forever()

        def on_disconnect(self, client, userdata, rc):  # The callback for when the client connects to the broker
            print('disconnected!')
            self.mqtt_connected = False

        def on_connect(self, client, userdata, flags, rc):  # The callback for when the client connects to the broker
            self.mqtt_flag = rc
            self.mqtt_connected = True
            if rc != 0:
                print("CONNECTION ERROR")
                if rc == 1:
                    self.mqtt_error(u"BAD PROTOCOL", True)
                if rc == 2:
                    self.mqtt_error(u"CLIENT-ID ERROR", True)
                if rc == 3:
                    self.mqtt_error(u"SERVICE UNAVAILABLE", True)
                if rc == 4:
                    self.mqtt_error(u"BAD USERNAME OR PASSWORD", True)
                if rc == 5:
                    self.mqtt_error(u"NOT AUTHORIZED", True)
            else:
                self.mqtt_error(u"CONNECTED", False)
            print("CONNECTED MQTT client with result code {0}".format(str(rc)))  # Print result of connection attempt
            client.subscribe("/opentrack/move")  # Subscribe to the topic “digitest/test1”, receive any messages published on it

        def on_message(self, client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
            print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg

        def mqtt_error(self, message, error):
            if error:
                client.disconnect() # disconnect gracefully
                client.loop_stop() # stops network loop
            self.ui.MQTTTestButton.setIcon(QIcon())
            self.ui.MQTTTestButton.setText(QCoreApplication.translate("MainWindow", message, None))

        def start_mqtt(self):
            global mqtt_thread
            self.ui.MQTTTestButton.setEnabled(False)

            print(self.mqtt_connected, self.mqtt_flag)

            if self.mqtt_flag == 0 and self.mqtt_connected == True:
                self.stop_mqtt()
            else:
                client.disconnect() # disconnect gracefully
                client.loop_stop() # stops network loop
                mqtt_thread = Thread(target=self.connect_to_mqtt, args=("Thread",))
                mqtt_thread.start()
                self.mqtt_error(u"CONNECTING", False)
                QtCore.QTimer.singleShot(5000, self.check_mqtt)

        def check_mqtt(self):
            if self.mqtt_connected and self.mqtt_flag == 0:
                play_icon = QIcon()
                play_icon.addFile(u":/16x16/icons/16x16/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.MQTTTestButton.setIcon(play_icon)
                self.ui.MQTTTestButton.setText(QCoreApplication.translate("MainWindow", u" DISCONNECT", None))
                self.ui.MQTTTestButton.setEnabled(True)
            else:
                self.stop_mqtt()

        def stop_mqtt(self):
            print('stopping MQTT')
            global mqtt_thread
            client.disconnect() # disconnect gracefully
            client.loop_stop() # stops network loop
            if mqtt_thread and mqtt_thread.is_alive():
                mqtt_thread.join()
            print('MQTT stopped')
            play_icon = QIcon()
            play_icon.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.MQTTTestButton.setIcon(play_icon)
            self.ui.MQTTTestButton.setText(QCoreApplication.translate("MainWindow", u" CONNECT TO BROKER", None))
            self.ui.MQTTTestButton.setEnabled(True)


        # ------------------------------------------------------------------ #
        #  Dual-PC UDP streaming                                              #
        # ------------------------------------------------------------------ #

        def set_dualpc_status(self, text, color=''):
            """Update label_version with dual-PC connection status."""
            version_link = u'<a style="text-decoration: none; color: #62676f;" href="https://github.com/thelordskippy/CamBot6D/releases">{}</a>'.format(version)
            if text:
                span = u'<span style="color: {};">{}</span>'.format(color, text)
                self.ui.label_version.setText(version_link + u' \u2013 ' + span)
            else:
                self.ui.label_version.setText(
                    u'<span style="text-decoration: none; color: #62676f;">disconnected</span>')

        def on_remoteSelection_changed(self, i):
            global dualpc_role
            dualpc_role = i
            config.set('dualpc', 'role', str(i))
            self.write_config()
            self.stop_dualpc()
            if i == 1 and dualpc_derived_key:
                self.start_dualpc_host()
            elif i == 2 and dualpc_derived_key:
                self.start_dualpc_controller()
            elif i == 0:
                # Restore game connection status label
                self.ui.label_version.setText(
                    u'<a style="text-decoration: none; color: #62676f;"'
                    u' href="https://github.com/thelordskippy/CamBot6D/releases">'
                    + version +
                    u'</a> \u2013 <span style="text-decoration: none;'
                    u' color: #62676f;">disconnected</span>')
                self.ui.label_version.setToolTip(u'please launch Star Citizen')

        def on_dualpc_password_set(self):
            global dualpc_derived_key, dualpc_key_salt
            password = self.ui.dualPCPasswordEdit.text().strip()
            if not password:
                return
            salt = _secrets.token_bytes(16)
            key  = cambot_protocol.derive_key(password, salt)
            dualpc_key_salt    = salt
            dualpc_derived_key = key
            config.set('dualpc', 'key_salt',    salt.hex())
            config.set('dualpc', 'key_derived',  key.hex())
            self.write_config()
            self.ui.dualPCPasswordEdit.clear()
            # Restart streaming with new key if already in a role
            if dualpc_role > 0:
                self.on_remoteSelection_changed(dualpc_role)

        def start_dualpc_host(self):
            """Start the Gaming PC UDP receiver thread."""
            global dualpc_running
            self.stop_dualpc()
            dualpc_running = True
            t = Thread(target=self.dualpc_receiver_thread, daemon=True)
            t.start()
            port = int(opentrack_port) if opentrack_port else dualpc_port
            self.set_dualpc_status('waiting for Remote PC', '#62676f')
            self.ui.label_version.setToolTip('listening on port {}'.format(port))

        def start_dualpc_controller(self):
            """Start the Controller PC UDP sender thread."""
            global dualpc_running
            self.stop_dualpc()
            dualpc_running = True
            t = Thread(target=self.dualpc_sender_thread, daemon=True)
            t.start()
            self.set_dualpc_status('Gaming PC disconnected', '#62676f')
            self.ui.label_version.setToolTip('enter Gaming PC IP and shared password')

        def stop_dualpc(self):
            global dualpc_running
            dualpc_running = False

        def dualpc_receiver_thread(self):
            """Gaming PC: receive axes + buttons from Controller PC, forward to FreeTrack."""
            port = int(opentrack_port) if opentrack_port else dualpc_port
            last_seq_map   = {}
            pending_hello  = {}   # sender_ip -> (nonce, timestamp)
            authenticated  = set()

            sock = _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)
            sock.setsockopt(_socket.SOL_SOCKET, _socket.SO_REUSEADDR, 1)
            sock.settimeout(1.0)
            try:
                sock.bind(('', port))
            except OSError as e:
                print('DualPC host bind error:', e)
                self.dualpc_bind_error_signal.emit()
                return

            print('DualPC host listening on UDP port', port)

            # Check for Windows Firewall block rule (runs once per session start)
            if _check_firewall_block():
                self.dualpc_firewall_warning_signal.emit()

            while dualpc_running:
                try:
                    data, addr = sock.recvfrom(512)
                except _socket.timeout:
                    continue
                except OSError:
                    break

                sender_ip = addr[0]

                if len(data) < 2:
                    continue

                msg_type = data[1]

                # --- Handshake: HELLO_ACK from controller ---
                if msg_type == cambot_protocol.MSG_HELLO_ACK:
                    pdata = pending_hello.get(sender_ip)
                    if pdata:
                        nonce, _ = pdata
                        if cambot_protocol.verify_hello_ack(data, nonce, dualpc_derived_key):
                            # Authenticated: clear seq map so restarted controller is accepted
                            last_seq_map.pop(sender_ip, None)
                            authenticated.add(sender_ip)
                            pending_hello.pop(sender_ip, None)
                            print('DualPC: authenticated', sender_ip)
                            self.dualpc_status_signal.emit(
                                'Remote PC connected', '#4CAF50',
                                'receiving from {}'.format(sender_ip))
                    continue

                # --- Data packet: initiate/retry handshake if not authenticated ---
                if sender_ip not in authenticated:
                    pdata = pending_hello.get(sender_ip)
                    if pdata is None or (time.monotonic() - pdata[1]) > 5.0:
                        nonce = _secrets.token_bytes(16)
                        pending_hello[sender_ip] = (nonce, time.monotonic())
                        hello_pkt = cambot_protocol.pack_hello(nonce)
                        try:
                            sock.sendto(hello_pkt, addr)
                        except OSError:
                            pass
                    continue

                # --- Verified data ---
                result = cambot_protocol.verify_and_unpack(
                    data, dualpc_derived_key, last_seq_map, sender_ip)
                if result is None:
                    continue

                if result['type'] == cambot_protocol.MSG_AXES:
                    self.F.updateFreeTrack(
                        result['x'], result['y'], result['z'],
                        result['yaw'], result['pitch'], result['roll'])

            sock.close()
            print('DualPC host stopped')

        def dualpc_sender_thread(self):
            """Controller PC: send axes + buttons to Gaming PC at ~100 Hz."""
            global dualpc_seq
            target_ip   = opentrack_ip if opentrack_ip else '127.0.0.1'
            target_port = int(opentrack_port) if opentrack_port else dualpc_port

            sock = _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)
            sock.settimeout(0)   # non-blocking for recv (MSG_HELLO from host)

            interval = 1.0 / 100  # 100 Hz
            next_send = time.monotonic()

            print('DualPC controller → {}:{}'.format(target_ip, target_port))

            while dualpc_running:
                now = time.monotonic()

                # Check for incoming MSG_HELLO from Gaming PC
                readable, _, _ = _select.select([sock], [], [], 0)
                if readable:
                    try:
                        data, _ = sock.recvfrom(512)
                        if len(data) >= 2 and data[1] == cambot_protocol.MSG_HELLO:
                            result = cambot_protocol.verify_and_unpack(
                                data, dualpc_derived_key, {}, '0.0.0.0')
                            if result and result['type'] == cambot_protocol.MSG_HELLO:
                                ack = cambot_protocol.pack_hello_ack(
                                    result['nonce'], dualpc_derived_key)
                                try:
                                    sock.sendto(ack, (target_ip, target_port))
                                    self.dualpc_status_signal.emit(
                                        'Gaming PC connected', '#4CAF50',
                                        'streaming to {}'.format(target_ip))
                                except OSError:
                                    pass
                    except (BlockingIOError, OSError):
                        pass

                # Rate-limit to 100 Hz
                if now < next_send:
                    time.sleep(max(0, next_send - now))
                    continue
                next_send += interval

                # Send axes
                dualpc_seq += 1
                try:
                    pkt = cambot_protocol.pack_axes(
                        dualpc_seq, x, y, z, yaw, pitch, roll,
                        dualpc_derived_key)
                    sock.sendto(pkt, (target_ip, target_port))
                except OSError as e:
                    print('DualPC send error:', e)


            sock.close()
            print('DualPC controller stopped')

        @Slot(str, str, str)
        def _dualpc_update_status(self, text, color, tooltip):
            self.set_dualpc_status(text, color)
            if tooltip:
                self.ui.label_version.setToolTip(tooltip)

        @Slot()
        def _dualpc_host_bind_error(self):
            self.set_dualpc_status('port bind error', '#E57373')

        @Slot()
        def _show_firewall_warning(self):
            msg = QMessageBox(self)
            msg.setWindowTitle("Windows Firewall is blocking CamBot 6D")
            msg.setIcon(QMessageBox.Warning)
            msg.setText(
                "Windows Firewall has a <b>Block</b> rule for this application, "
                "which will prevent the Remote Control PC from connecting.")
            msg.setInformativeText(
                "To fix:\n"
                "1. Open <b>Windows Defender Firewall with Advanced Security</b>\n"
                "2. Click <b>Inbound Rules</b> in the left pane\n"
                "3. Find the rule for <i>python.exe</i> or <i>CamBot6D.exe</i> "
                "with a red \u2715 (Block) icon\n"
                "4. Right-click it and choose <b>Delete</b> (or change Action to Allow)\n"
                "5. Toggle the Gaming PC mode off and on again in CamBot 6D")
            open_btn = msg.addButton("Open Firewall Settings", QMessageBox.ActionRole)
            msg.addButton("Dismiss", QMessageBox.RejectRole)
            msg.exec_()
            if msg.clickedButton() == open_btn:
                subprocess.Popen(['mmc', 'wf.msc'])

        # ------------------------------------------------------------------ #

        def joystick_thread(self):

            global x
            global y
            global z
            global yaw
            global pitch
            global roll
            global controllerTest
            global tts
            global controllers_count
            global joystickNames
            global joystickUids
            global joystickIds
            global joystick
            global gamepad

            xboxone_sensitivity = 1
            _xbox_last_id = -1
            _xbox_debug_counter = 0

            # Xbox button indices for pygame.joystick.Joystick + SDL2.
            # pygame.CONTROLLER_BUTTON_* values are for pygame.controller.Controller
            # and do NOT match (e.g. CONTROLLER_BUTTON_LEFTSHOULDER == 9, not 4).
            XBOX_BTN_A    = 0
            XBOX_BTN_B    = 1
            XBOX_BTN_X    = 2
            XBOX_BTN_Y    = 3
            XBOX_BTN_LB   = 4   # Left Bumper
            XBOX_BTN_RB   = 5   # Right Bumper
            XBOX_BTN_VIEW = 6   # View / Back
            XBOX_BTN_MENU = 7   # Menu / Start
            XBOX_BTN_LS   = 8   # Left Stick click
            XBOX_BTN_RS   = 9   # Right Stick click
            XBOX_BTN_XBOX = 11  # Xbox / Guide button

            while joystick_loop:

                controller_id = -1

                time.sleep(0.005) #200 fps (ish) !!!change this to proper 120 fps

                if self.F.roboting:
                    x = self.F.x
                    y = self.F.y
                    z = self.F.z
                    yaw = self.F.yaw
                    pitch = self.F.pitch
                    roll = self.F.roll

                else:

                    try:
                        if controllers_count != pygame.joystick.get_count():
                            controllers_count = pygame.joystick.get_count()
                            self.repopulate_controllers_dropdown()
                            #self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"penis", None))
                            print("controllers changed")
                            #joystickNames = [pygame.joystick.Joystick(x).get_name() for x in range(pygame.joystick.get_count())]
                            #joystickIds = [pygame.joystick.Joystick(x).get_instance_id() for x in range(pygame.joystick.get_count())]
                            #joystickUids = [pygame.joystick.Joystick(x).get_guid() for x in range(pygame.joystick.get_count())]
                    except pygame.error as message:
                        print(message)

                    if controller == 'xboxone':
                        pygame.event.pump()

                        if gamepad is not None:
                            controller_id = -1
                            try:
                                for c in range(pygame.joystick.get_count()):
                                    temp_joy = pygame.joystick.Joystick(c)
                                    # Ensure it's initialized to get GUID
                                    if not temp_joy.get_init(): temp_joy.init()

                                    if gamepad == temp_joy.get_guid():
                                        controller_id = c
                                        break
                            except pygame.error as message:
                                print(f"Discovery error: {message}")

                            if controller_id >= 0:
                                joy = pygame.joystick.Joystick(controller_id)
                                if not joy.get_init(): joy.init()

                                if controller_id != _xbox_last_id:
                                    _xbox_last_id = controller_id
                                    print(f"Using controller: {joy.get_name()}  ({joy.get_numaxes()} axes, {joy.get_numbuttons()} buttons)")

                                invert_roll = -1 if xboxone_invert_roll else 1
                                invert_yaw = -1 if xboxone_invert_yaw else 1
                                invert_pitch = -1 if not xboxone_invert_pitch else 1

                                try:
                                    # SDL2 axis reads — indices match pygame.CONTROLLER_AXIS_* constants
                                    left_x  = joy.get_axis(pygame.CONTROLLER_AXIS_LEFTX)        # Left Stick X
                                    left_y  = joy.get_axis(pygame.CONTROLLER_AXIS_LEFTY)        # Left Stick Y
                                    right_x = joy.get_axis(pygame.CONTROLLER_AXIS_RIGHTX)       # Right Stick X
                                    right_y = joy.get_axis(pygame.CONTROLLER_AXIS_RIGHTY)       # Right Stick Y
                                    trig_l  = joy.get_axis(pygame.CONTROLLER_AXIS_TRIGGERLEFT)  # Left Trigger  (-1 idle → +1 full)
                                    trig_r  = joy.get_axis(pygame.CONTROLLER_AXIS_TRIGGERRIGHT) # Right Trigger (-1 idle → +1 full)

                                    # Live axis verification (throttled — prints ~1/sec at 200 Hz)
                                    _xbox_debug_counter += 1
                                    if _xbox_debug_counter % 10 == 0:
                                        print(f"[Xbox axes] LS=({left_x:+.4f},{left_y:+.4f})  RS=({right_x:+.4f},{right_y:+.4f})  LT={trig_l:+.4f}  RT={trig_r:+.4f}")

                                    stick_x     = self.Deadzone(left_x,  .05)  # Left Stick X  → camera X
                                    stick_z     = self.Deadzone(left_y,  .05)  # Left Stick Y  → camera Z
                                    stick_yaw   = self.Deadzone(right_x, .05)  # Right Stick X → yaw
                                    stick_pitch = self.Deadzone(right_y, .05)  # Right Stick Y → pitch

                                    # Triggers: SDL2 -1.0 idle → +1.0 full; normalize to 0–1
                                    stick_y0 = (trig_l + 1.0) / 2.0  # Left Trigger  → camera Y down
                                    stick_y1 = (trig_r + 1.0) / 2.0  # Right Trigger → camera Y up

                                    if xboxone_motion == 0:  # absolute coordinates
                                        x = increment(x, (- stick_x) * xboxone_sensitivity)
                                        z = increment(z, (stick_z) * xboxone_sensitivity)
                                        # Simplified Y calculation (Right trigger up, Left trigger down)
                                        y = increment(y, (stick_y1 - stick_y0) * xboxone_sensitivity)

                                        yaw = increment(yaw, (- stick_yaw * invert_yaw) / 200 * xboxone_sensitivity)
                                        pitch = increment(pitch,
                                                          (stick_pitch * invert_pitch) / 200 * xboxone_sensitivity)

                                        if joy.get_button(XBOX_BTN_LB):
                                            roll = roll + 0.0025 * xboxone_sensitivity * invert_roll
                                        if joy.get_button(XBOX_BTN_RB):
                                            roll = roll - 0.0025 * xboxone_sensitivity * invert_roll

                                    else:  # relative coordinates
                                        x = increment(x, (- math.sin(yaw) * stick_z - math.cos(
                                            yaw) * stick_x) * xboxone_sensitivity)
                                        z = increment(z, (- math.sin(yaw) * stick_x + math.cos(
                                            yaw) * stick_z) * xboxone_sensitivity)
                                        y = increment(y, (stick_y1 - stick_y0) * xboxone_sensitivity)

                                        yaw = increment(yaw, (- stick_yaw * invert_yaw) / 200 * xboxone_sensitivity)
                                        pitch = increment(pitch, (- math.sin(roll) * stick_yaw * invert_yaw + math.cos(
                                            roll) * stick_pitch * invert_pitch) / 200 * xboxone_sensitivity)
                                        roll = increment(roll, (math.sin(
                                            pitch) * stick_yaw * invert_yaw) / 200 * xboxone_sensitivity)

                                        if joy.get_button(XBOX_BTN_LB):
                                            roll = (roll + math.cos(pitch) * 0.0025 * xboxone_sensitivity * invert_roll)
                                            yaw = (yaw + math.sin(pitch) * 0.0025 * xboxone_sensitivity * invert_roll)
                                        if joy.get_button(XBOX_BTN_RB):
                                            roll = (roll - math.cos(pitch) * 0.0025 * xboxone_sensitivity * invert_roll)
                                            yaw = (yaw - math.sin(pitch) * 0.0025 * xboxone_sensitivity * invert_roll)

                                    # Wrap rotations
                                    if xboxone_wrap_rotation:
                                        yaw = (yaw + math.pi) % (2 * math.pi) - math.pi
                                        pitch = (pitch + math.pi) % (2 * math.pi) - math.pi
                                        roll = (roll + math.pi) % (2 * math.pi) - math.pi

                                    # Limits and Rumble (Pygame 2 specific)
                                    if any(abs(v) > 500 for v in [x, y, z]) or any(
                                            abs(v) > math.pi for v in [yaw, pitch, roll]):
                                        # rumble(low_freq, high_freq, duration_ms)
                                        joy.rumble(0, 0.5, 500)
                                        x = np.clip(x, -500, 500)
                                        y = np.clip(y, -500, 500)
                                        z = np.clip(z, -500, 500)
                                        yaw = np.clip(yaw, -math.pi, math.pi)
                                        pitch = np.clip(pitch, -math.pi, math.pi)
                                        roll = np.clip(roll, -math.pi, math.pi)
                                    else:
                                        joy.stop_rumble()

                                    # Event Handling
                                    for event in pygame.event.get():
                                        if event.type == pygame.JOYHATMOTION:
                                            # D-Pad sensitivity control
                                            hat_x, hat_y = event.value
                                            if hat_y == 1:
                                                xboxone_sensitivity = min(16, xboxone_sensitivity * math.sqrt(2))
                                            elif hat_y == -1:
                                                xboxone_sensitivity = max(0.0625, xboxone_sensitivity / math.sqrt(2))

                                        if event.type == pygame.JOYBUTTONDOWN:
                                            btn = event.button
                                            if btn == XBOX_BTN_A:    self.ui.pushButton_add_waypoint.click()
                                            if btn == XBOX_BTN_B:    self.ui.pushButton_delete_all.click()
                                            if btn == XBOX_BTN_X:    self.F.goHome(q, config)
                                            if btn == XBOX_BTN_VIEW: self.goBackward(q, config)
                                            if btn == XBOX_BTN_MENU: self.goForward(q, config)
                                            if btn == XBOX_BTN_XBOX: self.showForeground()

                                except pygame.error as message:
                                    print(f"Read error on ID {controller_id}: {message}")

                        #print(x,y,z,yaw,pitch,roll)

                    elif controller == 'spacemouse':

                        pygame.event.pump()

                        if joystick != None:

                            try:
                                for c in range(pygame.joystick.get_count()):
                                    if joystick == pygame.joystick.Joystick(c).get_guid():
                                        controller_id = c
                                        break
                            except pygame.error as message:
                                print(message)

                            if controller_id >= 0:

                                try:
                                    x = wraparound(x, - pygame.joystick.Joystick(controller_id).get_axis(0))
                                    y = wraparound(y, - pygame.joystick.Joystick(controller_id).get_axis(2))
                                    z = wraparound(z, pygame.joystick.Joystick(controller_id).get_axis(1))
                                    yaw = wraparound(yaw, pygame.joystick.Joystick(controller_id).get_axis(4))
                                    pitch = wraparound(pitch, pygame.joystick.Joystick(controller_id).get_axis(3))
                                    roll = wraparound(roll, - pygame.joystick.Joystick(controller_id).get_axis(5))

                                    #print(x,y,z,yaw,pitch,roll)
                                except pygame.error as message:
                                    print("Cannot read joystick ID " + str(controller_id))
                                    print(message)
                                    #raise SystemExit(message)

                    if controller == 'xboxone' or controller == 'spacemouse':

                        self.F.updateFreeTrack(x,y,z,yaw,pitch,roll)



        def Deadzone(self, value, zone):
            if (abs(value) < zone):
                return 0
            else:
                if value < 0:
                    return value + zone
                else:
                    return value - zone

        ########################################################################
        ## MENUS ==> DYNAMIC MENUS FUNCTIONS
        ########################################################################
        def Button(self):
            # GET BT CLICKED
            btnWidget = self.sender()

            # PAGE MAIN
            if btnWidget.objectName() == "btn_main":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_main)
                UIFunctions.resetStyle(self, "btn_main")
                UIFunctions.labelPage(self, "Camera")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

            # PAGE CONTROLLERS
            if btnWidget.objectName() == "btn_controllers":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_controllers)
                UIFunctions.resetStyle(self, "btn_controllers")
                UIFunctions.labelPage(self, "Controllers")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

            # PAGE MAIN
            if btnWidget.objectName() == "btn_info":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_info)
                UIFunctions.resetStyle(self, "btn_info")
                UIFunctions.labelPage(self, "Info")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))


            # PAGE MAIN
            if btnWidget.objectName() == "btn_settings":
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_settings)
                UIFunctions.resetStyle(self, "btn_settings")
                UIFunctions.labelPage(self, "Settings")
                btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        ## ==> END ##

        ########################################################################
        ## START ==> APP EVENTS
        ########################################################################

        ## EVENT ==> MOUSE DOUBLE CLICK
        ########################################################################
        def eventFilter(self, watched, event):
            if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
                print("pos: ", event.pos())
        ## ==> END ##

        ## EVENT ==> MOUSE CLICK
        ########################################################################
        def mousePressEvent(self, event):
            self.dragPos = event.globalPos()
            if event.buttons() == Qt.LeftButton:
                print('Mouse click: LEFT CLICK')
            if event.buttons() == Qt.RightButton:
                print('Mouse click: RIGHT CLICK')
            if event.buttons() == Qt.MidButton:
                print('Mouse click: MIDDLE BUTTON')
        ## ==> END ##

        ## EVENT ==> KEY PRESSED
        ########################################################################
        def keyPressEvent(self, event):
            print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
            if event.text() == "+":
                self.F.newWaypoint(q, config)
            if event.text() == "-":
                self.F.deleteAll(q, config)
        ## ==> END ##

        ## EVENT ==> RESIZE EVENT
        ########################################################################
        def resizeEvent(self, event):
            self.resizeFunction()
            return super(MainWindow, self).resizeEvent(event)

        def resizeFunction(self):
            print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
        ## ==> END ##

        ########################################################################
        ## END ==> APP EVENTS
        ############################## ---/--/--- ##############################

        def closeEvent(self, event):
            print('collecting threads')
            self.stop_controller_test()
            stop_joystick()
            self.stop_mqtt()
            self.stop_dualpc()
            stop_tts()
            self.F.stop_freetrack()
            self.F.stop_hotkey()
            print('closing')




def tts_queue(queue, voice,rate,volume,voice_enable):
    global tts
    global all_processes
    while True:
        text = queue.get()
        print('TEXT',text,'ENABLE',voice_enable)
        for process in all_processes:
            process.terminate()
        q = Queue()
        if voice_enable:
            tts = Process(target=tts_thread, args=(text,voice,rate,volume))
            tts.daemon = True
            tts.start()
            all_processes.append(tts)

def tts_thread(text, voice,rate,volume):

    engine.setProperty('rate', rate)     # setting up new voice rate
    engine.setProperty('volume',volume)    # setting up volume level  between 0 and 1
    """VOICE"""
    engine.setProperty('voice', voice)  #changing index, changes voices. o for male
    #engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()

def restart_tts(voice,rate,volume):
    global q
    global ttsQ
    global voice_enable
    global voices

    if not voice:
        if voices[0]:
            voice = voices[0].id

    q.put('')
    time.sleep(0.1)
    stop_tts()
    q = Queue()
    ttsQ = Process(target=tts_queue, args=((q),voice,rate,volume,voice_enable))
    ttsQ.start()




def stop_joystick():
    global joystick_loop
    global joystick_value
    joystick_loop = False
    if joystick_value and joystick_value.is_alive():
        joystick_value.join()

def stop_tts():
    global all_processes
    global ttsQ
    for process in all_processes:
        process.terminate()
    ttsQ.terminate()
    ttsQ.join()



if __name__ == "__main__":

    import pygame
    multiprocessing.freeze_support()

    print("\nPLEASE make sure")
    print("- TrackIR v5 is closed\n")
    print("- Star Citizen is launched after CamBot 6D")

    print('READING CONFIG')


    configFolder = os.environ.get('USERPROFILE') + '\\.cambot6d'
    configIni = configFolder + '\\config.ini'

    config.read(configIni)

    if not config.has_section('main'):
        config.add_section('main')

    if config.has_option('main', 'hotkey'):
        hotkey_enable = config.getboolean('main', 'hotkey')
    if config.has_option('main', 'voice'):
        voice_enable = config.getboolean('main', 'voice')
    if config.has_option('main', 'mqtt'):
        mqtt_enable = config.getboolean('main', 'mqtt')

    if not config.has_section('speed'):
        config.add_section('speed')

    if config.has_option('speed', 'path'):
        path_time = config.getfloat('speed', 'path')
    else:
        config.set('speed', 'path', str(path_time))

    if config.has_option('speed', 'point'):
        point_time = config.getfloat('speed', 'point')
    else:
        config.set('speed', 'point', str(point_time))

    if config.has_option('speed', 'path_ease'):
        path_ease_selection = config.getint('speed', 'path_ease')
    else:
        config.set('speed', 'path_ease', str(path_ease_selection))

    if config.has_option('speed', 'point_ease'):
        point_ease_selection = config.getint('speed', 'point_ease')
    else:
        config.set('speed', 'point_ease', str(point_ease_selection))

    if config.has_option('speed', 'spatial'):
        spatial_selection = config.getint('speed', 'spatial')
    else:
        config.set('speed', 'spatial', str(spatial_selection))

    if config.has_option('speed', 'temporal'):
        temporal_selection = config.getint('speed', 'temporal')
    else:
        config.set('speed', 'temporal', str(temporal_selection))


    if not config.has_section('voice'):
        config.add_section('voice')

    if config.has_option('voice', 'id'):
        voice_id = config.get('voice', 'id')

    if config.has_option('voice', 'rate'):
        rate = config.getint('voice', 'rate')
    else:
        config.set('voice', 'rate', str(rate))

    if config.has_option('voice', 'volume'):
        volume = config.getfloat('voice', 'volume')
    else:
        config.set('voice', 'volume', str(volume))

    if not config.has_section('dualpc'):
        config.add_section('dualpc')

    if config.has_option('dualpc', 'ip'):
        opentrack_ip = config.get('dualpc', 'ip')
    if config.has_option('dualpc', 'port'):
        opentrack_port = config.get('dualpc', 'port')
    if config.has_option('dualpc', 'role'):
        dualpc_role = config.getint('dualpc', 'role')
    if config.has_option('dualpc', 'key_salt'):
        _s = config.get('dualpc', 'key_salt')
        if _s:
            dualpc_key_salt = bytes.fromhex(_s)
    if config.has_option('dualpc', 'key_derived'):
        _d = config.get('dualpc', 'key_derived')
        if _d:
            dualpc_derived_key = bytes.fromhex(_d)

    if not config.has_section('mqtt'):
        config.add_section('mqtt')

    if config.has_option('mqtt', 'ip'):
        mqtt_ip = config.get('mqtt', 'ip')
    if config.has_option('mqtt', 'port'):
        mqtt_port = config.get('mqtt', 'port')
    if config.has_option('mqtt', 'user'):
        mqtt_user = config.get('mqtt', 'user')
    if config.has_option('mqtt', 'pass'):
        mqtt_pass = config.get('mqtt', 'pass')


    #print(config.set('main', 'hotkey', 'true'))

    if not config.has_section('controllers'):
        config.add_section('controllers')

    if config.has_option('controllers', 'type'):
        print(config.get('controllers', 'type'))
        controller = config.get('controllers', 'type')
    if config.has_option('controllers', 'spacemouse_id'):
        print(config.get('controllers', 'spacemouse_id'))
    if config.has_option('controllers', 'spacemouse_name'):
        print(config.get('controllers', 'spacemouse_name'))
    if config.has_option('controllers', 'xboxone_id'):
        print(config.get('controllers', 'xboxone_id'))
    if config.has_option('controllers', 'xboxone_name'):
        print(config.get('controllers', 'xboxone_name'))

    if config.has_option('controllers', 'spacemouse_motion'):
        spacemouse_motion = config.getint('controllers', 'spacemouse_motion')
    else:
        config.set('controllers', 'spacemouse_motion', str(spacemouse_motion))
    if config.has_option('controllers', 'spacemouse_invert_pitch'):
        spacemouse_invert_pitch = config.getboolean('controllers', 'spacemouse_invert_pitch')
    if config.has_option('controllers', 'spacemouse_invert_yaw'):
        spacemouse_invert_yaw = config.getboolean('controllers', 'spacemouse_invert_yaw')
    if config.has_option('controllers', 'spacemouse_invert_roll'):
        spacemouse_invert_roll = config.getboolean('controllers', 'spacemouse_invert_roll')
    if config.has_option('controllers', 'spacemouse_wrap_rotation'):
        spacemouse_wrap_rotation = config.getboolean('controllers', 'spacemouse_wrap_rotation')

    if config.has_option('controllers', 'xboxone_motion'):
        xboxone_motion = config.getint('controllers', 'xboxone_motion')
    else:
        config.set('controllers', 'xboxone_motion', str(xboxone_motion))
    if config.has_option('controllers', 'xboxone_invert_pitch'):
        xboxone_invert_pitch = config.getboolean('controllers', 'xboxone_invert_pitch')
    if config.has_option('controllers', 'xboxone_invert_yaw'):
        xboxone_invert_yaw = config.getboolean('controllers', 'xboxone_invert_yaw')
    if config.has_option('controllers', 'xboxone_invert_roll'):
        xboxone_invert_roll = config.getboolean('controllers', 'xboxone_invert_roll')
    if config.has_option('controllers', 'xboxone_wrap_rotation'):
        xboxone_wrap_rotation = config.getboolean('controllers', 'xboxone_wrap_rotation')

    if config.has_option('controllers', 'keyboard_motion'):
        keyboard_motion = config.getint('controllers', 'keyboard_motion')
    else:
        config.set('controllers', 'keyboard_motion', str(keyboard_motion))
    if config.has_option('controllers', 'keyboard_invert_pitch'):
        keyboard_invert_pitch = config.getboolean('controllers', 'keyboard_invert_pitch')
    if config.has_option('controllers', 'keyboard_invert_yaw'):
        keyboard_invert_yaw = config.getboolean('controllers', 'keyboard_invert_yaw')
    if config.has_option('controllers', 'keyboard_invert_roll'):
        keyboard_invert_roll = config.getboolean('controllers', 'keyboard_invert_roll')
    if config.has_option('controllers', 'keyboard_wrap_rotation'):
        keyboard_wrap_rotation = config.getboolean('controllers', 'keyboard_wrap_rotation')

    # getfloat() raises an exception if the value is not a float
    # getint() and getboolean() also do this for their respective types

    if not os.path.isdir(configFolder):
        try:
            os.mkdir(configFolder)
        except OSError as error:
            print(error)

    try:
        with open(configIni, 'w') as f:
            config.write(f)
    except OSError as error:
        print(sys.exc_info()[0])



    print('STARTING PYGAME client')

    pygame.joystick.init()

    joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
    print(joysticks)
    joystickNames = [pygame.joystick.Joystick(x).get_name() for x in range(pygame.joystick.get_count())]
    joystickIds = [pygame.joystick.Joystick(x).get_instance_id() for x in range(pygame.joystick.get_count())]
    joystickUids = [pygame.joystick.Joystick(x).get_guid() for x in range(pygame.joystick.get_count())]
    print(joystickIds)
    print(joystickUids)
    print(joystickNames)

    pygame.display.set_caption("CamBot 6D - controller")
    icon = pygame.image.load('icons/16x16/cil-3d.png')
    pygame.display.set_icon(icon)

    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')



    voices = engine.getProperty('voices')       #getting details of current voice

    #select voice from config file, only if voice still exists on PC
    if voice_id:
        for thisvoice in voices:
            if thisvoice.id == voice_id:
                voice = thisvoice.id
    #else select first voice in list
    if not voice:
        if voices[0]:
            voice = voices[0].id
    if voice:
        ttsQ = Process(target=tts_queue, args=((q),voice,rate,volume,voice_enable))
        #ttsQ.daemon = True
        ttsQ.start()

    window = MainWindow()

    sys.exit(app.exec_())



