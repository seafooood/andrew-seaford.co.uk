# Getting Started With FreeCAD: Spreadsheets and Parametric Design

## Introduction

Parametric design allows you to define the dimensions of your model using parameters. These parameters can be stored in a spreadsheet, making it incredibly easy to update your design. Change a value in the spreadsheet, and your 3D model will automatically update to reflect the new dimension. This saves you time and effort, especially in complex projects.

This guide will walk you through the process of creating a simple parametric cube in FreeCAD. You will learn how to:

*   Create a spreadsheet to store your design parameters.
*   Link the dimensions of your 3D model to the values in the spreadsheet.
*   Modify your model by simply changing the values in the spreadsheet.

By the end of this tutorial, you'll have a solid understanding of how to use spreadsheets to create parametric designs in FreeCAD.

## Getting Started

### Step 1: Create a Spreadsheet

1.  From the toolbar dropdown, select the **Spreadsheet** workbench.
2.  Click on the **Create Spreadsheet** icon to create a new spreadsheet.

![Creating a new spreadsheet in FreeCAD](image.png)

### Step 2: Define Your Parameters

1.  Enter the following values into the spreadsheet:

| | A | B |
| :--- | :--- | :--- |
| **1** | Width | 10 |
| **2** | Length | 20 |
| **3** | Height | 30 |

![Entering parameters into the spreadsheet](image-1.png)

### Step 3: Set Aliases for Your Parameters

To make our parameters easier to reference, we'll give them aliases.

1.  Right-click on cell **B1** (which contains the value `10`) and select **Properties** from the context menu.
2.  In the **Cell Properties** window, go to the **Alias** tab.
3.  Enter `width` as the alias and click **OK**.

![Setting an alias for the width parameter](image-2.png)

4.  Repeat this process for cells **B2** and **B3**, using the aliases `length` and `height` respectively.

Once you've set the aliases, the cells should be highlighted in yellow, indicating that they have an alias.

![All parameters with aliases set](image-3.png)

### Step 4: Create the 3D Model

1.  From the toolbar dropdown, select the **Part Design** workbench.
2.  Click on the **Create Body** icon to create a new body for our model.

![Creating a new body in the Part Design workbench](image-4.png)

3.  Click on **Create sketch** to start sketching our model.
4.  Select the **XY-plane (Base plane)** and click **OK**.

![Selecting the XY-plane for the sketch](image-5.png)

### Step 5: Draw the Base of the Cube

1.  Click on the **Create Rectangle** icon and draw a rectangle of any size in the sketch editor.

### Step 6: Link the Sketch to the Spreadsheet

Now, we'll link the dimensions of the rectangle to the parameters in our spreadsheet.

1.  Select the vertical constraint of the rectangle. Click on the **f(x)** icon next to the length value to open the **Formula Editor**.

![Opening the Formula Editor for the vertical constraint](image-6.png)

2.  In the **Formula Editor**, enter `Spreadsheet.length` and click **OK**.

![Entering the formula for the length](image-7.png)

![The length of the rectangle is now linked to the spreadsheet](image-8.png)

3.  Next, select the horizontal constraint of the rectangle. Click on the **f(x)** icon next to the height value to open the **Formula Editor**.
4.  In the **Formula Editor**, enter `Spreadsheet.width` and click **OK**.

![Entering the formula for the width](image-9.png)

5.  Click **Close** to close the sketch editor.

### Step 7: Create the Pad

1.  With the sketch selected, click on the **Pad** icon to extrude the rectangle into a 3D shape.
2.  In the **Pad parameters**, click on the **f(x)** icon next to the **Length** value.
3.  In the **Formula Editor**, enter `Spreadsheet.height` and click **OK**. Then, click **OK** again to create the pad.

![Entering the formula for the height of the pad](image-10.png)

### Step 8: You're Done!

Congratulations! You have successfully created a parametric cube.

![The final parametric cube](image-11.png)

Now for the fun part! Go back to the **Spreadsheet** tab and change the values for `width`, `length`, and `height`. You'll see the cube automatically resize itself based on your changes.

![Resizing the cube by changing the spreadsheet values](image-12.png)

![The cube automatically resizes](image-13.png)

## Conclusion

In this tutorial, you've learned the fundamentals of parametric design in FreeCAD. By using a spreadsheet to control the dimensions of your model, you can create flexible and easily modifiable designs. This is a powerful technique that can save you a lot of time and effort in your projects.

Now that you understand the basics, you can start exploring more complex parametric designs. Happy modeling!