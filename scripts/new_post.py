#!/usr/bin/env python3
"""按日期创建新博客文章模板。

用法:
    python scripts/new_post.py                     # 以今天日期创建
    python scripts/new_post.py --date 2026-09-01   # 指定日期创建
    python scripts/new_post.py --title 我的标题     # 直接填好标题
    python scripts/new_post.py --edit              # 创建后用默认编辑器打开

文件名格式为 YYYY-MM-DD.md，若当天已存在同名文件，
则依次追加 -1、-2 等后缀（与现有文章命名习惯一致）。
"""

import argparse
import datetime
import os
import subprocess
import sys
from typing import Optional

POSTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "content", "posts")


def build_filename(date: datetime.date) -> str:
    """确定不冲突的文件名: YYYY-MM-DD.md 或 YYYY-MM-DD-N.md"""
    base = date.isoformat()
    candidate = f"{base}.md"
    if not os.path.exists(os.path.join(POSTS_DIR, candidate)):
        return candidate
    n = 1
    while True:
        candidate = f"{base}-{n}.md"
        if not os.path.exists(os.path.join(POSTS_DIR, candidate)):
            return candidate
        n += 1


def build_content(date: datetime.date, title: Optional[str]) -> str:
    title = title if title else "TODO: 标题"
    return f"""---
title: {title}
published: {date.isoformat()}
description: "TODO: 描述"
tags: [TODO]
category: "TODO"
draft: true
lang: zh
---

TODO: 正文内容
"""


def open_in_editor(path: str) -> None:
    editor = os.environ.get("EDITOR")
    try:
        if editor:
            subprocess.run([editor, path], check=False)
        elif sys.platform == "win32":
            os.startfile(path)  # type: ignore[attr-defined]
        else:
            subprocess.run(["xdg-open", path], check=False)
    except OSError as e:
        print(f"无法打开编辑器: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="创建新博客文章模板")
    parser.add_argument("--date", help="发布日期 (YYYY-MM-DD)，默认今天")
    parser.add_argument("--title", help="文章标题，默认留 TODO 标志")
    parser.add_argument("--edit", action="store_true", help="创建后用编辑器打开")
    args = parser.parse_args()

    if args.date:
        try:
            date = datetime.date.fromisoformat(args.date)
        except ValueError:
            sys.exit(f"日期格式错误: {args.date}，应为 YYYY-MM-DD")
    else:
        date = datetime.date.today()

    os.makedirs(POSTS_DIR, exist_ok=True)
    filename = build_filename(date)
    path = os.path.join(POSTS_DIR, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(build_content(date, args.title))

    print(f"已创建: {path}")
    print("记得填写 title / description / tags / category 等 TODO 项")

    if args.edit:
        open_in_editor(path)


if __name__ == "__main__":
    main()
