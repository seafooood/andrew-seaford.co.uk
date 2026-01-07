---
title: "How To Create a Python Requirements File"
date: 2025-02-02
categories: 
  - "prog"
  - "python"
slug: "how-to-create-a-python-requirements-file"
---

Creating and using a requirements.txt file in Python is a standard practice for managing project dependencies. This file lists all the Python packages your project depends on, along with their versions. Here's a step-by-step guide on how to create and use it:

## Creating a requirements.txt File

### Install the Necessary Packages

First, install the packages your project needs. You can do this using pip:

```sh
pip install package_name
```

### Freeze the Current Environment

Once you've installed all the necessary packages, you can generate a requirements.txt file using the pip freeze command. This command outputs a list of installed packages in the current environment and their versions.

```sh
pip freeze > requirements.txt
```

### Manual Editing (Optional)

You can manually edit the requirements.txt file to add or remove packages, or to specify version ranges. The file format is simple: each line contains a package name and an optional version specifier.

```txt
package_name==1.0.0
another_package>=2.0,<3.0
```

## Using a requirements.txt File

### Create a Virtual Environment

It's a good practice to use a virtual environment to manage your project's dependencies. Create a virtual environment using:

```sh
python -m venv myenv
```

### Activate the Virtual Environment

On Windows:

```sh
myenv\Scripts\activate
```

On macOS and Linux:

```sh
source myenv/bin/activate
```

### Install Dependencies from requirements.txt

With the virtual environment activated, you can install all the packages listed in requirements.txt using:

```sh
pip install -r requirements.txt
```

## Best Practices

Pin Versions: Pin the versions of your dependencies to ensure that your project works as expected regardless of updates to those packages. Use == to pin exact versions.

```txt
numpy==1.19.5
pandas==1.2.4
```

Update Regularly: Regularly update your requirements.txt file to keep track of changes in your dependencies.

```sh
pip freeze > requirements.txt
```

Review Dependencies: Periodically review your requirements.txt file to remove unnecessary dependencies that might have been included during development but are no longer needed.

## Example Workflow

### Install Dependencies

```sh
pip install numpy pandas
```

### Freeze Dependencies

```sh
pip freeze > requirements.txt
```

### Check the Generated requirements.txt

```txt
numpy==1.21.0
pandas==1.3.0
```

### Create and Activate a Virtual Environment

```sh
python -m venv myenv
source myenv/bin/activate  # macOS/Linux
myenv\Scripts\activate     # Windows
```

### Install Dependencies in the New Environment

```sh
pip install -r requirements.txt
```

By following these steps, you can ensure that your project’s environment is reproducible, making it easier to collaborate with others and deploy your application.
