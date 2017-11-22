def crop_imgs(filename=""):
	import numpy as np
	import cv2,copy
	color_img = cv2.imread(filename)
	img = cv2.imread(filename,0)[10:-10,10:-10]
	img = cv2.copyMakeBorder(img,20,20,20,20,cv2.BORDER_CONSTANT,value=[255,255,255])
	ret,thresh = cv2.threshold(img,240,255,cv2.THRESH_BINARY_INV)
	kernel = np.ones((5,5),np.uint8)
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
	thresh2 = copy.deepcopy(thresh)
	contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	cnts=[]
	for i in contours:
	    	area=cv2.contourArea(i)
	    	if area>30000:
	    		cnts.append(i)
	print len(cnts)
	i=1
	for cnt in cnts:
		x,y,w,h = cv2.boundingRect(cnt)
		print str(x)+","+str(y)+" to "+str(x+w)+","+str(y+h)
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		#cv2.drawContours(img,[cnt],-1,(0,255,0),3)
		#approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
		#cv2.imshow('image',thresh2)
		cv2.imwrite(str(i)+filename,color_img[y:(h+y),x:(w+x)])
		#cv2.imshow('coutours',img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		i=i+1
	