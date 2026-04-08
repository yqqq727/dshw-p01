#!/usr/bin/env python3
"""
更新 README.md 中的 GitHub 仓库链接
使用方法：python update_readme.py https://github.com/你的用户名/dshw-p01
"""

import sys
import re

def update_github_links(readme_path, new_url):
    """更新 README.md 中的 GitHub 链接"""
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 替换所有 GitHub 链接
    original_content = content

    # 替换 shield.io badge
    content = re.sub(
        r'\[!\[GitHub\]\(https://img\.shields\.io/badge/GitHub-仓库-blue\.svg\]\(https://github\.com/[^)]+\)',
        f'[![GitHub](https://img.shields.io/badge/GitHub-仓库-blue.svg)]({new_url})',
        content
    )

    # 替换其他 GitHub 链接
    content = re.sub(
        r'https://github\.com/yourusername/dshw-p01',
        new_url,
        content
    )

    if content != original_content:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ 已更新 README.md 中的 GitHub 链接为: {new_url}")
        return True
    else:
        print("⚠️  未找到需要更新的链接")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方法: python update_readme.py https://github.com/你的用户名/dshw-p01")
        sys.exit(1)

    new_url = sys.argv[1]
    readme_path = "README.md"

    if not new_url.startswith("https://github.com/"):
        print("❌ 错误：请提供有效的 GitHub 仓库 URL")
        sys.exit(1)

    update_github_links(readme_path, new_url)
