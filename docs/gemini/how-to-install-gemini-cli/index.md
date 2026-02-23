---
keywords: [gemini cli, installation, ubuntu, nodejs, npm]
---

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

[https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/gemini/how-to-install-gemini-cli](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/gemini/how-to-install-gemini-cli)

## Gemini Related Articles

- [Configuring Gemini Permissions](../configuring-gemini-permissions/index.md)
- [How To Chat With Langflow From A Python Script](../../langflow/how-to-chat-with-langflow-from-a-python-script/index.md)
- [How To Enable Logging In Langflow](../../langflow/how-to-enable-logging-in-langflow/index.md)
- [How To Install Langflow on Ubuntu Using Docker](../../langflow/how-to-install-langflow-on-ubuntu-using-docker/index.md)
- [How To Install Langflow on Ubuntu Without Docker](../../langflow/how-to-install-langflow-on-ubuntu-without-docker/index.md)
