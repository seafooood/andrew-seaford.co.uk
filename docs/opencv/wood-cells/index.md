---
title: "Wood Cells"
date: 2012-01-18
categories:
  - "halcon"
keywords: [halcon, wood-analysis, image-processing, thresholding, computer-vision]
---

Analysis of wood cells using halcon.

```
read_image (Woodcells1, 'C:\\Program Files\\MVTec\\HALCON\\images\\woodcell.png')
X := 20
threshold (Woodcells1, CellBoarder, 0, 120)
get_image_pointer1 (Woodcells1, Pointer, Type, Width, Height)
open_file ('wood_cells.dat', 'output', FileHandle)
for i := 0 to Width-X-1 by 1
    clip_region (CellBoarder, Part, 0, i, Height-1, i+X)
    area_center (Part, Area, Row, Col)
    fwrite_string (FileHandle, i + ' ' + (Area * 100.0 / (X * Height)))
    fnew_line (FileHandle)
endfor
close_file (FileHandle)

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/wood-cells](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/opencv/wood-cells)

## OpenCV Related Articles

- [Detecting the Dominant points on an image using OpenCV](../detecting-dominant-points-image-opencv/index.md)
- [Detecting Dominant Points in an Image using OpenCV in Python](../detecting-dominant-points-in-an-image-using-opencv-in-python/index.md)
- [Drawing simple shapes using OpenCV](../drawing-simple-shapes-opencv/index.md)
- [Flood Fill using OpenCV](../flood-fill-opencv/index.md)
- [Gaussian image smoothing using OpenCV](../gaussian-image-smoothing-opencv/index.md)
