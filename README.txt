
华夏离线批量编辑器 v2.3.6-r6g（稳定性修复）
- 修复：正则误写（\d）→ \d，恢复 CSV/TXT/Excel 导入、12位行号识别、代发/批量导入校验；
- 强化：表头清洗（去BOM和空格）、金额解析容错（支持1,234.56）；
- 保留：多编码导入（GB18030/BIG5-HKSCS/CP950等）与中文反乱码、背景图、四向滚动、自适应对话框；
- 导出：代发（无表头，文本格式）、批量（含表头，文本格式）。

本地打包：
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  pyinstaller app_exact.spec
  python build_exe.py --onefile
