#!/usr/bin/env python3
"""
合并三个 Jupyter Notebooks 为一个完整的报告
"""
import json
import os
from datetime import datetime

# 读取三个 notebooks
def read_notebook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# 写入合并后的 notebook
def write_notebook(nb, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

print("[INFO] Reading notebooks...")
nb1 = read_notebook('01_download.ipynb')
nb2 = read_notebook('02_clean.ipynb')
nb3 = read_notebook('03_analysis.ipynb')

print("[INFO] Merging notebooks...")
# 创建新的 notebook 结构
merged_nb = {
    "cells": [],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.11.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# 添加标题单元格
title_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [
        "# P01: 金融数据获取、管理与初步分析 - 完整报告\n",
        "\n",
        f"**生成时间**: {datetime.now().strftime('%Y年%m月%d日')}\n",
        "\n",
        "---\n",
        "\n",
        "## 📋 报告目录\n",
        "\n",
        "### 第一部分：数据获取与说明\n",
        "- 数据源介绍\n",
        "- 数据下载过程\n",
        "- 数据完整性检查\n",
        "\n",
        "### 第二部分：数据清洗与管理\n",
        "- 6步数据清洗流程\n",
        "- 数据质量评估\n",
        "- CSV vs Parquet 对比\n",
        "\n",
        "### 第三部分：统计分析与可视化\n",
        "- 描述性统计\n",
        "- 4张核心可视化图表\n",
        "- CAPM 模型回归分析\n",
        "- 投资启示与结论\n",
        "\n",
        "---\n"
    ]
}

merged_nb["cells"].append(title_cell)

# 合并所有单元格（保留每个 notebook 的结构）
for i, nb in enumerate([nb1, nb2, nb3], 1):
    # 添加章节分隔
    section_header = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            f"\n",
            f"{'='*80}\n",
            f"\n",
            f"# 第 {i} 部分：{'数据获取' if i==1 else '数据清洗' if i==2 else '统计分析与可视化'}\n",
            f"\n",
            f"{'='*80}\n",
            f"\n"
        ]
    }
    merged_nb["cells"].append(section_header)

    # 添加该 notebook 的所有单元格
    for cell in nb["cells"]:
        merged_nb["cells"].append(cell)

# 保存合并后的 notebook
output_file = 'report_complete.ipynb'
write_notebook(merged_nb, output_file)

print(f"[SUCCESS] Merged notebook created: {output_file}")
print(f"[INFO] Total cells: {len(merged_nb['cells'])}")
print(f"[INFO] Size: {len(json.dumps(merged_nb, ensure_ascii=False)) / 1024:.1f} KB")
print(f"\n[NEXT] Run this command to generate HTML:")
print(f"   jupyter nbconvert --to html {output_file} --output report.html")
