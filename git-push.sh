#!/bin/bash

# Working directory
working_dir="/home/apkfuel/htdocs/images.apkfuel.com"

# Change directory
cd "$working_dir"

# Full path to Git executable
git_executable="/usr/bin/git"

echo "Working Directory: $working_dir"

# Check Git version
git_version="$($git_executable --version)"
echo "Git Version: $git_version"

# Check Git status
git_status="$($git_executable status)"
echo "Git Status:"
echo "$git_status"

# Git commands
$git_executable add .
$git_executable commit -m "$(date +'%Y-%m-%d %H:%M:%S')"
$git_executable fetch
$git_executable pull
$git_executable push -u origin master
echo "Git operations completed successfully"
