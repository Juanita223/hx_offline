
华夏离线批量编辑器 v2.3.6-r5
- 修复：CSV 多编码导入（UTF-8/GBK/GB18030/UTF-16 等），无表头自动识别，空表头回退。
- 修复：库维护导入后自动刷新显示。
- 修复：背景图在编辑表格内可见（Treeview 底纹），自适应缩放、透明度可调。
- 修复：GitHub/本地打包时 numpy 未打入导致启动报错（在 spec/脚本中显式收集 numpy，并固定 numpy==2.0.1）。
- 功能：代发工资导出无表头；批量转账“行别信息类型”支持空值；选择行号后自动带出银行名称并联动“华夏银行→行内转账”。
- UI：各对话框自适应尺寸；四向滚动条；菜单命名按你要求统一（“导入行号”“代发工资录入”“批量转账录入”）。

本地一键打包：
  python -m venv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  pyinstaller app_exact.spec
  #（可选）单文件：python build_exe.py --onefile
