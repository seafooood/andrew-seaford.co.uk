# How to Set Up GitHub Actions to Automatically Run Pytests

Automating your software testing is a great way to ensure your code is reliable and to catch bugs early. If you're working on a Python project, you might find yourself manually running tests from the command line every time you make a change. This is a perfect opportunity to streamline your workflow.

This guide will walk you through setting up GitHub Actions to automatically run your `pytest` unit tests every time you push a change or open a pull request. We'll focus on a common scenario where tests are located in a `Backend` directory and will be executed in a GitHub-hosted **Ubuntu Linux** environment. By the end, you'll have a professional, automated testing process right within your repository.

## Creating the GitHub Actions Workflow

The first step is to tell GitHub what you want it to do. You'll accomplish this by creating a special configuration file.

1.  In the root of your repository, create a directory named `.github`.
2.  Inside the `.github` directory, create another directory named `workflows`.
3.  Finally, inside the `.github/workflows` directory, create a new file and name it `python-tests.yml`.

Now, copy and paste the following code into your new `python-tests.yml` file.

```yaml
name: Python Unit Tests

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Check out repository code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
        # If your project has a requirements.txt file, uncomment the line below
        # pip install -r Backend/requirements.txt
      
    - name: Execute Pytest
      run: pytest
      working-directory: ./Backend
```

## Understanding the Workflow File

Let's break down what each part of this file does so you can feel confident customizing it for your own projects.

*   **`name: Python Unit Tests`**
    This sets the name of your workflow, which you'll see in the "Actions" tab of your GitHub repository.

*   **`on`**
    This section defines when the workflow should run. Here, we've configured it to trigger on every `push` and `pull_request` to the `main` branch.

*   **`jobs`**
    This section outlines the series of jobs to be executed.
    *   **`build`**: We've named our single job `build`.
    *   **`runs-on: ubuntu-latest`**: This tells GitHub to run our job on a virtual machine using the latest version of Ubuntu.

*   **`steps`**
    These are the individual tasks that make up the `build` job. They are executed in order.
    *   **`Check out repository code`**: This step uses a pre-built community action (`actions/checkout@v4`) to download your repository's code onto the runner.
    *   **`Set up Python`**: This uses another standard action (`actions/setup-python@v5`) to install your desired version of Python on the runner.
    *   **`Install dependencies`**: This step executes shell commands to install `pytest`. If you have other dependencies listed in a `Backend/requirements.txt` file, you can uncomment the last line to install them as well.
    *   **`Execute Pytest`**: This is the final step where the magic happens.
        *   `run: pytest`: This command starts the `pytest` test runner.
        *   `working-directory: ./Backend`: This crucial instruction tells GitHub to change into the `Backend` directory before running the command, perfectly mimicking how you run it locally.

## Activating Your Workflow

To get your new automated testing workflow up and running, all you need to do is commit and push the `python-tests.yml` file to your repository:

```bash
git add .github/workflows/python-tests.yml
git commit -m "Add GitHub Actions workflow for Python tests"
git push
```

That's it! The workflow is now active. It will automatically run on your next push or pull request to the `main` branch. You can monitor its progress, view logs, and see the results of your test runs in the **Actions** tab of your GitHub repository.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/github/how-to-set-up-github-actions-to-automatically-run-pytests](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/github/how-to-set-up-github-actions-to-automatically-run-pytests)
