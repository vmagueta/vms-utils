#!/usr/bin/env python3

"""
rename_files.py

This script renames files in a given directory by replacing a specified
filename prefix with a new one. 
It only affects files that start with the given prefix.

Example:
  Original: vms_blabla_blablabla_blablabla.png
  New: victorMaguetaSoler_blabla_blablabla_blablabla.png

Usage:
  1. Run the script.
  2. Enter the folder path.
  3. Enter the current prefix (e.g., 'vms').
  4. Enter the separator (e.g., '_').
  5. Enter the new prefix (e.g., 'victorMaguetaSoler').

Author: Victor Magueta
"""

import os

def rename_files_in_path():
    """
    Rename files in the specified directory by replacing a prefix.
    """
    path = input("Enter the path to the folder: ").strip()
    os.chdir(path)
    current_prefix = input("Enter the current prefix: ").strip()
    separator = input("Enter the separator: ").strip()
    new_prefix = input("Enter the new prefix: ").strip()

    for filename in os.listdir(path):
        if filename.startswith(current_prefix):
            new_filename = filename.replace(current_prefix, new_prefix, 1)
            os.rename(filename, new_filename)
            print(f"Renamed: {filename} -> {new_filename}")
        else:
            print(f"Skipped: {filename} (does not start with {current_prefix})")


if __name__ == "__main__":
    rename_files_in_path()
