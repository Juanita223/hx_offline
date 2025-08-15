
import sys
import PyInstaller.__main__
args = [
    "--noconfirm","--clean","--windowed",
    "--name=华夏离线批量编辑器","--icon=icon.ico",
    "--collect-all=pandas","--collect-all=openpyxl","--collect-all=xlrd","--collect-all=PIL","--collect-all=numpy",
    "--add-data=bg.jpg;.","--add-data=icon.ico;.",
    "app_exact.py",
]
if "--onefile" in sys.argv:
    args.insert(0,"--onefile")
PyInstaller.__main__.run(args)
