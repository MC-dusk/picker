import random as rm
import time
import os

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

    pick_list = []

    def pick(self):
        def pick1(self):
            length = len(self.nl)
            id = rm.randrange(0,length)
            self.name = self.nl[id]
            self.pick_list.append(self.name+'\n')
        def pick2(self):
            length = len(self.nl)
            id = rm.randrange(0,length)
            id2 = id
            while id2 == id:
                id2 = rm.randrange(0,length)
            self.name = self.nl[id] + '\n' + self.nl[id2]
            self.pick_list.append(self.name+'\n')
        if self.gui.get_pickNum() == 1:
            pick1(self)
        else:
            pick2(self)

    def run(self):
        self.pick()
        while True:
            quit = self.gui.quitGet()
            if quit == True:
                record_history = self.gui.get_history()
                if record_history == True:
                    os.makedirs('history',exist_ok=True)
                    unix_time = str(int(time.time()))
                    f = open(f'history/history-{unix_time}.log', mode='w', encoding='utf-8')
                    f.writelines(self.pick_list)
                    f.close()
                break
            flag = 0
            pickFlag = self.gui.pickGet()
            if pickFlag > flag:
                self.pick()
                flag += 1
            self.gui.showName(self.name)