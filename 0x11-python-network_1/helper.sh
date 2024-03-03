#!/usr/bin/bash
# Commits and pushes code changes to github
git status
git add .
git status
git commit -m "$1"
git push
