---
title: "Customize Inno Setup Installer Images: WizardImageFile Guide"
description: "Customize your Inno Setup installer with custom images using WizardImageFile and WizardSmallImageFile. Includes correct image sizes and BMP format guide."
keywords: [inno setup custom images, wizardimagefile, wizardsmallimagefile, inno setup theme, inno setup installer images, inno setup wizard image size]
date: 2015-02-12
categories:
  - "inno"
---

To customise the look of your inno installer, you can modify the images displayed on the install pages. The large image on the left hand side of the instal pages is set using the parameter WizardImageFile. The small image shown on the top right of the install pages is set using the parameter WizardSmallImageFile.

In this example I have replaced the standard images with a large red image. Hopefully you will make an image that is more appealing.

![InstallLargeImage](images/installlargeimage-300x227.png)

![InstallSmallImage](images/installsmallimage-300x228.png)

The WizardImageFile and WizardSmallImageFile parameters should be defined in the \[setup\] section of the inno install script. In this example the images are in the folder c:\\InstallFiles and are called Small.bmp and Large.bmp.

```yml
[Setup] 
WizardSmallImageFile="C:\InstallFiles\Small.bmp" 
WizardImageFile="c:\InstallFiles\Large.bmp"
```

The files must be saved as 256bit bmp files. I created my examples files using GIMP. To save the images using GIMP.

1. Click File > Export As...
2. Select a location for the file, enter a file name and then click export
3. Expand the 'Compatibility Options' and check 'Do not write color space information'. Expand the 'Advanced Options' and select 24 bits R8 G8 B8 and then click the export button

![Export](images/export-182x300.png)

The small image should be 55x58 pixels. The large image should be 164x314 pixels.

- Download full Inno script [CustomImage.iss](customimages.iss "CustomImage.iss")
- Download image large [Large.bmp](large.bmp "Large.bmp")
- Download image small [Small.bmp](small.bmp "Small.bmp")

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/custom-inno-theme](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/inno/custom-inno-theme)
