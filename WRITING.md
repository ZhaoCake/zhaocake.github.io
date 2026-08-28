# 博客编写规范

本博客基于 [Astro](https://astro.build) + [Fuwari](https://github.com/saicaca/fuwari) 模板。撰写新文章请遵循以下规范。

## 一、新建文章

```sh
pnpm new-post <filename>
# 例：pnpm new-post my-first-post
```

生成 `src/content/posts/<filename>.md`。也可在该目录手动新建 `.md` 文件。

## 二、Frontmatter 规范

每篇文章顶部 YAML frontmatter：

```yaml
---
title: 文章标题              # 必填
published: 2024-01-20       # 必填，发布日期 YYYY-MM-DD
image: "https://cnmiw.com/api.php?sort=CDNtop"  # 可选，封面图（默认用随机图 API）
description: 摘要描述        # 可选，列表页展示
tags: [标签1, 标签2]         # 可选
category: 分类名             # 可选
draft: false                # 可选，true 则不发布
lang: zh                     # 可选，与站点语言不同时设置
updated: 2024-02-01         # 可选，文章更新日期
---
```

字段定义见 `src/content/config.ts`。

## 三、正文书写

正文用 GitHub Flavored Markdown。Fuwari 额外支持以下扩展语法。

### 1. Admonitions 提示框

````md
:::note
普通提示
:::

:::tip
小技巧
:::

:::important
重要信息
:::

:::caution
注意事项
:::

:::warning
警告
:::
````

### 2. GitHub 仓库卡片

````md
::github{repo="ZhaoCake/systemc_simple_tutorial"}
````

渲染为带 star/fork 统计的仓库卡片。

### 3. 代码块（Expressive Code）

支持行号、可折叠区块、语言徽章、复制按钮。`shellsession` 语言不显行号。

````md
```ts
const x: number = 1;
```
````

折叠区块：在语言后加 `collapsed`。

### 4. 数学公式（KaTeX）

行内：`$E=mc^2$`。块级：

````md
$$
\int_0^1 f(x)\,dx
$$
````

### 5. 图片（PhotoSwipe 灯箱）

`![alt](./img.jpg)` 可点击放大。图片放 `src/assets/` 被 Astro 优化；放 `public/` 用绝对路径 `/xxx` 引用。

### 6. 其他内置特性

- 标题自动生成锚点（悬停显示 `#`，可复制链接）。
- TOC 目录自动生成（见 `siteConfig.toc`）。
- 上一篇/下一篇按 `published` 日期自动排序。
- spoiler 剧透块（hover 显示内容）。

## 四、注意事项

- **图片路径**：封面/正文图优先放 `src/assets/`（Astro 图片优化，build 时压缩）；`public/` 下的图用绝对路径引用（如 `/assets/asuka.png`）。
- **草稿**：`draft: true` 不发布，可用于暂存未完成文章。
- **文件名**：用日期前缀 `YYYY-MM-DD-xxx.md` 便于排序。
- **分类/标签**：`category` 单值字符串，`tags` 是字符串数组。
- **多语言**：站点默认中文（`zh_CN`），英文文章设 `lang: en`。

## 五、部署

push 到 `main` 分支后，`.github/workflows/deploy.yml` 自动 build 并部署到 GitHub Pages（`gh-pages` 分支）。站点地址：https://zhaocake.github.io/
