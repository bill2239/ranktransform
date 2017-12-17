import numpy
import cv2
import sys
 
def rank_transform(img_path,windowsize):
    image = cv2.imread(img_path, 0)
    height = len(image)
    width = len(image[0])
     
    #window size
    hy = windowsize
    wx = windowsize
     
    for y in xrange(hy/2, height - hy/2):
        for x in xrange(wx/2, width - wx/2):
            count = 0
            #MxN
            for j in xrange(y - hy/2, y + hy/2 + 1):
                for i in xrange(x - wx/2, x + wx/2 + 1):
                    if image[j][i] > image[y][x]:
                        count+=1

            image[y][x] = count
    rt= image[1:height-1,1:width-1] #offet by 1
    #optional -- scale to unsigned 8 bit for visualization 
    minVal=0
    maxVal=8.0
    rt = 255.0 * ( rt - minVal ) / (maxVal - minVal - 1.0)  
    return rt

rt= rank_transform(sys.argv[2],3)
cv2.imshow("rank", rt)
cv2.waitKey(0)

filename = sys.argv[2]
cv2.imwrite(filename, rt)

