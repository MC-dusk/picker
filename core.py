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