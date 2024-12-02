#!/bin/bash

# Define the base directory
BASE_DIR="app"

# Create directories
mkdir -p $BASE_DIR/models
mkdir -p $BASE_DIR/schemas
mkdir -p $BASE_DIR/crud
mkdir -p $BASE_DIR/routes
mkdir -p $BASE_DIR/utils

# Create main files
touch $BASE_DIR/__init__.py
touch $BASE_DIR/main.py
touch $BASE_DIR/database.py
touch $BASE_DIR/config.py

# Create files in subdirectories
for subdir in models schemas crud routes; do
  touch $BASE_DIR/$subdir/__init__.py
  for file in user league team player match draft trade event waiver; do
    touch $BASE_DIR/$subdir/$file.py
  done
done

# Create utility files
touch $BASE_DIR/utils/__init__.py
touch $BASE_DIR/utils/security.py
touch $BASE_DIR/utils/dependencies.py

# Create requirements file
touch requirements.txt

echo "Directory and file structure created successfully!"
