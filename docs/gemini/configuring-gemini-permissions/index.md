---
keywords: [gemini cli, permissions, yolo mode, settings.json, tool confirmation]
---

# Configuring Gemini Permissions

The permission you grant with "Always" in the interactive prompt is currently **session-specific**, the permissions will be forgotten when you restart the CLI.

Here are the two primary ways to achieve persistent or automatic approval:

-----

## 🚀 Option 1: Use YOLO Mode (`--yolo`)

The easiest way to bypass all tool confirmations, is to start the Gemini CLI in **YOLO mode**. This setting is temporary for the session unless you use the second method.

  * **To start with YOLO mode:**

    ```bash
    gemini --yolo
    ```

    This mode will automatically approve *all* tool calls the model makes (like running `shell` commands, which includes `npm`), so use it with caution as it removes the security prompt.

  * **To toggle YOLO mode on/off within a session:**
    Press **`Ctrl+y`** inside the Gemini CLI prompt.

-----

## 💾 Option 2: Persistent Approval via `settings.json`

The Gemini CLI supports a persistent configuration file where you can explicitly list tools that should be auto-approved, making your choice permanent across all sessions and projects on your machine.

1.  **Locate your User Settings File:**

      * This file is typically located at: `~/.gemini/settings.json` (on Linux/macOS)

2.  **Edit the File:**
    Open this `settings.json` file in a text editor.

3.  **Add `autoApprovedTools`:**
    You need to add a `tools` block with an `autoApprovedTools` array. For a command like `npm`, you are granting permanent permission to the underlying `shell` tool.

    If the file is empty or just contains a theme setting, it might look like this after your modification:

    ```json
    {
      "theme": "Default",
      "tools": {
        "autoApprovedTools": [
          "shell"
        ]
      }
    }
    ```

    The `"shell"` tool is the one Gemini uses to execute commands like `npm`, `git`, `ls`, etc. By adding `"shell"` to this list, you are permanently instructing the CLI to **auto-approve all shell commands** without a prompt.

Any changes you make to the `~/.gemini/settings.json` file will persist across all your Gemini CLI sessions until you manually remove the entry.

## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/gemini/configuring-gemini-permissions](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/gemini/configuring-gemini-permissions)
