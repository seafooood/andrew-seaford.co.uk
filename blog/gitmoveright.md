---
title: "GitMoveRight Released"
date: 2026-03-12
slug: "git-move-right-initial-released"
authors: [andrewseaford]
tags: [vs-code, extension, developer-tools]
---

<div style={{display: 'flex', gap: '2rem', alignItems: 'flex-start'}}>
<div style={{flex: 1}}>

Every time you drag a file to a new folder in VS Code, Git silently destroys its history. No warning, no prompt. It just treats the move as a delete and a brand-new file, wiping every commit, blame annotation, and diff in the process.

I built GitMoveRight to fix that. It watches for file moves and stages them as proper Git renames automatically, so history stays intact and your Source Control panel shows a clean rename instead of a confusing delete/add pair. It's free, open source, and available now on the VS Code Marketplace.

</div>
<img src={require('../portfolio/vs-extension-GitMoveRight/GitMoveRight128x128.png').default} alt="GitMoveRight" style={{width: '130px', flexShrink: 0}} />
</div>

[VS Extension - GitMoveRight](../portfolio/vs-extension-GitMoveRight/)
<!-- truncate -->
