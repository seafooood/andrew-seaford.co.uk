# Troubleshooting: Unable to Delete a Docker Image Used by a Stopped Container on Ubuntu

## Introduction

When working with Docker on your Ubuntu system, you might encounter a situation where you're unable to delete a Docker image, even though you've stopped the container that was using it. This typically happens because a stopped container, while not running, still maintains a connection to the image it was created from. Docker preserves this link to allow you to restart or inspect the container later.

This guide will walk you through the simple steps to safely and completely remove a Docker image by first detaching it from its stopped container.

## Understanding the Error Message

When you attempt to remove the image, you will see an error message similar to this:

```bash
Error response from daemon: conflict: unable to delete a04352c09577 (must be forced) - image is being used by stopped container d13eb48bb62e
```

This message clearly indicates that the image with the ID `a04352c09577` cannot be deleted because a stopped container with the ID `d13eb48bb62e` is still referencing it.

## Step-by-Step Solution

To resolve this, you'll need to remove the container first, and then you'll be free to delete the image.

### Step 1: Stop the Container (Optional but Recommended)

While the error message indicates the container is already stopped, it's good practice to run the `stop` command to be certain. Use the container ID from the error message.

```bash
sudo docker container stop d13eb48bb62e
```

### Step 2: Remove the Stopped Container

Now, you need to permanently remove the container. This action will sever the link to the Docker image.

```bash
sudo docker container rm d13eb48bb62e
```

Once this command is successful, the container is deleted.

### Step 3: Delete the Docker Image

With the container removed, you can now successfully delete the Docker image. Use the image ID from the original error message.

```bash
sudo docker image remove a04352c09577
```

### Step 4: Confirm the Image Deletion

To verify that the image has been removed, you can list all the Docker images on your system.

```bash
sudo docker image list
```

The image with the ID `a04352c09577` should no longer appear in the list.