import keyboard as kb


def getKeyboardInput():
    hook_on_press_w = kb.on_press_key('w', lambda e: print("You pressed:", e.name), True)
    hook_on_press_a = kb.on_press_key('a', lambda e: print(e.name), True)
    hook_on_press_s = kb.on_press_key('s', lambda e: print(e.name), True)
    hook_on_press_d = kb.on_press_key('d', lambda e: print(e.name), True)
    hook_on_press_enter = kb.on_press_key('enter', lambda e: exit, True)
    kb.wait('enter')
    kb.unhook_all()