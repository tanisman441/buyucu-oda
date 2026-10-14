"""Syntax-check the game's inline module script with Node (no browser needed).

Usage: python tools/check.py   -> exits non-zero and prints the error on a syntax problem.
"""
import os, re, subprocess, sys, tempfile

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(root, 'index.html'), encoding='utf-8').read()
scripts = re.findall(r'<script type="module">(.*?)</script>', html, re.S)
if not scripts:
    sys.exit('index.html: <script type="module"> bulunamadi')
with tempfile.NamedTemporaryFile('w', suffix='.mjs', delete=False, encoding='utf-8') as f:
    f.write(scripts[0])
    path = f.name
try:
    r = subprocess.run(['node', '--check', path], capture_output=True, text=True)
finally:
    os.unlink(path)
if r.returncode:
    print(r.stderr)
    sys.exit(1)
print('ok: index.html modul betigi sozdizimi temiz')
