## ==> GUI FILE
from CamBot6D import *
import pygame
import socket, struct
import ctypes, ctypes.wintypes
#from ctypes import *
from pynput.mouse import Controller
import numpy as np
from scipy import interpolate
import mmap
from dataclasses import dataclass
#from dataclasses import astuple
import XInput
import windows
import win32event

@dataclass
class FT_SharedMem:
    DataID: int
    CamWidth: int
    CamHeight: int
    Yaw: float
    Pitch: float
    Roll: float
    X: float
    Y: float
    Z: float
    RawYaw: float
    RawPitch: float
    RawRoll: float
    RawX: float
    RawY: float
    RawZ: float
    X1: float
    Y1: float
    X2: float
    Y2: float
    X3: float
    Y3: float
    X4: float
    Y4: float
    GameID: int
    table_ints_1: int
    table_ints_2: int
    GameID2: int


#    def __array__(self):
#        return np.array(astuple(self))

print('NAME', __name__)

WM_QUIT = 0x0012

class Functions(MainWindow):

    print('CONNECTED', XInput.get_connected())

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

    def send_to_freetrack_thread(self, threadname):

        loop_delta = 1./self.fps
        current_time = target_time = time.perf_counter()

        ft_SharedMem_bytes = 92
        ft_heap_bytes = 92 + 4 + 8 + 4

        # structure of mmap_mutex
        # typedef struct FTHeap__ {
        #     FTData data;
        #     int32_t GameID;
        #     union
        #     {
        #         unsigned char table[8];
        #         int32_t table_ints[2];
        #     };
        #     int32_t GameID2;
        # } volatile FTHeap;

        #try:
        #create Non-Persisted Memory-Mapped File
        mmap_sharedmem = mmap.mmap(-1, ft_heap_bytes, 'FT_SharedMem', access=mmap.ACCESS_DEFAULT,offset=0)
        #print('MMAP', mmap_sharedmem)

#####
        """
        PAGE_READWRITE = 0x04
        CreateFileMappingA = ctypes.windll.kernel32.CreateFileMappingA
        CreateFileMappingA.argtypes = [ctypes.wintypes.HANDLE, ctypes.c_void_p, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD, ctypes.wintypes.LPCSTR]
        mmap_sharedmem_windll = CreateFileMappingA(-1, None, PAGE_READWRITE, 0, ft_SharedMem_bytes, b'FT_SharedMem')
        if (mmap_sharedmem_windll == 0):
            raise ctypes.WinError()
        print('MMAP_DLL', mmap_sharedmem_windll)


        #create ipc_heap
        FILE_MAP_WRITE = 2
        MapViewOfFile = ctypes.windll.kernel32.MapViewOfFile
        MapViewOfFile.restype = ctypes.POINTER(ctypes.c_char)
        ipc_heap = MapViewOfFile(mmap_sharedmem_windll, FILE_MAP_WRITE, 0, 0, ft_heap_bytes)
        if ipc_heap == 0:
            raise ctypes.WinError()

        #create ipc_mutex
        ipc_mutex = ctypes.windll.kernel32.CreateMutexA(None, False, 'FT_SharedMem')
        if (ipc_mutex == 0):
            raise ctypes.WinError()
        print(ipc_mutex)

        #except Exception as e:
        #    print('ERROR', e)
        """
#####

        while self.sendToFreeTrack:

#            try:
#                with mmap.mmap(-1, ft_heap_bytes, 'FT_SharedMem', access=mmap.ACCESS_DEFAULT,offset=0) as mmap_mutex:
#                    print(mmap_mutex.read())
#            except Exception as e:
#                print('ERROR', e)

#####

            #get data from ipc_mutex
#            if ipc_mutex:
#                wait_result = win32event.WaitForSingleObject(ipc_mutex, 16)
#                if (wait_result == win32event.WAIT_OBJECT_0):
                    #print(ipc_heap)
                    #data = struct.unpack('Iiiffffffffffffffffffffiiii', ipc_heap)
                    #pBuf_str = ctypes.cast(ipc_heap, ctypes.c_char_p)
                    #print(pBuf_str.value)
