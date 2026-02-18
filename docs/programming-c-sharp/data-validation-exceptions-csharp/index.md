---
title: "Data Validation and Exceptions in C#"
date: 2013-08-29
categories:
  - "csharp"
keywords: [csharp, data-validation, exceptions, try-catch, error-handling]
---

The setName funcion demostrates simple data validation on the argument value.

```
void setName(string value)
{
    // validate empty
    if (string.IsNullOrWhiteSpace(value))
    {
        throw new ArgumentNullException("Please enter a value");
    }

    // validate length
    if (value.Length > 10)
    {
        throw new ArgumentException("The value is too long");
    }

    // value is valid
    MessageBox.Show("The value is valid");
}

```

When calling the setName function it is important that we implement code to catch any exceptions

```
try
{
    setName(textBox1.Text);
}
catch (Exception ex)
{
    MessageBox.Show("Error " + ex.Message);
}

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/data-validation-exceptions-csharp](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-c-sharp/data-validation-exceptions-csharp)
