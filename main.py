import pyautogui
import mouse
import time
import os

class CaptureBot:
    def __init__(self, title):
        self.title = title
        self.makeDir(self.title)
        self.pageNum = 1
        self.capturedPage = []
        self.CHECKPAGECOUNT = 5

    def makeDir(self, title):
        import os
        if not os.path.exists(title):
            os.makedirs(title)

    def getPoint(self, title):
        print('다음 버튼을 클릭하세요', title)
        while True:
            if mouse.is_pressed(button='left'):
                x, y = pyautogui.position()
                time.sleep(0.5)
                print(title, x, y)
                return (x, y)

    def getCapturePoint(self):
        self.LTx, self.LTy = self.getPoint('Left Top')
        self.RTx, self.RTy = self.getPoint('Right Top')
        self.RBx, self.RBy = self.getPoint('Right Bottom')
        self.NBx, self.NBy = self.getPoint('Next Button')
        self.PVx, self.PVy = self.getPoint('Prev Button')

    def waitForLoad(self):
        time.sleep(0.4)

    def capture(self):
        curPage = pyautogui.screenshot(f'./{self.title}/{self.pageNum}.png', region=(self.LTx, self.LTy, self.RTx - self.LTx, self.RBy - self.RTy))
        self.pageNum += 1
        self.capturedPage.append(curPage)
        print(self.pageNum)

    def clickNext(self):
        pyautogui.click(self.NBx, self.NBy)

    def isEndPage(self):
        if self.pageNum < 10:
            return False
        else:
            iterator = iter(cap.capturedPage[-self.CHECKPAGECOUNT:])
            try:
                first = next(iterator)
            except StopIteration:
                return True
            return all(first == rest for rest in iterator)

    def afterEndPageCaputre(self, campanyName):
        if campanyName =="교보":
            pyautogui.click(487, 1025)
        elif campanyName == 'yes24':
            pyautogui.click(487, 1025)

        for i in range(1, self.CHECKPAGECOUNT+1):
            os.remove(f'./{self.title}/{self.pageNum - i}.png')

    def clickPrev(self):
        pyautogui.click(self.PVx, self.PVy)

    def savePDF(self):
        from PIL import Image
        filenameList = [i for i in os.listdir(f'./{self.title}')]
        filenameList.sort(key=len)
        imageList = []
        for filename in filenameList:
            img = Image.open(f"./{self.title}/{filename}")
            imageList.append(img.convert('RGB'))
        imageList[0].save(f'./{self.title}.pdf', save_all=True, append_images=imageList[1:], quality=100)

cap = CaptureBot(input('제목을 입력하세요: '))
cap.getCapturePoint()
while True:
    cap.capture()
    cap.clickNext()
    cap.waitForLoad()
    if cap.isEndPage():
        cap.afterEndPageCaputre('교보')
        break

cap.savePDF()

