# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 22:20:34 2020
@author: Animesh
"""

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
from IPython import get_ipython

get_ipython().run_line_magic('matplotlib', 'qt')  #Plot in seperate window
#get_ipython().run_line_magic('matplotlib', 'inline')

lcam = 'inputVideo/vid4_L.mp4'
rcam = 'inputVideo/vid4_R.mp4'
outVideo = 'outputVideo/outVideo4.avi'

portLand = 0    # 0 means portrait, otherwise landscape

if (portLand == 0):
    lrot = 3    #Rotate image
    rrot = 3
else:
    lrot = 0    #Rotate image
    rrot = 2

def brmatch(Lcam, Rcam):
    # Convert to LAB space before color match
    Lcam_lab = cv2.cvtColor(Lcam, cv2.COLOR_BGR2LAB).astype("float32")
    Rcam_lab = cv2.cvtColor(Rcam, cv2.COLOR_BGR2LAB).astype("float32")
    
    (L_l, L_a, L_b) = cv2.split(Lcam_lab)
    (R_l, R_a, R_b) = cv2.split(Rcam_lab)
    
    L_l_mean = np.mean(L_l)
    L_a_mean = np.mean(L_a)
    L_b_mean = np.mean(L_b)
    R_l_mean = np.mean(R_l)
    R_a_mean = np.mean(R_a)
    R_b_mean = np.mean(R_b)
    L_l_std = np.std(L_l)
    L_a_std = np.std(L_a)
    L_b_std = np.std(L_b)
    R_l_std = np.std(R_l)
    R_a_std = np.std(R_a)
    R_b_std = np.std(R_b)
    
    # Subtract R  mean from itself
    R_new_l = R_l - R_l_mean
    R_new_a = R_a - R_a_mean
    R_new_b = R_b - R_b_mean
    
    # Multiply with std ratio
    R_new_l = (L_l_std/R_l_std)*R_new_l
    R_new_a = (L_a_std/R_a_std)*R_new_a
    R_new_b = (L_b_std/R_b_std)*R_new_b
    
    # Add L mean
    R_new_l += L_l_mean
    R_new_a += L_a_mean
    R_new_b += L_b_mean
    
    R_new_l = np.clip(R_new_l, 0, 255)
    R_new_a = np.clip(R_new_a, 0, 255)
    R_new_b = np.clip(R_new_b, 0, 255)
    
    Rcam_new_lab = cv2.merge([R_new_l, R_new_a, R_new_b])
    Rcam_new = cv2.cvtColor(Rcam_new_lab.astype("uint8"), cv2.COLOR_LAB2BGR)
    return Rcam_new

######################################
##  First Scan
##  Read both camera to find frame count
######################################
print("First Scan")
cap = cv2.VideoCapture(lcam) # Left camera
#cap.set(3,640)
#cap.set(4,480)
cap2 = cv2.VideoCapture(rcam) #Right Camera
#cap2.set(3,640)
#cap2.set(4,480)
w1=int(cap.get(3))
h1=int(cap.get(4))
print("Raw Video width, Height = ", w1,h1)

if (cap.isOpened()== False) :
    print("Camera 1 Not Found")
if (cap2.isOpened()== False) :
    print("Camera 2 Not Found")

currentFrame=0
frame_count=0

# Loop for capturing frame by frame
while(1) :
    ret, frame1 = cap.read()
    if ret:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyWindow('Frame1')
        elif cv2.waitKey(1) == 27:
            break
    else: break
    ret, frame2 = cap2.read()
    if ret:
        if cv2.waitKey(1) & 0xFF == ord('e'):
            cap2.release()
            cv2.destroyWindow('Frame2')
        elif cv2.waitKey(1) == 27:
            break
    else: break
    currentFrame += 1
    frame_count+=1
cap.release()
cap2.release()
cv2.destroyAllWindows()
print('Number of Frames = '+str(frame_count))

######################################
##  Second Scan
##  Read both camera to create individual time difference and create
##  intensity vectors
######################################
print("Second Scan")

cap = cv2.VideoCapture(lcam)  #Left camera
cap2 = cv2.VideoCapture(rcam) #Right Camera

ret, cam1a = cap.read()
cam1a_1 = np.rot90(cam1a,lrot)
h, w, b = np.shape(cam1a_1)
print("Rotated Video width, Height = ", w,h)
hby4 = round(h/4)
thby4 = round(3*h/4)
wby4 = round(w/4)
twby4 = round(3*w/4)

ret, cam2a = cap2.read()
cam2a_1 = np.rot90(cam2a, rrot)
h1, w1, b1 = np.shape(cam2a_1)
h1by4 = round(h1/4)
th1by4 = round(3*h1/4)
w1by4 = round(w1/4)
tw1by4 = round(3*w1/4)

result1 = np.zeros(frame_count)
result2 = np.zeros(frame_count)
intensity1 = 0
intensity2 = 0
i=0
#while(1) :
print('Loop # ')

for i in range(0,frame_count-1):
    print(i, end='\r')
    ret, cam1b = cap.read()
    if ret:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
        elif cv2.waitKey(1) == 27:
            break
    else: break
    cam1b_1 = np.rot90(cam1b,lrot)
    ret, cam2b = cap2.read()
    if ret:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap2.release()
        elif cv2.waitKey(1) == 27:
            break
    else: break
    cam2b_1 = np.rot90(cam2b,rrot)  
    diff1 = np.uint8(np.absolute(cam1a_1.astype(np.int)-cam1b_1.astype(np.int)))
    diff2 = np.uint8(np.absolute(cam2a_1.astype(np.int)-cam2b_1.astype(np.int)))
    cv2.imshow('Difference',diff2)

    intensity1 = 0
    intensity2 = 0
    for j in range(hby4, thby4):
        for k in range(wby4, twby4):
            m1 = diff1[j][k]
            intensity1 = intensity1 + (np.int(m1[0]) + np.int(m1[1]) + np.int(m1[2]))/3
            result1[i] = intensity1
    cam1a_1 = cam1b_1
    
    for a in range(h1by4, th1by4):
        for b in range(w1by4, tw1by4):
            m2 = diff2[a][b]
            intensity2 = intensity2 + (np.int(m2[0]) + np.int(m2[1]) + np.int(m2[2]))/3
            result2[i] = intensity2
    cam2a_1 = cam2b_1
    #i += 1
result1 = result1 - np.mean(result1)
result1 = result1*100/max(result1)
result2 = result2 - np.mean(result2)
result2 = result2*100/max(result2)
plt.plot(result1, 'r')
plt.plot(result2, 'b')
plt.grid()
plt.xlabel('Difference Frame')
plt.ylabel('Intensity')
plt.title('Difference Frame vs. Intensity')
plt.legend(('Red:Left Camera', 'Blue:Right Camera'), 
            loc='lower left', shadow=True)
plt.show

cap.release()
cap2.release()
cv2.destroyAllWindows()

print(end='\n')
print("Cross Correlate Intensity Vectors with changing delay")

l = len(result1)
delay = 20   # Assumption is there will be max +/- 20 frame delay difference

result3 = np.zeros(2*delay+1)
x_result3 = np.arange(-delay, delay+1, 1)  # x-axis fpr plotting

k = 0
for i in range(-delay, delay+1):
    if i>0:
        #print(len(result1[i:l]),len(result2[0:l-i]))
        x1_1 = result1[i:l]
        x2_1 = result2[0:l-i]
        result3[k] = np.dot(x1_1,x2_1)/math.sqrt(np.dot(x1_1,x1_1)*np.dot(x2_1,x2_1))
        k += 1
    else:
        #print(len(result1[0:l+i]),len(result2[-i:l]))
        x1_1 = result1[0:l+i]
        x2_1 = result2[-i:l]
        result3[k] = np.dot(x1_1,x2_1)/math.sqrt(np.dot(x1_1,x1_1)*np.dot(x2_1,x2_1))
        k += 1
    #result[i] = np.cov(x1[0:l-i],x2[i:l])
#print(result3)
plt.figure()
plt.plot(x_result3, result3)
plt.grid(True)
plt.xlabel('Frame Delay')
plt.ylabel('Cross Correlation')
plt.title('Cross Correlation vs. Frame Delay')
plt.show
ind = np.argmax(result3)
diff_act = -delay + ind + 1
print("Frame difference = ", diff_act)


######################################
##  Third and Final Scan
##  Read both camera, synchronize and stitch back
######################################
print("Third Scan")

cap = cv2.VideoCapture(lcam)  #Left camera
#cap.set(3,640)
#cap.set(4,480)
cap2 = cv2.VideoCapture(rcam) #Right Camera
#cap2.set(3,640)
#cap2.set(4,480)

currentFrame = 0
loopno = 0

if (portLand == 0):     # portrait mode
    out3 = cv2.VideoWriter(outVideo, cv2.VideoWriter_fourcc('X','V', 'I', 'D'), 22, (2*w+140, h))
else:
    out3 = cv2.VideoWriter(outVideo, cv2.VideoWriter_fourcc('X','V', 'I', 'D'), 22, (2*w, h))

# Create a grey image to create precise gap between videos.
# This is important to create the right 3-D image when viewing in a phone
# using a VR set
camt = 80*np.ones((h,140,3),dtype=np.uint8)

#diff_act=1

# Throw away frames to synchronize the videos
if(diff_act>=0):
    for j in range(0, diff_act-1):
      ret, cam = cap.read() 
else:
    for j in range(0, abs(diff_act)-1):
      ret, cam1 = cap2.read()     

# Stitch frames
for i in range(0,frame_count-abs(diff_act)):
    ret, cam1 = cap.read()
    L_cam = np.rot90(cam1,lrot)
    ret, cam2 = cap2.read()
    R_cam = np.rot90(cam2,rrot)
    R_cam_match = brmatch(L_cam, R_cam)  # Color match
    if (portLand == 0):     # portrait mode
        op = np.concatenate((L_cam, camt, R_cam_match), axis=1)
    else:
        op = np.concatenate((L_cam, R_cam_match), axis=1)
    out3.write(op)

out3.release() 
cap.release()
cap2.release()
#cv2.destroyAllWindows()                 