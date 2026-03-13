# VS Code Extension - GitMoveRight

Moving a file in VS Code silently destroys its Git history. GitMoveRight fixes that automatically.

---

<div style={{display: 'flex', gap: '2rem', alignItems: 'flex-start'}}>
<div style={{flex: 1}}>

## The Problem

Dragging a file to a new folder in the VS Code Explorer is a raw filesystem operation. Git has no idea a rename happened. It just sees one file disappear and an untracked file appear. Your Source Control panel fills up with a confusing delete/add pair, and once you commit, all of that file's history is gone. Every blame annotation, every `git log --follow`, every diff: wiped.

## The Solution

GitMoveRight watches for file moves and immediately stages them as a proper Git rename. Git recognises it as the same file, history is preserved, and your Source Control panel shows a clean `R` status. Nothing to configure, nothing to remember. Just drag and drop as you always have.

</div>
<img src={require('./GitMoveRight700x700.png').default} alt="GitMoveRight" style={{width: '280px', flexShrink: 0}} />
</div>

---

## Features

- **Automatic.** Works silently in the background. Just drag and drop as normal.
- **History-preserving.** Moves are staged as Git renames, keeping full commit history, `git log --follow`, and blame intact.
- **Safe.** Only acts on files already tracked by Git. Untracked files and files outside a Git repository are left completely alone.
- **"Move with Git..."** Right-click any file in the Explorer for an explicit, dialog-driven move when you want full control.
- **Configurable.** Turn off automatic staging or notifications at any time via VS Code Settings.

---

## How to Use

### Automatic (drag and drop)

Move files in the Explorer as you normally would. GitMoveRight handles the rest. You'll see a brief notification confirming the rename was staged, and the Source Control panel will show `R` instead of a delete/add pair.

### Manual ("Move with Git...")

1. Right-click any tracked file in the Explorer
2. Select **Move with Git...**
3. Choose the destination in the save dialog
4. GitMoveRight moves the file and stages the rename for you

---

GitMoveRight is free and open source. Download it from the VS Code Marketplace or browse the source on GitHub.

## Extension Marketplace

[VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=AndrewSeaford.gitmoveright)

## Github Repository

[GitHub vs-code-extension-GitMoveRight](https://github.com/seafooood/vs-code-extension-GitMoveRight)
