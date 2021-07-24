## 抽签器 v1.0

- 功能：自定义一个名单（文件名：list.txt，一行一个名字），放在程序相同目录下，随机抽取名单中的名字。
  - 用例：提供王者荣耀英雄列表，今天玩什么？

### v1.0源代码：

> 采用类进行封装

#### picker.py

```python
from core import Core
from gui import Gui

inter = Gui()
picker = Core(inter)
picker.run()
```

#### core.py

```python
import random as rm
class Core:
    def __init__(self,gui):
        self.gui = gui
        try:
            file = open('list.txt', mode='r', encoding='utf-8')
            nameList = file.readlines()
            for i in range(len(nameList)):
                nameList[i] = nameList[i].rstrip('\n')
            self.nl = nameList
        except:
            self.nl = ['请看\n帮助']

    def pick(self):
        length = len(self.nl)
        id = rm.randrange(0,length)
        self.name = self.nl[id]

    def run(self):
        self.pick()
        while True:
            quit = self.gui.quitGet()
            if quit:
                break
            flag = 0
            pickFlag = self.gui.pickGet()
            if pickFlag > flag:
                self.pick()
                flag += 1
            self.gui.showName(self.name)
```

#### gui.py

```python
import tkinter as tk
from tkinter import messagebox as mb

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('picker v1.0')
        # self.root.iconbitmap("picker.ico")
        self.root.geometry('480x270+200+200')

        self.fr = tk.Frame(self.root, relief='ridge', bd=5, bg='#D8D8D8')
        self.fr.place(relx=0.5, rely=0.5, anchor='center')

        self.frnm = tk.Frame(self.fr, relief='groove', bd=3, width=240, height=240, bg='#CED8F6')
        self.frnm.grid(row=0, column=0, rowspan=3)

        self.title = tk.Label(self.fr, text="抽签器", bd=50, font=('黑体',25,'bold'), fg="#F78181", bg="#F2F5A9")
        self.title.grid(row=0, column=1, columnspan=2)

        self.theChosenOne = tk.StringVar()
        self.nm = tk.Label(self.frnm, textvariable=self.theChosenOne, bd=40, font=('黑体',25), bg='#CED8F6', cursor='xterm')
        self.nm.place(relx=0.5, rely=0.5, anchor='center')

        self.pickFlag = 0
        self.pk = tk.Button(self.fr, text = "抽签", bd=3, font=('黑体',20), command = self.pickCount)
        self.pk.grid(row=1, column=1, columnspan=2)

        self.pickFlag = 0
        self.pk = tk.Button(self.fr, text = "帮助", bd=3, font=('黑体',20), command = self.help)
        self.pk.grid(row=2, column=1)

        self.quitFlag = False
        self.qt = tk.Button(self.fr, text = "退出", bd=3, font=('黑体',20), command = self.quit)
        self.qt.grid(row=2, column=2)        

    def showName(self,name):
        self.theChosenOne.set(name)
        self.root.mainloop()

    def help(self):
        mb.showinfo('帮助','请在本程序相同路径下放一个list.txt名单列表，一行一个名字',icon = mb.INFO)

    def pickCount(self):
        self.pickFlag += 1
        self.root.quit()

    def pickGet(self):
        return self.pickFlag

    def quit(self):
        self.root.quit()
        self.quitFlag = True

    def quitGet(self):
        return self.quitFlag
```

### 编译：

- 用`pyinstaller -F -w -i picker.ico picker_v1.0.py [--upx-dir <DIR>]`方式打包生成exe（8.97M）。
  - 其中`<DIR>`为upx文件夹的绝对路径，upx是用于压缩exe大小的，可选。
- exe文件：https://wwx.lanzoui.com/b01ihoygb (52pj)

### 截图：

[![WJHUk6.png](https://z3.ax1x.com/2021/07/19/WJHUk6.png)](https://imgtu.com/i/WJHUk6)

### END
