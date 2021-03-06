import cv2
import numpy as np

def hough_line(img):
    thetas = np.deg2rad(np.arange(-90.0, 90.0))
    width, height = img.shape
    diag_len = np.ceil(np.sqrt(width * width + height * height))   # max_dist
    rhos = np.linspace(-diag_len, diag_len, diag_len * 2.0)

    cos_t = np.cos(thetas)
    sin_t = np.sin(thetas)
    num_thetas = len(thetas)

    accumulator = np.zeros((2 * diag_len, num_thetas), dtype=np.uint64)
    y_idxs, x_idxs = np.nonzero(img)  # (row, col) indexes to edges


    for i in range(len(x_idxs)):
        x = x_idxs[i]
        y = y_idxs[i]
        
    for t_idx in range(num_thetas):
        rho = round(x * cos_t[t_idx] + y * sin_t[t_idx]) + diag_len
        accumulator[rho, t_idx] += 1
            
    return accumulator, thetas, rhos

img = cv2.imread('./power_left/12.jpg')
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
edges = cv2.Canny(dst,255,0,apertureSize = 3)
accumulator, thetas, rhos = hough_line(edges)
idx = np.argmax(accumulator)
rho = rhos[idx / accumulator.shape[1]]
theta = thetas[idx % accumulator.shape[1]]


##for rho,theta in lines[0]:
##    a = np.cos(theta)
##    b = np.sin(theta)
##    x0 = a*rho
##    y0 = b*rho
##    x1 = int(x0 + 1000*(-b))
##    y1 = int(y0 + 1000*(a))
##    x2 = int(x0 - 1000*(-b))
##    y2 = int(y0 - 1000*(a))
##
##    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#cv2.imshow("IMAGE",edges)
#cv2.waitKey(0)




