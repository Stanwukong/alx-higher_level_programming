#!/bin/bash
chmod u+x *.py
git add .
git status
git commit -m "$1"
git push
