# How to Play a Sound When Claude Code Needs Your Attention

When working with Claude Code agents, you might find that the agent pauses mid-task and waits for your permission to continue, but because the terminal window is in the background, you don't notice until much later. This breaks your flow and slows down your work.

This guide will walk you through how to configure Claude Code to play a sound whenever it needs your attention, using its built-in hooks system on a Linux system. By the end, you will have audio alerts for two situations: when the agent is asking for permission to use a tool, and when it has finished a task and is waiting for your next instruction.

## What Are Claude Code Hooks?

Hooks are shell commands that Claude Code runs automatically in response to specific events in its lifecycle. You configure them in `~/.claude/settings.json`, and Claude Code fires them at the appropriate moments. One of the available hook events is `Notification`, which fires when Claude Code wants to alert the user.

The `Notification` hook supports several notification types. The two most useful for this guide are:

- `permission_prompt` - fires when the agent needs you to approve a tool use
- `idle_prompt` - fires when the agent has finished and is waiting for your next instruction

## Setting Up Sound Notifications

### Step 1: Find a working audio player

Claude Code hooks run shell commands, so you need a command-line audio player. On most Linux systems with PipeWire, `pw-play` is available. Check which players you have:

```bash
which pw-play paplay aplay
```

This guide uses `pw-play`. If you only have `aplay`, substitute it in the commands below.

### Step 2: Choose your notification sounds

Linux systems with the freedesktop sound theme include a set of short audio clips in `/usr/share/sounds/freedesktop/stereo/`. List them to see what is available:

```bash
ls /usr/share/sounds/freedesktop/stereo/
```

Test a sound by playing it directly:

```bash
pw-play /usr/share/sounds/freedesktop/stereo/bell.oga
```

Try a few until you find ones you are happy with. This guide uses:

- `message-new-instant.oga` for permission prompts
- `complete.oga` for idle prompts (task complete)

### Step 3: Open your Claude Code settings file

Open `~/.claude/settings.json` in your editor. If the file does not exist yet, create it. If it already has content, you will be adding a new `hooks` key alongside the existing ones.

### Step 4: Add the Notification hooks

Add the following `hooks` block to your `settings.json`. If the file was empty, this is the entire contents:

```json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "pw-play /usr/share/sounds/freedesktop/stereo/message-new-instant.oga"
          }
        ]
      },
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "pw-play /usr/share/sounds/freedesktop/stereo/complete.oga"
          }
        ]
      }
    ]
  }
}
```

If your file already has other settings, such as a `permissions` block, merge the `hooks` key in at the top level:

```json
{
  "permissions": {
    "allow": []
  },
  "hooks": {
    "Notification": [
      {
        "matcher": "permission_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "pw-play /usr/share/sounds/freedesktop/stereo/message-new-instant.oga"
          }
        ]
      },
      {
        "matcher": "idle_prompt",
        "hooks": [
          {
            "type": "command",
            "command": "pw-play /usr/share/sounds/freedesktop/stereo/complete.oga"
          }
        ]
      }
    ]
  }
}
```

There are multiple settings.json files, select the appropriate settings based on your requirements. The naming is:

- .claude/settings.json — project settings, committed to repo (shared with team)
- .claude/settings.local.json — local project settings, gitignored (personal)
- ~/.claude/settings.json — global user settings

### Step 5: Test the sounds

Before relying on the hooks, verify that both commands work correctly from your terminal:

```bash
pw-play /usr/share/sounds/freedesktop/stereo/message-new-instant.oga
pw-play /usr/share/sounds/freedesktop/stereo/complete.oga
```

You should hear each sound play. If you do not hear anything, check that your system audio is not muted and that `pw-play` is correctly installed.

Once both sounds play successfully, Claude Code will fire them automatically from the next session onwards. No restart is required.

## Choosing Different Sounds

The freedesktop sound theme includes several other useful clips. Here are some good candidates if you want to use something different:

| File | Character |
|---|---|
| `bell.oga` | Short, sharp bell |
| `alarm-clock-elapsed.oga` | Repeating alarm, hard to miss |
| `complete.oga` | Soft completion chime |
| `dialog-warning.oga` | Warning tone |
| `dialog-information.oga` | Neutral information tone |

Replace the filename in the `command` value in `settings.json` to switch sounds.

## Conclusion

Claude Code's hooks system makes it straightforward to add audio alerts to your workflow. By adding a `Notification` hook to `~/.claude/settings.json`, you can configure separate sounds for two key moments: when the agent needs your permission to proceed, and when it has finished a task and is waiting for your next instruction. This means you can keep the terminal in the background and still know immediately when Claude Code needs your attention.
