---
keywords: [docker, remove images, ubuntu, disk space, dangling images]
---

# A Guide to Removing Unused Docker Images on Ubuntu

If you frequently work with Docker on your **Ubuntu** system, you've likely accumulated a number of Docker images. While these images are essential for running containers, they can take up a significant amount of disk space over time, especially unused or "dangling" images left over from previous builds. This guide will walk you through a simple and effective way to clean up your system and remove any Docker images that are no longer in use.

Following these steps will help you reclaim valuable disk space and keep your Docker environment organized.

## Viewing Your Current Docker Images

Before you start removing images, it's a good idea to see what's currently on your system. This will give you a clear picture of what will be removed.

To view a list of all Docker images, open your terminal and run the following command:

```bash
sudo docker images list
```

This command will display a list of your images, including their repository, tag, image ID, creation date, and size.

## Pruning Unused Docker Images

The most efficient way to remove unused images is with the `docker image prune` command. This command is specifically designed to help you clean up your image registry.

To remove all images that are not associated with any container, execute this command:

```bash
sudo docker image prune -a
```

You will be prompted to confirm that you want to remove these images. Type `y` and press `Enter` to proceed.

### Understanding the Command

*   `docker image prune`: This is the basic command for removing unused images.
*   `-a` or `--all`: This flag is crucial. It tells Docker to remove all images that are not being used by at least one container. This includes "dangling" images (those without a tag) as well as any other tagged images that are not currently in use.

## Confirming the Cleanup

After the prune command has finished, you can verify that the unused images have been removed by running the initial command again:

```bash
sudo docker images list
```

The output should now show a shorter list of images, reflecting that the unused ones have been successfully deleted.

By following these simple steps, you can easily manage your Docker images on Ubuntu, ensuring your system remains efficient and free of unnecessary clutter.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/a-guide-to-removing-unused-docker-images-on-ubuntu](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/docker/a-guide-to-removing-unused-docker-images-on-ubuntu)

## Docker Related Articles

- [Containerize An Inno Installed Application](../containerize-an-inno-installed-application/index.md)
- [Containerize .net Framework 4.8 Console Application](../containerize-net-framework-4-8-console-application/index.md)
- [How To Avoid Using sudo with Docker](../how-to-avoid-using-sudo-with-docker/index.md)
- [Dockerize a Python Flask App: Step-by-Step Guide](../how-to-containerize-a-python-flask-application/index.md)
- [Troubleshooting: Unable to Delete a Docker Image Used by a Stopped Container on Ubuntu](../troubleshooting-image-in-use/index.md)