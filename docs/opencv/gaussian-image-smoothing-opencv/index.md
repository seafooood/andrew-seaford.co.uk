---
title: "Gaussian image smoothing using OpenCV"
date: 2012-07-09
categories:
  - "digital-image-processing"
keywords: [opencv, gaussian-blur, image-smoothing, noise-reduction, image-processing]
---

Image smoothing is often used in digital image processing to reduce noise or camera artifacts. An example of a common algortihm used to perform image smoothing is Gaussian. Gaussian filtering is done by convolving each pixel in the input image with a Gaussian Kernal and then summing to produce the output image.

```
#include "stdafx.h"
#include "cv.h"
#include "highgui.h"

int _tmain(int argc, _TCHAR* argv[])
{
	// open and display input image
	IplImage* input = cvLoadImage("test.jpg");
	cvNamedWindow("Input", CV_WINDOW_AUTOSIZE);
	cvShowImage("Input", input);

	// create the output 
	IplImage* output = cvCreateImage(cvSize(input->width, input->height), input->depth, input->nChannels);
	cvSmooth(input, output, CV_GAUSSIAN, 9);

	// display the output image
	cvNamedWindow("Output", CV_WINDOW_AUTOSIZE);
	cvShowImage("Output", output);

	// wait for user
	cvWaitKey(0);

	// garbage collection
	cvReleaseImage(&input);
	cvReleaseImage(&output);
	cvDestroyWindow("Input");
	cvDestroyWindow("Output");
	
	return 0;
}

```

\[caption id="attachment\_111" align="alignnone" width="300" caption="Input image"\][![](images/input-300x201.png "input")](images/input.png)\[/caption\]

\[caption id="attachment\_113" align="alignnone" width="300" caption="Output Image after smoothing"\][![](images/output1-300x202.png "output")](images/output1.png)\[/caption\]


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/gaussian-image-smoothing-opencv](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/gaussian-image-smoothing-opencv)

## OpenCV Related Articles

- [Detecting the Dominant points on an image using OpenCV](../detecting-dominant-points-image-opencv/index.md)
- [Detecting Dominant Points in an Image using OpenCV in Python](../detecting-dominant-points-in-an-image-using-opencv-in-python/index.md)
- [Drawing simple shapes using OpenCV](../drawing-simple-shapes-opencv/index.md)
- [Flood Fill using OpenCV](../flood-fill-opencv/index.md)
- [Image Contour detection and display using OpenCV](../image-contour-detection-display-opencv/index.md)
