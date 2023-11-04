#!/bin/bash

# Check if there are any uncommitted changes
if [[ -n $(git status -s) ]]; then
  echo "Uncommitted changes found. Stashing changes..."
  git stash
fi

# Add all changes to the staging area
git add .

# Commit the changes with a message
git commit -m "done"

# Push the changes to the remote repository
git push

# Pop the stashed changes, if any
if [[ -n $(git stash list) ]]; then
  echo "Popping stashed changes..."
  git stash pop
fi