#                    print(ctypes.string_at(ipc_heap))
#                    ctypes.windll.kernel32.ReleaseMutex(ipc_mutex)
                    #print(len(ipc_heap))
            #    shmem.write(szMsg1)
            #    while (shmem.tell() != SHMEMSIZE):
            #        shmem.write_byte(" ")
            #    shmem.seek(0)
            #    print "WROTE in FIRST process: ", szMsg1
            #    win32event.ReleaseMutex(hMutex)

            #getGameData
            #717;Star Citizen;FreeTrack20;V170;;;3450;02CDF4CE4E343EC6B4A200

#####

            previous_time, current_time = current_time, time.perf_counter()
            time_delta = current_time - previous_time


            if self.robot == None:
                position = [self.x, self.y, self.z, self.yaw, self.pitch, self.roll]
            else:
                #print('SIZE', self.robot[0].size, 'TICK', self.clock.tick_busy_loop())
                #print('FPS', self.fps)
                if self.robot[0].size > 1:
                    #print('SIZE', self.robot[0].size, 'X:', self.robot[0][0])
                    position = [self.robot[0][0], self.robot[1][0], self.robot[2][0], self.robot[3][0], self.robot[4][0], self.robot[5][0]]
                    self.robot = [np.delete(self.robot[0], 0), np.delete(self.robot[1], 0), np.delete(self.robot[2], 0), np.delete(self.robot[3], 0), np.delete(self.robot[4], 0), np.delete(self.robot[5], 0)]
                else:
                    print('FINAL')
                    self.x = self.robot[0][0]
                    self.y = self.robot[1][0]
                    self.z = self.robot[2][0]
                    self.yaw = self.robot[3][0]
                    self.pitch = self.robot[4][0]
                    self.roll = self.robot[5][0]
                    self.robot = None


            data = struct.unpack('Iiiffffffffffffffffffffiiii', mmap_sharedmem)

            TFreeTrackData = FT_SharedMem(*data)
            TFreeTrackData.DataID = TFreeTrackData.DataID + 1
            TFreeTrackData.CamWidth = 100
            TFreeTrackData.CamHeight = 250
            TFreeTrackData.X = position[0] #-500..500
            TFreeTrackData.Y = position[1]
            TFreeTrackData.Z = position[2]
            TFreeTrackData.Yaw = position[3]
            #print(TFreeTrackData.Yaw)
            TFreeTrackData.Pitch = position[4]
            TFreeTrackData.Roll = position[5]

            """
            TFreeTrackData.RawYaw = position[0]
            TFreeTrackData.RawPitch = position[1]
            TFreeTrackData.RawRoll = position[2]
            TFreeTrackData.RawX = position[3]
            TFreeTrackData.RawY = position[4]
            TFreeTrackData.RawZ = position[5]



            TFreeTrackData.X1 = 100.
            TFreeTrackData.Y1 = 200.
            TFreeTrackData.X2 = 300.
            TFreeTrackData.Y2 = 200.
            TFreeTrackData.X3 = 300.
            TFreeTrackData.Y3 = 100.
            """

            #STAR CITIZEN
            #No;Game Name;Game protocol;Supported since;Verified;By;INTERNATIONAL_ID;FTN_ID
            #717;Star Citizen;FreeTrack20;V170;;;3450;02CDF4CE4E343EC6B4A200
            #3450 -187806156 1053209762 3450

            #set GameID2 == GameID if Star Citizen is launched
            GameID = TFreeTrackData.GameID2
            GameInt1 = TFreeTrackData.table_ints_1
            GameInt2 = TFreeTrackData.table_ints_2
            if TFreeTrackData.GameID != TFreeTrackData.GameID2:
                if TFreeTrackData.GameID == 3450:
                    GameID = 3450
                    GameInt1 = -187806156
                    GameInt2 = 1053209762
                if TFreeTrackData.GameID == 1901:
                    GameID = 1901

            print (TFreeTrackData.GameID, TFreeTrackData.table_ints_1, TFreeTrackData.table_ints_2, TFreeTrackData.GameID2)

            data = struct.pack('Iiiffffffffffffffffffffiiii', TFreeTrackData.DataID, TFreeTrackData.CamWidth, TFreeTrackData.CamHeight, TFreeTrackData.Yaw, TFreeTrackData.Pitch, TFreeTrackData.Roll, TFreeTrackData.X, TFreeTrackData.Y, TFreeTrackData.Z, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, TFreeTrackData.GameID, GameInt1, GameInt2, GameID )
            mmap_sharedmem.seek(0)
            mmap_sharedmem.write(data)


            #self.fps rate limit
            target_time += loop_delta
            sleep_time = target_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)

                #120 fps minus 0.5 milliseconds (time for the loop to execute, rought guess)
                #time.sleep(1/self.fps - 0.0005) #delay for one frame at self.fps (might execute slightly slower: 8 ms + loop time of 0.5 ms - hence subtraction of 0.5ms)
                #self.clock.tick_busy_loop(self.fps) #max FPS - but 6.5% CPU usage

        #set everything to zero on exit
        GameID = 0
        data = struct.pack('Iiiffffffffffffffffffffiiii', 0, 0, 0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, .0, 0, 0, 0, 0 )
        mmap_sharedmem.seek(0)
        mmap_sharedmem.write(data)


    def __init__(self, window, UIFunctions):

        self.UIFunctions = UIFunctions

        self.window = window
        #self.clock = pygame.time.clock()

        self.mouse = Controller()

        self.points = np.empty((0,6), float)

        self.robot = None

        self.fps = 120

        self.sendToFreeTrack = True
        self.waitForHotkeyTid = None

        ###
        # [ALT]+[Num+] hotkey registration
        #ctypes.windll.user32.RegisterHotKey(None, 1, win32con.MOD_ALT, win32con.VK_ADD)

        #finally:
        #    ctypes.windll.user32.UnregisterHotKey(None, 1)
        ###

        self.config_mouse_sensitivity = 0.01
        self.config_keyboard_sensitivity_t = 0.05
        self.config_keyboard_sensitivity_r = 0.2

        self.speed_modifier = 1

        self.send_to_freetrack = ''
        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0
        self.pitch = 0
        self.roll = 0

        #should be last in __init__
        self.send_to_freetrack = Thread(target=self.send_to_freetrack_thread, args=("Thread",))
        self.send_to_freetrack.start()

    def stop_freetrack(self):
        print('stopping freetrack')
        self.sendToFreeTrack = False
        if self.send_to_freetrack and self.send_to_freetrack.is_alive():
            self.send_to_freetrack.join()

    def start_hotkey(self):
        self.wait_for_hotkey = Thread(target=self.wait_for_hotkey_thread, args=("Thread",))
        #self.wait_for_hotkey.daemon = True
        self.wait_for_hotkey.start()
        self.waitForHotkeyTid = self.wait_for_hotkey.native_id

    def stop_hotkey(self):
        print('stopping hotkey')
        try:
            ctypes.windll.user32.PostThreadMessageW(self.waitForHotkeyTid, WM_QUIT, 0, 0)
            ctypes.windll.user32.UnregisterHotKey(None, 1)
        except Exception as error:
            print('Error stopping hotkey', error)

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

        loop_delta = 1./self.fps
        current_time = target_time = time.perf_counter()

        while run:

            previous_time, current_time = current_time, time.perf_counter()
            time_delta = current_time - previous_time

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

            #self.fps rate limit
            target_time += loop_delta
            sleep_time = target_time - time.perf_counter()
            if sleep_time > 0:
                time.sleep(sleep_time)

            #self.clock.tick(120) #does not work in compiled version. tick_busy_loop does work but uses too many CPU resources.
            #time.sleep(1/self.fps - 0.0005) #120 fps minus 0.5 milliseconds (time for the loop to execute, rought guess)

            #print(self.x,self.y,self.z,self.yaw,self.pitch,self.roll)

            #print(x,y,z,yaw,pitch,roll)

            #pygame.event.pump()

    def gamePadIncrement(self, old, new):
        if abs(new) < 0.05:
            return old
        else:
            return old + new/100

    def updateFreeTrack(self,x,y,z,yaw,pitch,roll):
        if self.robot == None:
            self.x = x
            self.y = y
            self.z = z
            self.yaw = yaw
            self.pitch = pitch
            self.roll = roll

    def calculateSpline(self, path, duration):

        frames = duration * self.fps

        print('FRAMES', frames)

        k_limit = 2 # todo: Degree of the spline. Cubic splines are recommended. Even values of k should be avoided especially with a small s-value. 1 <= k <= 5, default is 3. !!!
        pathT = path.T #transpose array: all x values in one array etc

        #print(path)
        #print(pathT)

        if (len(path) < 3):
            k_limit = 1
        elif (len(path) < 4):
            k_limit = 2 #2 todo: make this selectable

        print('klimit', k_limit)

        try:
            tck, u = interpolate.splprep([pathT[0],pathT[1],pathT[2],pathT[3],pathT[4],pathT[5]], s=0, k=k_limit)

            # SPATIAL INTERPOLATION: linear, quadratic, cubic

            # TEMPORAL INTERPOLATION: auto
            u_fine = np.linspace(0,1,int(frames))

            # TEMPORAL INTERPOLATION: equidistant
            u_fine = np.array([.0]) #first element of array (0 = start point)

            for i in range(len(u)):
                if i != 0:
                    section = np.linspace(u[i-1],u[i],int(frames / (len(u) - 1) )) #create array with same number of elements between u points
                    section = np.delete(section, 0) #remove first element of section
                    u_fine = np.append(u_fine, section)



            x_fine, y_fine, z_fine, yaw_fine, pitch_fine, roll_fine = interpolate.splev(u_fine, tck) #todo: u instead of u_fine? !!!
            return [x_fine, y_fine, z_fine, yaw_fine, pitch_fine, roll_fine]
        except Exception as error:
            print('Splite interpolation error', error)
            return np.empty((0,6), float)

    def showForeground(self):
        if self.window.windowState() == Qt.WindowMinimized:
            #for whatever reason this breaks with fullscreen (and minimized from fullscreen)
            self.window.showNormal()
            time.sleep(0.2)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(win32gui.FindWindowEx(0,0,0, "CamBot 6D"))

    def newWaypoint(self, queue, config):
        if config.has_option('controllers', 'type'):
            controller = config.get('controllers', 'type')
        else:
            controller = keyboardandmouse

        if controller == "keyboardandmouse":
            self.robot = None
            self.checkMouseKeyboard(queue)
        else:
            if self.robot == None:
                self.saveWaypoint(queue)

    def deleteAll(self, queue, config):
        queue.put('all waypoints deleted')
        self.points = np.empty((0,6), float)

        table = self.window.ui.tableWidget_waypoints
        count = table.rowCount()

        if count > 0:
            while count >= 0:
              self.window.ui.tableWidget_waypoints.removeRow(count)
              count -= 1

            self.toggleTable(False)
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.tableWidget_waypoints.hide())
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.label_help_info.show())



    def pathForward(self, queue, config):
        duration = 3.0
        if config.has_option('speed', 'path'):
            duration = config.getfloat('speed', 'path')

        path = self.points

        motion = None

        try:
            #go to starting point
            spline = self.twoPointSpline([self.x, self.y, self.z, self.yaw, self.pitch, self.roll], path[0], 0.5)
            motion = spline

            #wait 3 seconds
            wait = np.ones(3 * self.fps)
            print("WAIT", len(wait))
            motion = [np.append(motion[0], wait * path[0][0]), np.append(motion[1], wait * path[0][1]), np.append(motion[2], wait * path[0][2]), np.append(motion[3], wait * path[0][3]), np.append(motion[4], wait * path[0][4]), np.append(motion[5], wait * path[0][5])]

            #do the motion
            spline = self.calculateSpline(path, duration)
            motion = [np.append(motion[0], spline[0]), np.append(motion[1], spline[1]), np.append(motion[2], spline[2]), np.append(motion[3], spline[3]), np.append(motion[4], spline[4]), np.append(motion[5], spline[5])]

            queue.put('starting in three,. two,. one.')

            self.robot = motion

        except Exception as error:
            queue.put('error: unable to calculate camera path')


    def pathBackward(self, queue, config):
        duration = 3.0
        if config.has_option('speed', 'path'):
            duration = config.getfloat('speed', 'path')

        path = np.flipud(self.points)

        motion = None

        try:
            #go to starting point
            spline = self.twoPointSpline([self.x, self.y, self.z, self.yaw, self.pitch, self.roll], path[0], .5)
            motion = spline

            #wait 3 seconds
            wait = np.ones(3 * self.fps)
            motion = [np.append(motion[0], wait * path[0][0]), np.append(motion[1], wait * path[0][1]), np.append(motion[2], wait * path[0][2]), np.append(motion[3], wait * path[0][3]), np.append(motion[4], wait * path[0][4]), np.append(motion[5], wait * path[0][5])]

            #do the motion
            spline = self.calculateSpline(path, duration)
            motion = [np.append(motion[0], spline[0]), np.append(motion[1], spline[1]), np.append(motion[2], spline[2]), np.append(motion[3], spline[3]), np.append(motion[4], spline[4]), np.append(motion[5], spline[5])]

            queue.put('starting in three,. two,. one.')

            self.robot = motion

        except Exception as error:
            queue.put('error: unable to calculate camera path')

    def twoPointSpline(self, position_from, position_to, duration):
        if position_from[0] != position_to[0] or position_from[1] != position_to[1] or position_from[2] != position_to[2] or position_from[3] != position_to[3] or position_from[4] != position_to[4] or position_from[5] != position_to[5]:
            path = np.empty((0,6), float)
            path = np.concatenate((path, [position_from]))
            path = np.concatenate((path, [position_to]))
            return self.calculateSpline(path, duration)
        else:
            return np.empty((0,6), float)

    def goHome(self, queue, config):
        duration = 1 #seconds
        position_from = [self.x, self.y, self.z, self.yaw, self.pitch, self.roll]
        position_to = [0, 0, 0, 0, 0, 0]
        if self.x != position_to[0] or self.y != position_to[1] or self.z != position_to[2] or self.yaw != position_to[3] or self.pitch != position_to[4] or self.roll != position_to[5]:
            queue.put('going home')
            path = np.empty((0,6), float)
            path = np.concatenate((path, [position_from]))
            path = np.concatenate((path, [position_to]))
            self.robot = self.calculateSpline(path, duration)
        else:
            queue.put('already home')
            self.robot = None


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
            Functions.toggleTable(self, True)
            QtCore.QTimer.singleShot(350, lambda: self.window.ui.tableWidget_waypoints.show())

    ## ==> TOGGLE TABLE WIDGET
    ########################################################################
    def toggleTable(self, expand):
        height = self.window.ui.frame_div_table_widget_M1.height()
        maxExtend = 205
        standard = 58

        # SET MAX WIDTH
        if expand:
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
            self.toggleTable(False)
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.tableWidget_waypoints.hide())
            QtCore.QTimer.singleShot(600, lambda: self.window.ui.label_help_info.show())

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.window.show()
        ## ==> END ##
