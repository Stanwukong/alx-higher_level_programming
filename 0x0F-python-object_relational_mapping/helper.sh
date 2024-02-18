#!/bin/bash
chmod u+x *.py
git add .
git commit -m "$1"
git push
