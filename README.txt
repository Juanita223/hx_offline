
华夏离线批量编辑器 v2.3.6-r6
- CSV/Excel/TXT 导入：多编码（UTF-8/GBK/GB18030/UTF-16…）+ 自动分隔符；无表头回退。
- CSV 编码自动打分选择（优先看 LNAME/名称列的中文占比），避免“读成乱码也算成功”。
- 名称反乱码：导入 CNAPS.LNAME / IBPS.name 时尝试 UTF-8↔GBK/latin1 的常见错码修复，仅在中文占比显著提升时生效。
- 库维护导入→自动刷新；表格四向滚动；对话框自适应；背景图在表格内可见且透明度可调。
- 代发工资：导出无表头；批量转账：行别信息类型支持空值；选择“华夏银行”→自动行内转账。
- 打包：requirements 固定 numpy==2.0.1；spec/脚本显式收集 numpy，解决“Unable to import numpy”。

本地一键打包：
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  pyinstaller app_exact.spec
  #（可选单文件）python build_exe.py --onefile
