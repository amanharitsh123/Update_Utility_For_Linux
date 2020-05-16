import subprocess, os

def process_query(inp, data):
    print("Running ", data)
    out = None
    os.system(data)