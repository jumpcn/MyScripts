import win32api, win32con
import time
import ImageGrab
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


while True:
	time.sleep(0.02)
	image = ImageGrab.grab()
	if image.getpixel((955,598)) == (255, 255, 0):
		click(955,598)
		print "click"
	del image
