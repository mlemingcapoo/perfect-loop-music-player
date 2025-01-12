# -*- mode: python ; coding: utf-8;
import os
import shutil
from pathlib import Path


# Define source and destination paths
project_root = os.path.abspath(SPECPATH)  # Use SPECPATH instead of __file__
source_data = os.path.join(project_root, 'data')
dist_path = os.path.join(project_root, 'dist')
dest_data = os.path.join(dist_path, 'data')


# source_gui = os.path.join(project_root, 'gui')
# dest_gui = os.path.join(dist_path, 'gui')

# Create clean data directory in dist
if os.path.exists(dest_data):
    shutil.rmtree(dest_data)
# if os.path.exists(dest_gui):
#     shutil.rmtree(dest_gui)

shutil.copytree(source_data, dest_data)
# shutil.copytree(source_gui, dest_gui)


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('data', 'data'),
        ('gui/index.html', 'gui'),
        ('gui/js', 'gui/js'),
        ('gui/resources', 'gui/resources'),
    ],
    hiddenimports=['playwright'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    Tree('data', prefix='data\\'),
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

