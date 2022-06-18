## ==> GUI FILE
from main import *
import pygame
import socket, struct
import ctypes, ctypes.wintypes
from pynput.mouse import Controller
import numpy as np

print('NAME', __name__)

WM_QUIT = 0x0012

class Functions(MainWindow):

    def wait_for_hotkey_thread(self, threadname):
        print('[ALT]+[Num+] hotkey registration')
        ctypes.windll.user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_ADD)
        try:
            msg = ctypes.wintypes.MSG()
            while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    if self.window.windowState() == Qt.WindowMinimized:
                        #for whatever reason this breaks with fullscreen (and minimized from fullscreen)
                        self.window.showNormal()
                        time.sleep(0.2)
                    win32gui.SetForegroundWindow(win32gui.FindWindowEx(0,0,0, "CamBot 6D"))
                ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
                ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))
        except:
            print('hotkey FAILED')

    def send_to_opentrack_thread(self, threadname):
        while self.sendToOpenTrack:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                self.clock.tick(200) #200 fps
                position = [self.x, self.y, self.z, self.yaw, self.pitch, self.roll]
                struct.pack_into('dddddd', self.buf, 0, *position)
                try:
                    sock.sendto(self.buf, self.address)
                except:
                    print("socket error")

    def __init__(self, window, UIFunctions):

        self.UIFunctions = UIFunctions

        self.window = window
        self.clock = pygame.time.Clock()

        self.mouse = Controller()

        self.points = np.empty((0,6), float)


        self.sendToOpenTrack = True
        self.waitForHotkeyTid = None

        ###
        # [ALT]+[Num+] hotkey registration
        #ctypes.windll.user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_ADD)

        #finally:
        #    ctypes.windll.user32.UnregisterHotKey(None, 1)
        ###

        self.config_input_method = "keyboard"
        self.config_mouse_sensitivity = 0.01
        self.config_keyboard_sensitivity_t = 0.05
        self.config_keyboard_sensitivity_r = 0.2

        self.speed_modifier = 1

        self.send_to_opentrack = ''
        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0
        self.pitch = 0
        self.roll = 0
        self.address = ("127.0.0.1", 4242)
        self.buf = bytearray(8 * 6)

        #should be last in __init__
        self.send_to_opentrack = Thread(target=self.send_to_opentrack_thread, args=("Thread",))
        self.send_to_opentrack.start()

    def stop_opentrack(self):
        print('stopping opentrack')
        self.sendToOpenTrack = False
        if self.send_to_opentrack and self.send_to_opentrack.is_alive():
            self.send_to_opentrack.join()

    def start_hotkey(self):
        self.wait_for_hotkey = Thread(target=self.wait_for_hotkey_thread, args=("Thread",))
        #self.wait_for_hotkey.daemon = True
        self.wait_for_hotkey.start()
        self.waitForHotkeyTid = self.wait_for_hotkey.native_id

    def stop_hotkey(self):
        print('stopping hotkey')
        ctypes.windll.user32.PostThreadMessageW(self.waitForHotkeyTid, WM_QUIT, 0, 0)
        ctypes.windll.user32.UnregisterHotKey(None, 1)

    def checkMouseKeyboard(self, queue):

        mousePosition = self.mouse.position

        backdrop = pygame.image.load('images/background-01.png')
        pygame.display.init()

        #mouse_old = mouse.position
        #mouse_new = mouse_old

        #while True:
        #    mouse_old = mouse_new
        #    mouse_new = mouse.position
        #    diff = tuple(map(lambda d1, d2: d2 - d1, mouse_old, mouse_new))
        #    print(diff)

        #    time.sleep(0.01)

        #self.showMinimized()

        #stop joystick_loop
        #stop_joystick()

        run = True
        world = pygame.display.set_mode((400,400), flags=pygame.SHOWN | pygame.NOFRAME, display=display)

        # Create layered window
        hwnd = pygame.display.get_wm_info()["window"]

        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
        # Set window transparency color
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency), 220, win32con.LWA_ALPHA)
        self.window.showMinimized()

        world.fill(transparency)
        backdropbox = world.get_rect()
        world.blit(backdrop, backdropbox)
        pygame.display.update()
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

        while run:

            keys = pygame.key.get_pressed()

            if (keys[pygame.K_SPACE]):
                sprint = 3



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    #pygame.display.quit()
                    #pygame.display.init()
                    #pygame.display.set_mode((400, 400), flags=pygame.HIDDEN | pygame.NOFRAME, display=display)
                    pygame.display.quit()
                    pygame.display.init()
                    self.window.showNormal()
                    #start joystick_loop
                    #start_joystick()
                    self.mouse.position = mousePosition
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        queue.put('canceled')
                        run = False
                        #pygame.display.quit()
                        #pygame.display.init()
                        #pygame.display.set_mode((400, 400), flags=pygame.HIDDEN | pygame.NOFRAME,display=display)
                        pygame.display.quit()
                        pygame.display.init()
                        self.window.showNormal()
                        #start joystick_loop
                        #start_joystick()
                        self.mouse.position = mousePosition
                    elif event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                        run = False
                        #pygame.display.set_mode((400, 400), flags=pygame.HIDDEN | pygame.NOFRAME,display=display)
                        pygame.display.quit()
                        pygame.display.init()
                        self.window.showNormal()
                        #start joystick_loop
                        #start_joystick()
                        self.mouse.position = mousePosition
                elif event.type == pygame.MOUSEMOTION:
                    #mouse_position = pygame.mouse.get_pos()
                    mouse_position = pygame.mouse.get_rel()
                    self.yaw += mouse_position[0] * self.config_mouse_sensitivity * self.speed_modifier
                    self.pitch -= mouse_position[1] * self.config_mouse_sensitivity * self.speed_modifier
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: #left click
                        print('save point')
                        run = False
                        pygame.display.quit()
                        pygame.display.init()
                        self.window.showNormal()
                        self.saveWaypoint(queue)
                        self.mouse.position = mousePosition
                    elif event.button == 3: #right click
                        print('hide overlay')
                    elif event.button == 4: #scroll up
                        print('speed up')
                        if not self.speed_modifier * 2 >= 16:
                            self.speed_modifier = self.speed_modifier * 2
                    elif event.button == 5: #scroll down
                        print('speed down')
                        if not self.speed_modifier / 2 <= 0.0625:
                            self.speed_modifier = self.speed_modifier / 2

            self.x += (keys[pygame.K_a] - keys[pygame.K_d]) * self.config_keyboard_sensitivity_t * self.speed_modifier
            self.z -= (keys[pygame.K_w] - keys[pygame.K_s]) * self.config_keyboard_sensitivity_t * self.speed_modifier
            self.y += (keys[pygame.K_SPACE] - keys[pygame.K_LCTRL]) * self.config_keyboard_sensitivity_t * self.speed_modifier
            self.roll += (keys[pygame.K_q] - keys[pygame.K_e]) * self.config_keyboard_sensitivity_r * self.speed_modifier

            self.clock.tick(120) #120 fps

            #print(self.x,self.y,self.z,self.yaw,self.pitch,self.roll)

            #print(x,y,z,yaw,pitch,roll)

            #pygame.event.pump()

    def gamePadIncrement(self, old, new):
        if abs(new) < 0.05:
            return old
        else:
            return old + new/100

    def updateOpenTrack(self,x,y,z,yaw,pitch,roll):

        self.x = x * 2
        self.y = y * 2
        self.z = z * 2
        self.yaw = yaw * 10
        self.pitch = pitch * 10
        self.roll = roll * 20

    def newWaypoint(self, queue):
        if self.config_input_method == "keyboard":
            self.checkMouseKeyboard(queue)

    def saveWaypoint(self, queue):
        queue.put('waypoint added')

        table = self.window.ui.tableWidget_waypoints
        rowPosition = table.rowCount()
        #atualTime = globals()['atual_render_time']

        #self.q.put('waypoint added')

        table.insertRow(rowPosition)

        #time = str(atualTime)
        deleteButton = QPushButton()
        deleteButton.clicked.connect(lambda: self.deleteClicked(deleteButton))
        deleteButton.setStyleSheet(Style.style_bt_delet_row)
        icon_bt_del = QIcon()
        icon_bt_del.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(16,16), QIcon.Normal, QIcon.Off)
        deleteButton.setIcon(icon_bt_del)
        deleteButton.setMaximumSize(QSize(40, 20))

        table.setItem(rowPosition, 0, QTableWidgetItem('X=' + str(np.round(self.x, 1)) + ' | ' + 'Y=' + str(np.round(self.y, 1)) + ' | ' + 'Z=' + str(np.round(self.z, 1)) + ' | ' + 'Yaw=' + str(np.round(self.yaw, 1)) + ' | ' + 'Pitch=' + str(np.round(self.pitch, 1)) + ' | ' + 'Roll=' + str(np.round(self.roll, 1))))
        table.setItem(rowPosition, 1, QTableWidgetItem('Point ' + str(rowPosition + 1)))
        table.setCellWidget(rowPosition, 2, deleteButton)
        table.setRowHeight(rowPosition, 20)

        self.points = np.concatenate((self.points, [[self.x, self.y, self.z, self.yaw, self.pitch, self.roll]]))
        print('POINTS', self.points)


        if not rowPosition:
            Functions.toggleTable(self)
            QtCore.QTimer.singleShot(350, lambda: self.window.ui.tableWidget_waypoints.show())


    ## ==> TOGGLE TABLE WIDGET
    ########################################################################
    def toggleTable(self):
        height = self.window.ui.frame_div_table_widget_M1.height()
        maxExtend = 205
        standard = 58

        # SET MAX WIDTH
        if height == 58:
            heightExtended = maxExtend
            self.window.ui.label_help_info.hide()
        else:
            heightExtended = standard

        self.animation = QPropertyAnimation(self.window.ui.frame_div_table_widget_M1, b"maximumHeight")
        self.animation.setDuration(600)
        self.animation.setStartValue(height)
        self.animation.setEndValue(heightExtended)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    ########################################################################
    ## TABLE WIDGET ==> FUNCTIONS
    ########################################################################
    def deleteClicked(self, button):

        table = self.window.ui.tableWidget_waypoints
        count = table.rowCount()

        if button:
            row = self.window.ui.tableWidget_waypoints.indexAt(button.pos()).row()
            self.window.ui.tableWidget_waypoints.removeRow(row)

        if count == 1:
            self.toggleTable()
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.tableWidget_waypoints.hide())
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.label_help_info.show())

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.window.show()
        ## ==> END ##
