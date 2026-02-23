---
keywords: [ubuntu, apt, apt-get, package management, debian]
---

# Apt vs Apt-get Commands on Ubuntu

## Introduction

The primary difference is that **`apt`** is a newer, more **user-friendly** command-line interface designed for **interactive use**, while **`apt-get`** is an older, **low-level** tool primarily maintained for **scripting** and **backward compatibility**.

Since 2014, the `apt` command has been the recommended tool for daily package management on Debian-based systems like Ubuntu, as it simplifies and combines the most frequently used functions of older tools like `apt-get` and `apt-cache`.

### ⚙️ Key Differences

| Feature | `apt-get` (Older, Low-Level) | `apt` (Newer, User-Friendly) |
| :--- | :--- | :--- |
| **User Experience** | Less verbose output, no progress bar. | **More information**, including a **progress bar** during installation/upgrade. |
| **Search** | Requires the separate **`apt-cache search`** command. | **Includes search capability** (`apt search <package>`). |
| **Dependency Handling** | Standard dependency resolution. | **Superior dependency resolution**, can suggest or recommend packages. |
| **Upgrade Behavior** | `apt-get upgrade` does **not** install newly required packages for dependencies; it also leaves old package versions on the system. | `apt upgrade` **installs new dependencies** and by default **removes obsolete package versions** to free up disk space. |
| **Recommended Use** | Primarily for **scripts** and **automation** (due to stable, predictable output). | Primarily for **interactive, day-to-day package management**. |

### 💻 Example Commands

For example the two commands below are equivalent:

1.  `sudo apt install virtualbox-guest-utils`
2.  `sudo apt-get install virtualbox-guest-utils`

The commands will achieve the **same result** (installing the package) because `install` is a function that both tools support identically.

However, moving forward, it's generally recommended to switch to **`apt`** for your daily interactive use (like your example above) to benefit from the improved user experience and feature set. You can continue to use `apt-get` in any existing scripts to ensure they don't break, as the output of `apt` is not guaranteed to be backward-compatible.


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/apt-vs-apt-get](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/ubuntu/apt-vs-apt-get)

## Ubuntu Related Articles

- [Disk Cleanup Ubuntu](../disk-cleanup-ubuntu/index.md)
- [How To Assign A Static Ip Address in Ubuntu](../how-to-assign-a-static-ip-address-in-ubuntu/index.md)
- [How To Change Hostname In Ubuntu](../how-to-change-hostname-in-ubuntu/index.md)
- [How to Customize Your Bash Prompt on Ubuntu](../how-to-customize-your-bash-prompt-on-ubuntu/index.md)
- [Ubuntu 12.4 Enable SSH Service](../ubuntu-12-4-enable-ssh-service/index.md)
