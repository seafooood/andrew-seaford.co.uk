---
title: "Create a autocompleting textbox using C#"
date: 2012-01-18
categories: 
  - "csharp"
slug: "create-autocompleting-textbox-c"
---

The code example below creates an autocompleting textbox, with the possible values Andy, Andrew, Dylan and Kyle.

```
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace autoComplete
{
    public partial class Form1 : Form
    {
        AutoCompleteStringCollection nameCollection = new AutoCompleteStringCollection();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            nameCollection.Add("Andy");
            nameCollection.Add("Andrew");
            nameCollection.Add("Dylan");
            nameCollection.Add("Kyle");

            txtName.AutoCompleteMode = AutoCompleteMode.Suggest;
            txtName.AutoCompleteSource = AutoCompleteSource.CustomSource;
            txtName.AutoCompleteCustomSource = nameCollection;
        }
    }
}

```
