---
keywords: [github actions, npm test, CI/CD, react testing, automated testing]
---

# How to Set Up GitHub Actions to Automatically Run npm test

Automating your software testing is a great way to ensure your code is reliable and to catch bugs early. If you're working on a React project, you might find yourself manually running tests from the command line every time you make a change. This is a perfect opportunity to streamline your workflow.

This guide will walk you through setting up GitHub Actions to automatically run your `npm test` unit tests every time you push a change or open a pull request. We'll focus on a common scenario where tests are located in a `Frontend` directory and will be executed in a GitHub-hosted **Ubuntu Linux** environment. By the end, you'll have a professional, automated testing process right within your repository.

## Creating the GitHub Actions Workflow

The first step is to tell GitHub what you want it to do. You'll accomplish this by creating a special configuration file.

1.  In the root of your repository, create a directory named `.github`.
2.  Inside the `.github` directory, create another directory named `workflows`.
3.  Finally, inside the `.github/workflows` directory, create a new file and name it `react-tests.yml`.

Now, copy and paste the following code into your new `react-tests.yml` file.

```yaml
# .github/workflows/react-tests.yml

name: Frontend Unit Tests

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

frontend-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18.x'
          cache: 'npm'
          cache-dependency-path: Frontend/package-lock.json
      - name: Install Node dependencies
        run: npm ci
        working-directory: ./Frontend
      - name: Run Node tests
        run: npm test
        working-directory: ./Frontend
```

## Understanding the Workflow File

How It Works

- name: Frontend Unit Tests: Gives this workflow a clear name in the Actions tab.

- uses: actions/setup-node@v5: This is the official action for setting up a Node.js environment.[1]

  - node-version: '18.x': Specifies the version of Node.js to use. You should adjust this to match your project's requirements.

  - cache: 'npm': Automatically caches your npm dependencies, which can significantly speed up future runs.[2]

  - cache-dependency-path: Frontend/package-lock.json: Tells the cache to refresh whenever you update your dependencies in the package-lock.json file.

  - run: npm ci: This command is recommended for continuous integration. It installs dependencies directly from the package-lock.json file for faster, more reliable builds than npm install.

  - working-directory: ./Frontend: Just like with the Python tests, this crucial line tells GitHub Actions to run the npm ci and npm test commands inside your Frontend folder.

## Activating Your Workflow

To get your new automated testing workflow up and running, all you need to do is commit and push the `react-tests.yml` file to your repository:

```bash
git add .github/workflows/react-tests.yml
git commit -m "Add GitHub Actions workflow for React tests"
git push
```

That's it! The workflow is now active. It will automatically run on your next push or pull request to the `main` branch. You can monitor its progress, view logs, and see the results of your test runs in the **Actions** tab of your GitHub repository.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/github/how-to-set-up-github-actions-to-automatically-run-npm-test](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/github/how-to-set-up-github-actions-to-automatically-run-npm-test)

## GitHub Related Articles

- [How to Set Up GitHub Actions to Automatically Run Pytests](../how-to-set-up-github-actions-to-automatically-run-pytests/index.md)
- ['django-admin startproject' vs 'python -m django startproject'](../../programming-python/django/'django-admin-startproject'-vs-'python-m-django-startproject'/index.md)
- [Creating a Django Site With User Authentication](../../programming-python/django/creating-a-django-site-with-user-authentication/index.md)
- [Django Database Seeding](../../programming-python/django/django-database-seeding/index.md)
- [Getting Started with Django for Flask Developers](../../programming-python/django/getting-started-with-django-for-flask-developers/index.md)
