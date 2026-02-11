# How To Avoid Using sudo with Docker

## Introduction
It's common to have to run Docker commands with sudo on a fresh Ubuntu install. The easiest and most recommended way to avoid this is to add your user to the docker group.


## Step 1 - Add Your User to the docker Group

Run the following command in your terminal, replacing YOUR_USERNAME with your actual username (you can use the $USER variable, which automatically holds your current username, as shown):

```Bash
sudo usermod -aG docker $USER
```

* sudo: Executes the command with superuser privileges (required for this operation).

* usermod: The command for modifying a user account.

* -aG: An option that means "append" (-a) the user to the specified "group" (-G).

* docker: The name of the group you are adding your user to.

* $USER: An environment variable representing your current logged-in user.

## Step 2 - Activate the Changes

For the group changes to take effect, you need to either log out and log back in or restart your session.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/How%20To%20Avoid%20Using%20sudo%20with%20Docker](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/How%20To%20Avoid%20Using%20sudo%20with%20Docker)
