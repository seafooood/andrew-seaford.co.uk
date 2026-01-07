---
title: "Using OpenCV inside a C# WPF application"
date: 2013-08-29
categories: 
  - "csharp"
  - "digital-image-processing"
slug: "opencv-csharp-wpf-application"
---

In this example I will create a C++ dll that with contain the OpenCV image processing code. I then will create a C# WPF application, within this application i will then include the dll and using the image processing function.

1. Install OpenCV http://docs.opencv.org/doc/tutorials/introduction/windows\_install/windows\_install.html#windows-installation
2. Create a C++ Win32 console Application, in this example it will be called ImageProcessingAgain
3. Click Next. Select Application type dll. Then click finish.
4. Click Property Manager, right click on debug, then select 'Add Existing Property Sheet'. If you dont have a property sheet follow the following tutorial for creating The Local Method http://docs.opencv.org/doc/tutorials/introduction/windows\_visual\_studio\_Opencv/windows\_visual\_studio\_Opencv.html
5. Add the following code to the cpp
    
    ```
    // ImageProcessAgain.cpp : Defines the exported functions for the DLL application.
    //
    
    #include "stdafx.h"
    
    #include "opencv\cv.h"
    #include "opencv\highgui.h"
    
    extern "C"
    {   
    	__declspec(dllexport) int exampleImageProcessing(LPCWSTR);
    }
    
    extern int __cdecl exampleImageProcessing(LPCWSTR filename)
    {
    	IplImage* img = cvLoadImage((char*)filename);
    	return img->width;
    }
    
    ```
    
6. build the dll project

8. Create a C# WPF project called UsingOpencvAgain

10. copy the dll and then include the dll within the C# project

12. Select the dll in the solution explorer, set the 'copy to output directory' property to 'copy if newer'

14. Create two textboxes and a button

16. Add the following C# code to the application
     
     ```
     using System;
     using System.Collections.Generic;
     using System.Linq;
     using System.Text;
     using System.Windows;
     using System.Windows.Controls;
     using System.Windows.Data;
     using System.Windows.Documents;
     using System.Windows.Input;
     using System.Windows.Media;
     using System.Windows.Media.Imaging;
     using System.Windows.Navigation;
     using System.Windows.Shapes;
     using System.Runtime.InteropServices;
     
     namespace UsingOpencvAgain
     {
         /// 
         /// Interaction logic for MainWindow.xaml
         /// 
         public partial class MainWindow : Window
         {
             public MainWindow()
             {
                 InitializeComponent();
             }
     
             [DllImport("ImageProcessAgain.dll", CallingConvention = CallingConvention.Cdecl)]
             public static extern int exampleImageProcessing(string filename);
     
             private void button1_Click(object sender, RoutedEventArgs e)
             {
                 textBox2.Text = exampleImageProcessing(textBox1.Text).ToString();
             }
         }
     }
     
     
     ```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/opencv%20csharp%20wpf%20application](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/opencv%20csharp%20wpf%20application)
