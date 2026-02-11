# Testing Python Functions in a File With Invalid Top-Level Code Using Pytest

When writing Python tests, it’s common to import a module and call its functions directly. But what happens if the file you want to test contains **invalid top-level code** — such as a `return` statement outside of a function?

This guide walks you through a practical workaround: how to test functions in such a file **without editing the source code**. We’ll use `pytest` and a shared fixture in `conftest.py` to keep tests clean and reusable.

> **Platform:** The steps below are written for **Ubuntu Linux**, but the approach works the same on other operating systems where Python and pytest are available.

---

## Problem Scenario

Imagine you inherit a file called `myfile.py` that looks like this:

```python
def functionOne():
    return 1

def functionTwo():
    return 2

def functionThree(a,b):
    return a + b

def main():
    return 2

return main()
```

The issue here is the last line: `return main()`.
Python does not allow `return` statements at the top level of a module, so you cannot simply `import myfile`. Trying to do so will raise a `SyntaxError`.

---

## Goal

We want to:

* Test each function (`functionOne`, `functionTwo`, `main`) using `pytest`.
* Leave the original file untouched.
* Avoid repeating boilerplate code for loading and cleaning the file in every test.

---

## Step 1: Create a Loader Fixture in `conftest.py`

`pytest` has a special file called `conftest.py` where you can define fixtures and hooks that are **automatically available to all tests** in that directory (and its subdirectories).

We’ll use this to write a fixture that:

1. Reads the source code of `myfile.py`.
2. Strips out any invalid top-level `return` lines.
3. Executes the cleaned code in a namespace dictionary.
4. Makes that namespace available to tests.

Here’s the code for `conftest.py`:

```python
# conftest.py (shared across all tests in this folder)
import pathlib
import pytest

@pytest.fixture(scope="module")
def mymodule():
    """Load myfile.py into a namespace, stripping invalid top-level returns."""
    module_path = pathlib.Path(__file__).parent / "myfile.py"
    source = module_path.read_text()

    # Strip out any invalid top-level `return ...` lines
    cleaned_source = "\n".join(
        line for line in source.splitlines() if not line.startswith("return ")
    )

    ns = {}
    exec(cleaned_source, ns)
    return ns
```

---

## Step 2: Write Your Tests

With the fixture in place, you can now write clean and simple tests in `test_myfile.py`:

```python
# test_myfile.py
def test_function_one(mymodule):
    assert mymodule["functionOne"]() == 1

def test_function_two(mymodule):
    assert mymodule["functionTwo"]() == 2

def test_function_three(mymodule):
    assert mymodule["functionThree"](3, 4) == 7

def test_main(mymodule):
    assert mymodule["main"]() == 2
```

Notice how we didn’t need to `import myfile`. Instead, we access functions from the fixture namespace `mymodule`.

---

## Step 3: Run the Tests

From your project directory, run:

```bash
pytest -v
```

You should see output like this:

```
collected 4 items

test_myfile.py::test_function_one PASSED                                                                                              [ 25%]
test_myfile.py::test_function_two PASSED                                                                                              [ 50%]
test_myfile.py::test_function_three PASSED                                                                                            [ 75%]
test_myfile.py::test_main PASSED  
```

---

## Why This Works

* **`conftest.py` is special:** pytest automatically loads fixtures defined here, so they’re available to all tests without imports.
* **The `exec` trick:** By stripping the invalid line and running the cleaned code with `exec`, we can safely define the functions in a namespace dictionary, bypassing the syntax error.
* **Reusability:** Because the loader is defined in one place, you can reuse it across multiple tests without duplication.

---

## Conclusion

Even if you’re stuck with a Python file that can’t be imported normally, you can still test its functions cleanly with pytest. Using a `conftest.py` fixture makes the setup reusable and keeps your test files tidy.

This approach ensures you can write meaningful tests, maintain confidence in your code, and avoid touching source files you can’t change.



## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/importlib/Testing%20Pyhton%20modules%20with%20importlib](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/importlib/Testing%20Pyhton%20modules%20with%20importlib)
