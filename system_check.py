# -*- coding: utf-8 -*-
import os

def system_overview(base_path):
    summary = {}
    for root, dirs, files in os.walk(base_path):
        for file in files:
            ext = file.split('.')[-1].lower()
            summary[ext] = summary.get(ext, 0) + 1
    return summary

def find_duplicates(base_path):
    seen_sizes = {}
    duplicates = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith('.py'):
                fpath = os.path.join(root, file)
                size = os.path.getsize(fpath)
                if size in seen_sizes:
                    duplicates.append(fpath)
                else:
                    seen_sizes[size] = fpath
    return duplicates
