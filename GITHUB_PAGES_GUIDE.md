# GitHub Pages 启用指南

## 🔍 问题诊断

访问 https://yqqq727.github.io/dshw-p01/ 显示 404 错误

## ✅ 解决步骤

### 步骤 1：检查 GitHub Actions 运行状态

1. 访问：https://github.com/yqqq727/dshw-p01/actions
2. 查看 "Quarto Publish" workflow
3. 如果显示 ⚫️（灰色）或 🟡（黄色），说明正在运行或等待运行
4. 如果显示 ❌（红色），说明构建失败，查看日志

### 步骤 2：手动触发 GitHub Actions（如果需要）

1. 访问：https://github.com/yqqq727/dshw-p01/actions
2. 点击左侧 "Quarto Publish"
3. 点击右侧 "Run workflow" 按钮
4. 选择 "main" 分支
5. 点击绿色 "Run workflow" 按钮

### 步骤 3：启用 GitHub Pages（重要！）

1. 访问：https://github.com/yqqq727/dshw-p01/settings/pages
2. 在 "Build and deployment" 部分：
   - **Source**: 选择 "GitHub Actions"
   - 点击 "Save" 保存
3. 等待几分钟，GitHub Pages 会自动启用

### 步骤 4：等待构建完成

- **首次构建**: 通常需要 3-5 分钟
- **后续构建**: 通常需要 1-3 分钟

构建成功后：
1. 访问：https://github.com/yqqq727/dshw-p01/actions
2. 看到 "Quarto Publish" 显示绿色 ✅
3. 访问：https://yqqq727.github.io/dshw-p01/
4. 应该能看到电子书了！

## 🔧 如果还是打不开

### 检查 1：确认 _book 目录是否生成
访问：https://github.com/yqqq727/dshw-p01/tree/gh-pages

如果看到 `index.html` 文件，说明部署成功！

### 检查 2：清除浏览器缓存
- 按 `Ctrl + F5` 强制刷新
- 或使用隐私模式/无痕模式访问

### 检查 3：等待 DNS 传播
- GitHub Pages 域名可能需要几分钟才能生效
- 最多等待 10 分钟后再试

## 📊 预期结果

成功后，访问 https://yqqq727.github.io/dshw-p01/ 应该看到：
- 项目标题 "P01: 金融数据获取、管理与初步分析"
- 左侧导航栏
- 3个章节的链接
- 专业的排版和样式

## 🆘 仍然有问题？

如果按照以上步骤操作后仍然打不开，请：
1. 检查 GitHub Actions 日志，看是否有错误信息
2. 确认仓库是公开的（public）
3. 重新运行 workflow

---

**祝成功！** 🎉
