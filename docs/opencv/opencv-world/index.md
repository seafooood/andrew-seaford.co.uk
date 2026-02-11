---
title: "OpenCV Hello World"
date: 2012-07-09
categories: 
  - "digital-image-processing"
tags: 
  - "c"
  - "image-processing"
  - "machine-vision"
  - "opencv"
slug: "opencv-world"
---

Here is the Hello World example code for OpenCV. This simple example creates a image called output, then the text "Hello World" is added to the image.

```
#include "stdafx.h"
#include "cv.h"
#include "highgui.h"

int _tmain(int argc, _TCHAR* argv[])
{
	// create image
	IplImage* output = cvCreateImage(cvSize(400, 200), 8, 3);
	
	// create font and add text to the image
	CvFont font;
    cvInitFont(&font, CV_FONT_HERSHEY_SIMPLEX, 1,1,0,1,8);
	cvPutText(output, "Hello World", cvPoint(100,100), &font, cvScalar(255,255,0));
	
	// display image
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

\[caption id="attachment\_118" align="alignnone" width="300" caption="Hello World output image"\][![](images/hello-300x149.png "hello")](images/hello.png)\[/caption\]


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/opencv%20world](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/opencv%20world)
