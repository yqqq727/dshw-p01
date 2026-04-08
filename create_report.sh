#!/bin/bash
# 创建完整的分析报告

echo "正在生成完整的 report.html..."

# 使用 nbconvert 合并三个 notebooks
jupyter nbconvert \
  --to html \
  --execute \
  --ExecutePreprocessor.timeout=600 \
  01_download.ipynb 02_clean.ipynb 03_analysis.ipynb \
  --output report.html \
  --TagRemovePreprocessor.remove_cell_tags='{"remove_cell"}'

echo "✅ report.html 生成完成！"
