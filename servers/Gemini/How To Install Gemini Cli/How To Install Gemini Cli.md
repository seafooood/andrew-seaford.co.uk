# How To Install Gemini Cli on Ubunutu

## Install Procedure

### Step 1 - Install Node.js:

```bash
sudo apt purge nodejs
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts
```

### Step 2 - Install NPM

```bash
sudo apt install npm
``` 
### Step 3 - Install Gemini

```bash
sudo npm install -g @google/gemini-cli
```


## Usage

```bash
gemini
```

## Referances

<https://github.com/google-gemini/gemini-cli>