# How To Create a Python Virtual Environment

It's a good practice to use a virtual environment to manage your project's dependencies. Create a virtual environment using:

## Setup

### Step 1 - Install Package

- Install the venv package

```bash
sudo apt install python3.12-venv
```

### Step 2 - Create Env

- Create the virtual environment. In this example, we are going to name the venv asenv.

```sh
python -m venv asenv
```

### Step 3 - Activate the Virtual Environment

- On Windows:

```sh
asenv\Scripts\activate
```

- On macOS and Linux:

```sh
source asenv/bin/activate
```

### Step 4 - Select Virtual Environment in VS Code

- In VS Code select a python file.
- In the status bar at the bottom of the screen, click *Select Interpreter*
![alt text](image-1.png)
- From the list select the venv
![alt text](image.png)
- The selected interpreter in the status bar should now show the venv name.
![alt text](image-2.png)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/venv/How%20To%20Create%20a%20Python%20Virtual%20Environment](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming%20python/venv/How%20To%20Create%20a%20Python%20Virtual%20Environment)
