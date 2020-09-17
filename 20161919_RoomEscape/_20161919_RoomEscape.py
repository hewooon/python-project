from bangtal import *
 
scene1 = Scene("room1", "Images/배경-1.png")
scene2 = Scene("room2", "Images/배경-2.png")

door1 = Object("Images/문-오른쪽-닫힘.png")
door1.locate(scene1,800,270)
door1.show()

keypad = Object("Images/키패드.png")
keypad.setScale(2)
keypad.locate(scene1,850,420)
keypad.show()

flash = Object("Images/손전등.png")
flash.setScale(0.6)
flash.locate(scene1,150,570)
flash.show()

desk = Object("Images/책상.png")
desk.setScale(0.25)
desk.locate(scene1,200,180)
desk.show()

drawer = Object("Images/서랍장.png")
drawer.setScale(3)
drawer.locate(scene1,250,130)

battery = Object("Images/건전지.png")
battery.setScale(1.2)
battery.locate(scene1,400,200)

flashlight = Object("Images/켜진 손전등.png")
flashlight.defineCombination(flash,battery)

switch = Object("Images/스위치.png")
switch.setScale(2)
switch.locate(scene1,100,600)
switch.show()

hint = Object("Images/힌트.png")
hint.locate(scene1,150,-120)

bookshelf = Object("Images/책장.png")
bookshelf.setScale(1.3)
bookshelf.locate(scene1,750,200)
bookshelf.show()

new_bookshelf = Object("Images/책 빠진 책장.png")
new_bookshelf.setScale(1.3)

book = Object("Images/책.png")
book.setScale(0.3)
book.locate(scene1,700,100)

openbook = Object("Images/열린 책.png")
openbook.setScale(0.3)
openbook.locate(scene1,720,120)

door2 = Object("Images/문-왼쪽-열림.png")
door2.locate(scene2,320,270)
door2.show()

door3 = Object("Images/문-오른쪽-닫힘.png")
door3.locate(scene2,910,270)
door3.show()

cabinet = Object("Images/닫힌 캐비닛.png")
cabinet.setScale(0.8)
cabinet.locate(scene2,50,150)
cabinet.show()

opencabinet = Object("Images/열린 캐비닛.png")
opencabinet.setScale(0.8)
opencabinet.locate(scene2,50,150)

knife = Object("Images/커터칼.png")
knife.setScale(0.3)
knife.locate(scene2,80,350)

picture = Object("Images/그림.png")
picture.locate(scene2,700,500)
picture.show()

newpicture = Object("Images/찢어진 그림.png")
newpicture.locate(scene2,700,500)

safe = Object("Images/금고.png")
safe.setScale(0.3)
safe.locate(scene2,720,530)

key = Object("Images/열쇠.png")
key.setScale(0.3)
key.locate(scene2,760,550)

def flash_onMouseAction(x,y,action):
    flash.pick()
flash.onMouseAction = flash_onMouseAction

def desk_onMouseAction(x,y,action):
    drawer.show()
    battery.show()
desk.onMouseAction = desk_onMouseAction

def battery_onMouseAction(x,y,action):
    battery.pick()
battery.onMouseAction = battery_onMouseAction

def drawer_onMouseAction(x,y,action):
    drawer.hide()
    battery.hide()
drawer.onMouseAction = drawer_onMouseAction

switch.lighted = True
def switch_onMouseAction(x,y,action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene1.setLight(1)
        hint.hide()
    else:
        scene1.setLight(0.25)
        if flashlight.inHand():
            hint.show()
switch.onMouseAction = switch_onMouseAction

bookshelf.moved = False
def bookshelf_onMouseAction(x,y,action):
    if bookshelf.moved == False and action == MouseAction.DRAG_RIGHT:
        bookshelf.hide()
        new_bookshelf.locate(scene1,1000,150)
        new_bookshelf.show()
        book.show()
        bookshelf.moved = True
bookshelf.onMouseAction = bookshelf_onMouseAction

def book_onMouseAction(x,y,action):
    book.hide()
    openbook.show()
book.onMouseAction = book_onMouseAction

openbook.zoom = True
def openbook_onMouseAction(x,y,action):
    openbook.zoom = not openbook.zoom
    if openbook.zoom:
        openbook.setScale(0.3)
        openbook.locate(scene1,720,120)
    else:
        openbook.setScale(1.5)
        openbook.locate(scene1,500,100)
openbook.onMouseAction = openbook_onMouseAction

def keypad_onMouseAction(x,y,action):
    showKeypad("1298",door1)
keypad.onMouseAction = keypad_onMouseAction

door1.locked = True
door1.closed = True
def door1_onMouseAction(x,y,action):
    if door1.locked:
        showMessage("문이 잠겨있다.")
    elif door1.closed:
        keypad.hide()
        door1.setImage("Images/문-오른쪽-열림.png")
        door1.closed = False
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction

def door1_onKeypad():
    door1.locked = False
    showMessage("철커덕!!! 문이 열렸다.")
door1.onKeypad = door1_onKeypad

def door2_onMouseAction(x,y,action):
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

def cabinet_onMouseAction(x,y,action):
    cabinet.hide()
    opencabinet.show()
    knife.show()
cabinet.onMouseAction = cabinet_onMouseAction

def opencabinet_onMouseAction(x,y,action):
    opencabinet.hide()
    cabinet.show()
    knife.hide()
opencabinet.onMouseAction = opencabinet_onMouseAction

def knife_onMouseAction(x,y,action):
    knife.pick()
knife.onMouseAction = knife_onMouseAction

def picture_onMouseAction(x,y,action):
    if knife.inHand():
        picture.hide()
        newpicture.show()
        safe.show()
        key.show()
        door3.show()
picture.onMouseAction = picture_onMouseAction

def key_onMouseAction(x,y,action):
    key.pick()
key.onMouseAction = key_onMouseAction

door3.closed = True
def door3_onMouseAction(x,y,action):
    if door3.closed:
        if key.inHand():
            door3.setImage("Images/문-오른쪽-열림.png")
            showMessage("철커덕!!! 문이 열렸다.")
            door3.closed = False
        else:
            showMessage("열쇠가 필요해~~~")
    else:
        endGame()
door3.onMouseAction = door3_onMouseAction

startGame(scene1)