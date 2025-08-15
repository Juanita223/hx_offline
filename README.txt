
华夏离线批量编辑器 v2.3.6-r6f（编码增强）
- CNAPS/IBPS 导入：新增“编码：自动/UTF-8/GBK/GB18030/UTF-16/Latin1/BIG5-HKSCS/BIG5/CP950”，
  解决港澳台/境外名称（如“(香港地区)TAIWAN_SHIN_KONG_BK_HK”）在部分源文件中的解码问题。
- 自动编码评分：中文占比 + 0.05*ASCII 占比 - 0.7*乱码惩罚，降低误判 latin1/错误 utf-8。
- 名称列导入带轻量反乱码，仅在可读性显著提升时替换；“工具→修复已导入乱码…”可批量修复历史数据。
- 背景图热修、四向滚动、对话框自适应、代发工资无表头导出等均已包含。

GitHub 自动出 EXE：推到 main/master 即在 Actions Artifact 获取 dist 目录与单文件 EXE。
本地打包：
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  pyinstaller app_exact.spec
  python build_exe.py --onefile
