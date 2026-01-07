---
title: "Drawing simple shapes using OpenCV"
date: 2012-07-13
categories: 
  - "digital-image-processing"
slug: "drawing-simple-shapes-opencv"
---

When creating Machine Vision and Image Processing Algorithms it is often useful to draw simple shape on to the image being processed. This simple example shows how to draw some basic shapes using OpenCV.

```
#include "stdafx.h"
#include "cv.h"
#include "highgui.h"

int _tmain(int argc, _TCHAR* argv[])
{
	// create the output image
	IplImage* output = cvCreateImage(cvSize(400,400),8,3);
	cvZero(output);

	// draw a line
	cvLine(output, cvPoint(10,100), cvPoint(10,200), CV_RGB(0,0,255), 1,8,0);

	// draw a rectangle
	cvRectangle(output, cvPoint(100,10), cvPoint(200, 50), CV_RGB(255,0,0), 1);

	// draw a circle
	cvCircle(output, cvPoint(200,200), 100, CV_RGB(0,255,0), 1, 8);

	// draw an ellipse
	cvEllipse(output, cvPoint(350,350), cvSize(40,50),45, 0, 360, CV_RGB(0,0,255),1,8);

	// show the output
	cvNamedWindow("Output", CV_WINDOW_AUTOSIZE);  
    cvShowImage("Output", output); 

	// wait for user
	cvWaitKey(0);

	// garbage collection		
	cvReleaseImage(&output);
	cvDestroyWindow("Output");
	return 0;
}

```

\[caption id="attachment\_127" align="alignnone" width="298" caption="Drawing simple shapes using OpenCV"\][![](images/drawing-298x300.png "drawing")](images/drawing.png)\[/caption\]
