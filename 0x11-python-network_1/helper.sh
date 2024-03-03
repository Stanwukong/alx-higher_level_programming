#!/usr/bin/bash
# Commits and pushes code changes to github
pycodestyle *.py
chmod u+x *.py
git status
git add .
git status
git commit -m "$1"
git push
