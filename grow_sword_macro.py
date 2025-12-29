import pyautogui
import pygetwindow as gw
import pyperclip
import time


TargetLevel=13
ROOM_NAME = "검키우기매크로"
TARGET_TEXT = f"@사용자 〖✨강화 성공✨ +{TargetLevel-1} → +{TargetLevel}〗"
SSIBAL_TEXT = f"골드가 부족해. 골드를 더 모으고 오시게나."
DELAY = 3
last_chat = ""


def send_msg(win, text):
    pyperclip.copy(text)
    pyautogui.click(win.left + 100, win.bottom - 150)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.press('enter')
    pyautogui.press('enter')

def send_msg2(win): #@플레이봇 강화
    pyautogui.click(win.left + 100, win.bottom - 150)
    pyperclip.copy("@플레이봇")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.25)
    pyautogui.press('space')
    pyperclip.copy("강화")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.25)
    pyautogui.press('enter')
    pyautogui.press('enter')


def run_macro(mode):
    global last_chat

    try:
        target_win = gw.getWindowsWithTitle(ROOM_NAME)
        if not target_win:
            print(f"오류: '{ROOM_NAME}' 창을 찾을 수 없습니다.")
            return
        
        win = target_win[0]
        if win.isMinimized: win.restore()
        win.activate()

        inputSiphim = 0

        while True:
            pyautogui.click(win.left + 100, win.top + 150)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            
            current_chat = pyperclip.paste()[-500:]
            last_command_pos = current_chat.rfind("/강화")
            last_bot_pos = current_chat.rfind("〖")
            
            if (current_chat != last_chat and last_command_pos < last_bot_pos or inputSiphim>3):
                last_chat = current_chat
                inputSiphim = 0

                if SSIBAL_TEXT in current_chat:
                    break
                elif TARGET_TEXT in current_chat:
                    if (mode == "sell"):
                        send_msg(win, "/판매")
                    elif(mode == "reinforce"):
                        break
                else:
                    send_msg(win, "/강화")

            time.sleep(DELAY)
            inputSiphim += 1

    except Exception as e:
        print(f"오류 발생: {e}")



if __name__ == "__main__":
    run_macro("sell")