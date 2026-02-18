---
keywords: [ubuntu, bash prompt, PS1, terminal customization, bashrc]
---

# How to Customize Your Bash Prompt on Ubuntu

## Introduction

Have you ever wanted to simplify your command prompt? The default terminal prompt on Ubuntu and other Linux systems is helpful, showing your username, hostname, and current directory (e.g., `user@hostname:~/directory$`). However, when creating tutorials, sharing screenshots, or simply aiming for a more minimalist look, you might prefer to hide this information.

This guide will walk you through how to customize your terminal prompt on **Ubuntu Linux** to create a cleaner, more private workspace.

## Temporarily Changing Your Prompt

You can change your prompt for the current terminal session. This is a great way to try it out without making any permanent changes.

1.  Open your terminal.
2.  Type the following command and press Enter:

    ```bash
    export PS1="> "
    ```

Your prompt will immediately change to a simple `>` character. This change will last until you close the terminal.

## Making Your Custom Prompt Permanent

To make your new prompt the default for every terminal session, you need to add the command to your `.bashrc` file, a script that runs every time you open a new terminal.

1.  **Open the `.bashrc` file** in a text editor. We'll use `nano`, which is a simple command-line editor:

    ```bash
    nano ~/.bashrc
    ```

2.  **Add the command** to the end of the file. Scroll to the bottom of the file and add the following line:

    ```bash
    export PS1="> "
    ```

3.  **Save and exit.** In `nano`, you can do this by pressing `Ctrl+X`, then `Y` to confirm, and finally `Enter`.

4.  **Apply the changes.** To see your new prompt in action without logging out, you can run this command:

    ```bash
    source ~/.bashrc
    ```

From now on, every new terminal you open will greet you with your clean, custom prompt.

## How to Restore the Default Prompt

If you decide you want to go back to the default Ubuntu prompt, simply remove the `export PS1="> "` line from your `~/.bashrc` file and open a new terminal.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/how-to-customize-your-bash-prompt-on-ubuntu](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/how-to-customize-your-bash-prompt-on-ubuntu)
