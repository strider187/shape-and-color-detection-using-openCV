#classes and subclasses to import
import cv2
import numpy as np
import os



#The main function, main(path), path defines the directory of all the test files
def main(path):
    #reading the image
    img = cv2.imread(path,-1)
    path=path[2:]
    #creating a copy
    final=img
    #converting image to gray scale and making contours
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray,127,255,1)
    contours,h = cv2.findContours(thresh,1,2)
    #Creating lists
    a = []
    color=''
    #Writing data
    data='["'+path    
    #Finding the centroid
    for cnt in contours:
        #Defining the area
        M = cv2.moments(cnt)
        #Defining the centroid
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        ################################'''WE ARE HERE STUDYING FOR ONLY THREE COLOR BLUE, GREEN AND RED'''################################################################
        px=img[cy,cx,0]
        px1=img[cy,cx,1]
        px2=img[cy,cx,2]
        #defining color
        if(px==255):
            color= 'blue'
        elif(px1==128):
            color= 'green'
        elif(px2==255):
            color= 'red'
        #defining shape where approx is the number of sides in the image
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if len(approx)==5:
            shape= "pentagon"
        elif len(approx)==3:
            shape= "triangle"
        elif len(approx)==4:
            shape= "rhombus"
        elif len(approx)==6:
            shape= "hexagon"
        elif len(approx) == 9:
            shape= "half-circle"
        elif len(approx) > 9:
            shape= "circle"

        #ADDING ALL INFO IN DATA
        data+= ',["' + color + '-' + shape + '-' + str(cx) + '-' + str(cy)+'"]'
    #Displaying The Images
    cv2.imshow(data,final)
    cv2.waitKey(0)
    #Closing all the display windows
    cv2.destroyAllWindows()
    return data


if __name__ == "__main__":
    filename='results_#2451.csv'
    mypath = '.'
    #getting all files in the directory with png extension
    onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if f.endswith(".png")]
    #iterate over each file in the directory
    for fp in onlyfiles:
        #process the image
        data = main(fp)
        #printing the reesult
        print (data)
        
