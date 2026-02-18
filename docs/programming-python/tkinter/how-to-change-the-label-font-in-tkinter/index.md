---
title: "How To Change The Label Font in TKinter"
date: 2022-10-19
categories:
  - "prog"
  - "python"
tags:
  - "python-2"
keywords: [tkinter, python, gui, font, label]
---

The font attribute of the label widget can be used to change the font style and size.

First, we will create a window with a label using the default font and size.

```
import tkinter as tk

win = tk.Tk()
win.geometry("750x450")

title_label = tk.Label(win, text="hello")
title_label.pack(pady=10)

win.mainloop()

```

Below is the window with the label's default font and style.

[![](images/image-7.png)](images/image-7.png)

Next, we will add the font attribute to the label widget to customize the font style and size. In this example, we are going to change the font style to "Impact" and the font size to 20. The possible font styles are listed on the page https://learn.microsoft.com/en-us/typography/font-list/.

```
import tkinter as tk

win = tk.Tk()
win.geometry("750x450")

title_label = tk.Label(win, text="hello", font= 'Impact 17')
title_label.pack(pady=10)

win.mainloop()
```

Below is the output with the label's customized font style and size.

[![](images/image-8.png)](images/image-8.png)


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/tkinter/how-to-change-the-label-font-in-tkinter](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/tkinter/how-to-change-the-label-font-in-tkinter)
