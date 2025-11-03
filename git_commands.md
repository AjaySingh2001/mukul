# Git Commands

## --soft
Moves HEAD (the current branch) to <commit>.
Does not touch the index or working tree.
Result: all changes between the old HEAD and <commit> become staged (index contains those changes).
Use when: you want to undo commits but keep the changes staged for a different commit (e.g., squash commits or re-commit with edited message).
## example

git reset --soft head

## --mixed
Moves HEAD to <commit>.
Resets the index to match <commit>.
Working tree is left alone (files on disk remain as they were).
Result: changes between old HEAD and <commit> are unstaged and show as modified files (uncommitted in working dir).
Use when: you want to undo commit(s) and unstage changes so you can selectively re-stage.

## example

git reset --mixed <commit> or git reset <commit>

## --hard
Moves HEAD to <commit>.
Resets the index and working tree to match <commit>.
All uncommitted changes are lost (unless you recover via reflog).
Use with caution (never on commits others rely on).
Use when: you want your working tree and index to exactly match a commit (discarding local edits).

## example
## WARNING: this discards uncommitted changes 
git reset --hard origin/main


# --keep

Moves HEAD to <commit> but only if working tree changes can be kept (i.e., no conflicts).
Refuses and aborts if a file would be overwritten.
Safer than --hard when you must preserve local modifications.

# example

git reset --keep <commit>


# --merge

Similar to --keep, tries to reset but keeps local changes, aborts if conflicts would occur. Use rarely.

# example

git reset --merge <commit>