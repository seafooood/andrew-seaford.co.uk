# How to Create a Custom 3D-Printed Christmas Stamp with FreeCAD

The holiday season is a time for personal touches and heartfelt gifts. If you're looking for a unique way to decorate your Christmas cards, gift tags, or wrapping paper, a custom-made ink stamp is a fantastic DIY project.

This guide will walk you through using a simple Python script in FreeCAD to automatically generate a personalized 3D model of a Christmas stamp, ready for printing. It's a perfect project for 3D printing enthusiasts, crafters, and anyone wanting to add a special, homemade touch to their holiday greetings.

### A Note on Platform

This guide uses FreeCAD, a powerful and free 3D modeling software that runs on **Windows, macOS, and Linux**. The Python script below is designed to work on any of these platforms.

The only system-specific detail you may need to change is the file path to a font. We'll show you exactly how to do that!

### The FreeCAD Macro Script

The following Python code contains all the logic to create your stamp. Simply copy the entire script to follow the steps in the next section.

[ChristmasStamp.py](ChristmasStamp.py)

### How to Create Your Stamp: A Step-by-Step Guide

1.  **Copy the Code**
    Select and copy the entire Python script from the code block above.

2.  **Open the FreeCAD Macro Editor**
    Launch FreeCAD. From the top menu, navigate to `Macro > Macros...`.

3.  **Create a New Macro**
    In the macro window that appears, click the **Create** button. Give your new macro a descriptive name (e.g., `Create_Christmas_Stamp`) and click **OK**. An editor window for your new file will open.

4.  **Paste and Save the Script**
    Paste the script you copied into the editor window, completely replacing any text that might already be there. Save your work by selecting `File > Save` from the menu, and then close the editor tab.

5.  **Run the Macro!**
    Your new macro will now appear in the list. Select it and click the **Execute** button.

Just like that, FreeCAD will automatically generate the 3D model of your stamp in a new document!

### Personalizing Your Stamp

This is where the fun begins! You can easily customize the stamp by editing the parameters at the top of the script.

*   `TEXT_LINES`: This is a Python list of strings. Change the text inside the quotes to whatever you want your stamp to say. Each string is a new line on the stamp.
*   `STAMP_DIAMETER`: Change this value to make the stamp bigger or smaller. The value is in millimeters.
*   `FONT_PATH`: **Important!** If the script fails, it's likely because it can't find the default font. You'll need to provide the correct path to a font file (`.ttf` or `.otf`) on your system. Common paths are included in the script's comments.

### Next Steps

You're now ready to export the final `Christmas_Stamp` object as an STL file (`File > Export`) and send it to your 3D printer.

- [ChristmasStamp.FCStd](ChristmasStamp.FCStd)
- [ChristmasStamp.stl](ChristmasStamp.stl)

Happy printing, and have a very Merry Christmas!