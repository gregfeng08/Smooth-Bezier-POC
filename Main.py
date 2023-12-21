# Author: Gregory Feng
# Description: Proof of concept of continuous bezier curve merging
# Resources: https://www.stkent.com/assets/pdfs/UCLA-Math-149-Mathematics-of-Computer-Graphics-lecture-notes.pdf
# Main Takeaway: Smooth bezier curves can be generated when the middle control point of the sequentially increasing curve is calculated using 2*S-p where S is the point between the two curves and p is the control point of the first curve

import matplotlib.pyplot as plt
import numpy as np

def propPt(pt1, pt2, prop):
    return [[pt1[0][0]+(pt2[0][0]-pt1[0][0])*prop, pt1[0][1]+(pt2[0][1]-pt1[0][1])*prop, pt1[0][2]+(pt2[0][2]-pt1[0][2])*prop], '.']

def bezierPt(ptArr, prop):
    retArr = []
    if(len(ptArr)==1):
        return ptArr
    for i in range(0,len(ptArr)-1):
        retArr.append(propPt(ptArr[i], ptArr[i+1], prop))
    return bezierPt(retArr, prop)

def bezierPlot(pt1, pt2, pt3):
    prop = 0
    pts = [pt1, pt2, pt3]

    for i in pts:
        ax.scatter(i[0][0], i[0][1], i[0][2], marker=i[1])

    for i in range(0, 10): #ababb
        prop += 0.1
        for pt in bezierPt(pts, prop):
            ax.scatter(pt[0][0], pt[0][1], pt[0][2], marker=pt[1])
    return

def getSmoothPt(pt1, pt2, pt3):
    return [[pt3[0][0]*2-pt2[0][0],pt3[0][1]*2-pt2[0][1],pt3[0][2]*2-pt2[0][2]],'^']

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

pt1 = [[-10,10,10],'o']
pt2 = [[-43,0,50],'o'] #First middle point defines the curve
pt3 = [[5,-10,33],'o']

pt4 = getSmoothPt(pt1, pt2, pt3) #Every middle point must be calculated using smooth pt
pt5 = [[50,-60,70],'d']
pt6 = getSmoothPt(pt3, pt4, pt5) #Calculated using smoothpt
pt7 = [[30,100,50],'d']

bezierPlot(pt1, pt2, pt3)
bezierPlot(pt3, pt4, pt5)
bezierPlot(pt5, pt6, pt7)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.show()