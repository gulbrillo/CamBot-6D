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
    from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
    from PySide2.QtWidgets import *
    import time
    from threading import Thread
    from app_modules import *
    import numpy as np
    import win32api
    import win32con
    import win32gui
    try:
        import pyi_splash
    except:
        print ('dev mode')


try:
    # Update the text on the splash screen
    pyi_splash.update_text("PyInstaller is a great software!")
    pyi_splash.update_text("Second time's a charm!")
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
camera_path_loop = False
camera_path_thread = ''

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

transparency = (85, 85, 85) #everything that's black is transparent

fps = 60

#camera bot
start_points = 100 #todo:  option!
points = 2000
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
#spacemouse
joystick_loop = True
joystick = None
speed_t = 10 #translational
speed_r = 25 #rotational
#xboxone
gamepad = None

#mqtt
broker_address="192.168.1.10" #todo:  option!
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

    if abs(new) < 0.05:
        return old
    else:
        return old + new/100

if __name__ != "__mp_main__":
    class MainWindow(QMainWindow):

        def __init__(self):

            global mqtt_ip
            global mqtt_port
            global mqtt_user
            global mqtt_pass

            global opentrack_ip
            global opentrack_port
            global voice_enable
            global joystick_value

            F = Functions(self, UIFunctions)

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

            global camera_path_thread
            camera_path_thread = Thread(target=do_camera_path, args=("Thread",))

            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.F = F

            joystick_value = Thread(target=self.joystick_thread)
            joystick_value.start()

            self.mqtt_flag = None
            self.mqtt_connected = False

            self.ui.controllerSelection.addItem("")
            self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select a controller)", None))
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

            match controller:
                case "xboxone":
                    self.ui.xBoxButton.click()
                case "spacemouse":
                    self.ui.spaceMouseButton.click()


            ## PRINT ==> SYSTEM
            print('System: ' + platform.system())
            print('Version: ' +platform.release())

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
            #self.ui.pushButton_delete_all.clicked.connect()

            ## ==> play sample voice line
            self.ui.voiceTestButton.clicked.connect(lambda: q.put('This is a test of the CamBot 6D audio feedback system.'))

            self.ui.opentrackIPEdit.setText(QCoreApplication.translate("MainWindow", str(opentrack_ip), None))
            self.ui.opentrackIPEdit.textChanged.connect(self.opentrack_ip_changed)

            self.ui.opentrackPortEdit.setText(QCoreApplication.translate("MainWindow", str(opentrack_port), None))
            self.ui.opentrackPortEdit.textChanged.connect(self.opentrack_port_changed)

            self.ui.MQTTIPEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_ip), None))
            self.ui.MQTTIPEdit.textChanged.connect(self.mqtt_ip_changed)

            self.ui.MQTTPortEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_port), None))
            self.ui.MQTTPortEdit.textChanged.connect(self.mqtt_port_changed)

            self.ui.MQTTUserEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_user), None))
            self.ui.MQTTUserEdit.textChanged.connect(self.mqtt_user_changed)

            self.ui.MQTTPassEdit.setText(QCoreApplication.translate("MainWindow", str(mqtt_pass), None))
            self.ui.MQTTPassEdit.textChanged.connect(self.mqtt_pass_changed)

            self.ui.MQTTTestButton.clicked.connect(self.start_mqtt)

            ## ==> ADD NEW WAYPOINT
            self.ui.pushButton_add_waypoint.clicked.connect(lambda: F.newWaypoint(q))

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

        def opentrack_ip_changed(self, text):
            global opentrack_ip
            config.set('opentrack', 'ip', str(text))
            self.write_config()
            opentrack_ip = text

        def opentrack_port_changed(self, text):
            global opentrack_port
            config.set('opentrack', 'port', str(text))
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
                print(x,y,z)
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
                self.ui.controllerSelection.setItemText(0, QCoreApplication.translate("MainWindow", u"(please select your controller)", None))
                self.ui.controllerSelection.setCurrentIndex(0)

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

            self.repopulate_controllers_dropdown()


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

            self.repopulate_controllers_dropdown()

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

            self.repopulate_controllers_dropdown()

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
                        config.set('controllers', 'xboxone_id', controller_id)
                        config.set('controllers', 'xboxone_name', controller_name)
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
                        config.set('controllers', 'spacemouse_id', controller_id)
                        config.set('controllers', 'spacemouse_name', controller_name)
                        joystick = controller_id

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

        def joystick_thread(self):


            while joystick_loop:
                global x
                global y
                global z
                global yaw
                global pitch
                global roll
                global controllerTest
                global camera_path_thread
                global camera_path_loop
                global tts
                global controllers_count
                global joystickNames
                global joystickUids
                global joystickIds
                global joystick
                global gamepad

                controller_id = -1

                time.sleep(0.005) #200 fps (ish)

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

                    if gamepad != None:

                        try:
                            for c in range(pygame.joystick.get_count()):
                                if gamepad == pygame.joystick.Joystick(c).get_guid():
                                    controller_id = c
                                    break
                        except pygame.error as message:
                            print(message)

                        if controller_id >= 0:

                            try:
                                x = increment(x, - pygame.joystick.Joystick(controller_id).get_axis(0) - pygame.joystick.Joystick(controller_id).get_hat(0)[0]/4)
                                z = increment(z, pygame.joystick.Joystick(controller_id).get_axis(1) - pygame.joystick.Joystick(controller_id).get_hat(0)[1]/4)
                                y = increment(y, (pygame.joystick.Joystick(controller_id).get_axis(4)+1 - (pygame.joystick.Joystick(controller_id).get_axis(5)+1))/2)
                                yaw = increment(yaw, pygame.joystick.Joystick(controller_id).get_axis(2))
                                pitch = increment(pitch, pygame.joystick.Joystick(controller_id).get_axis(3))

                                #x = increment(x, - pygame.joystick.Joystick(controller_id).get_hat(0)[0]/4)
                                #z = increment(z, - pygame.joystick.Joystick(controller_id).get_hat(0)[1]/4)


                                if pygame.joystick.Joystick(controller_id).get_button(4):
                                    roll = roll + 0.005

                                if pygame.joystick.Joystick(controller_id).get_button(5):
                                    roll = roll - 0.005

                                for event in pygame.event.get():
                                    if event.type == pygame.JOYBUTTONDOWN:
                                        if pygame.joystick.Joystick(controller_id).get_button(0):
                                            camera_path_loop = False
                                            q.put('waypoint added')
                                            print('A')
                                        if pygame.joystick.Joystick(controller_id).get_button(1):
                                            camera_path_loop = False
                                            q.put('waypoints deleted')
                                            print('B')
                                        if pygame.joystick.Joystick(controller_id).get_button(2):
                                            camera_path_loop = False
                                            q.put('going home')
                                            print('X')
                                        if pygame.joystick.Joystick(controller_id).get_button(3):
                                            if camera_path_thread and camera_path_thread.is_alive():
                                                camera_path_loop = False
                                                q.put('cancelled')
                                                camera_path_thread.join()
                                            else:
                                                if camera_path_thread and camera_path_thread.is_alive():
                                                    camera_path_loop = False
                                                    camera_path_thread.join()
                                                camera_path_loop = True
                                                camera_path_thread = Thread(target=do_camera_path, args=("Thread",))
                                                camera_path_thread.start()
                                            print('Y')
                                        if pygame.joystick.Joystick(controller_id).get_button(6):
                                            print('window')
                                        if pygame.joystick.Joystick(controller_id).get_button(7):
                                            print('settings')
                                        if pygame.joystick.Joystick(controller_id).get_button(8):
                                            print('left down')
                                        if pygame.joystick.Joystick(controller_id).get_button(9):
                                            print('right down')
                                        if pygame.joystick.Joystick(controller_id).get_button(10):
                                            print('xbox')
                                        if pygame.joystick.Joystick(controller_id).get_button(11):
                                            print('share')

                            except pygame.error as message:
                                print("Cannot read gamepad ID " + str(controller_id))
                                print(message)
                                #raise SystemExit(message)

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
                    self.F.updateOpenTrack(x,y,z,yaw,pitch,roll)

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
                self.F.newWaypoint(q)
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
            stop_tts()
            self.F.stop_opentrack()
            self.F.stop_hotkey()
            print('closing')

def do_camera_path(threadname):
    global camera_path_loop
    n = 3

    while camera_path_loop:
        match n:
            case 3:
                q.put('starting in 3')
                time.sleep(1.8)
            case 2:
                q.put('2')
                time.sleep(1)
            case 1:
                q.put('1')
                break
        n = n - 1



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




#def start_joystick():
#    global joystick_loop
#    global joystick_value
#    joystick_loop = True
#    if not joystick_value.is_alive():
#        joystick_value = Thread(target=joystick_thread, args=("Thread",))
#        joystick_value.start()

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
    print("- opentrack Options > Filter is set to 1°/0.1mm Smoothing and no Deadzone")
    print("- opentrack is started with 'UDP over network' input on port 4242")
    print("- Star Citizen is running in windowed mode")
    print("- TrackIR v5 is closed\n")

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

    if not config.has_section('opentrack'):
        config.add_section('opentrack')

    if config.has_option('opentrack', 'ip'):
        opentrack_ip = config.get('opentrack', 'ip')
    if config.has_option('opentrack', 'port'):
        opentrack_port = config.get('opentrack', 'port')

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



