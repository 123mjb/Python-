import math
import os
import sys
# ⬜⬛


class Renderer:
    def __init__(self):
        self.ThreeDObject = [
            [["1", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]],
            [["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "1", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"],
             ["0", "0", "0", "0", "0", "0", "0", "0", "0"]]
        ]

        self.Rot = [0, 90]
        self.Loc = [5, 5, 5]  # y,z,x
        self.CHANGE = 15
        self.main()

    def getimg(self):
        img = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(0, len(img)):
            for j in range(0, len(img[0])):
                rayloc = self.Loc
                rel = [(j-1)-((len(img[0])-1)/2), (i-1)-((len(img)-1)/2)]
                relr = [self.CHANGE*rel[0]/4, self.CHANGE*rel[1]/4]
                rayr = [relr[0]+self.Rot[0] if relr[0]+self.Rot[0] <= 360 and relr[0]+self.Rot[0] > 0
                        else ((relr[0]+self.Rot[0]) - 360 if relr[0]+self.Rot[0] > 360 \
                        else 360 + relr[0]+self.Rot[0]), \
                        relr[1]+self.Rot[1] if relr[1]+self.Rot[1] <= 360 and relr[1]+self.Rot[1] >= 0 \
                        else ((relr[1]+self.Rot[1]) - 360 if relr[1]+self.Rot[1] > 360 \
                        else 360 + relr[1]+self.Rot[1])]
                # for 1 unit of distance away
                xz = 1*math.cos(math.radians(rayr[1]))
                x = math.sin(math.radians(rayr[0]))*xz
                z = math.cos(math.radians(rayr[0]))*xz
                y = math.sin(math.radians(rayr[1]))
                # print(rayr[0]," ",rayr[1])
                # print(str(y)+" "+str(z)+" "+str(x))
                for _ in range(0, 30):
                    rayloc = [rayloc[0]+(y/2), rayloc[1] +
                              (z/2), rayloc[2]+(x/2)]
                    if (round(rayloc[0]) > 0 and round(rayloc[0]) <= len(self.ThreeDObject) and round(rayloc[1]) > 0 and round(rayloc[1]) <= len(self.ThreeDObject[0]) and round(rayloc[2]) > 0 and round(rayloc[2]) <= len(self.ThreeDObject[0][0])) and self.ThreeDObject[round(rayloc[0])-1][round(rayloc[1])-1][round(rayloc[2])-1] == "1":
                        img[i][j] = 1
                        break
                    if rayloc[0] < 0 or rayloc[1] < 0 or rayloc[2] < 0:
                        break
                    # print(str(len(ThreeDObject))+str(len(ThreeDObject[0]))+str(len(ThreeDObject[0][0])),round(rayloc[0]), round(rayloc[1]), round(rayloc[2]), \
                    # str((round(rayloc[0]) > 0 and round(rayloc[0]) <= len(ThreeDObject) and round(rayloc[1]) > 0 and round(rayloc[1]) <= len(ThreeDObject[0]) and round(rayloc[2]) > 0 and round(rayloc[2]) <= len(ThreeDObject[0][0])) and ThreeDObject[round(rayloc[0])-1][round(rayloc[1])-1][round(rayloc[2])-1] == "1") + str((round(rayloc[0]) > 0 and round(rayloc[0]) <= len(ThreeDObject) and round(rayloc[1]) > 0 and round(rayloc[1]) <= len(ThreeDObject[0]) and round(rayloc[2]) > 0 and round(rayloc[2]) <= len(ThreeDObject[0][0]))))
        # print(img)
        self.printimage(img)

    def printimage(self, imag):
        toprint = ""
        image = imag
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                if image[i][j] == 1:
                    toprint = toprint+"⬛"
                elif image[i][j] == 0:
                    toprint = toprint + "⬜"
            toprint += "\n"
        print(toprint)

    def main(self):
        while True:
            os.system('cls')
            # print(str(Rot))
            self.getimg()
            inp = input('w,a,s,d to move camera: ')
            if inp == 'w':
                if self.Rot[1] > 360-(self.CHANGE/4):
                    self.Rot[1] = self.Rot[1] - 360 + (self.CHANGE/4)
                else:
                    self.Rot[1] += (self.CHANGE/4)
            if inp == 'a':
                if self.Rot[0] < (self.CHANGE/4):
                    self.Rot[0] = 360 - ((self.CHANGE/4) - self.Rot[0])
                else:
                    self.Rot[0] -= (self.CHANGE/4)
            if inp == 's':
                if self.Rot[1] < (self.CHANGE/4):
                    self.Rot[1] = 360 - ((self.CHANGE/4) - self.Rot[1])
                else:
                    self.Rot[1] -= (self.CHANGE/4)
            if inp == 'd':
                if self.Rot[0] > 360-(self.CHANGE/4):
                    self.Rot[0] = self.Rot[0] - 360 + (self.CHANGE/4)
                else:
                    self.Rot[0] += (self.CHANGE/4)
            if inp == 'e':
                sys.exit()
