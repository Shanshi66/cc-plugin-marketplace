#!/usr/bin/env python3
"""
Claude Code Hook: 记录用户 Prompt 到 .chat 文件夹

每次用户提交 Prompt 时，将其记录到项目根目录的 .chat 文件夹下。
按日期创建 markdown 文件，同一天的 Prompt 记录在同一个文件中。
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def main():
    # 从 stdin 读取 hook 输入
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON input: {e}", file=sys.stderr)
        sys.exit(1)

    # 提取必要字段
    prompt = input_data.get("prompt", "")
    cwd = input_data.get("cwd", "")

    if not prompt or not cwd:
        print("Error: Missing required fields (prompt or cwd)", file=sys.stderr)
        sys.exit(1)

    # 创建 .chat 目录
    chat_dir = Path(cwd) / ".chat"
    chat_dir.mkdir(exist_ok=True)

    # 获取当前日期和时间
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    # 确定 markdown 文件路径
    md_file = chat_dir / f"{date_str}.md"

    # 检查文件是否存在，决定是创建新文件还是追加
    if md_file.exists():
        # 追加到现有文件
        with open(md_file, "a", encoding="utf-8") as f:
            f.write(f"\n---\n\n")
            f.write(f"**{time_str}**\n\n")
            f.write(f"{prompt}\n")
    else:
        # 创建新文件
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(f"# {date_str}\n\n")
            f.write(f"**{time_str}**\n\n")
            f.write(f"{prompt}\n")

    print(f"Prompt logged to {md_file}")


if __name__ == "__main__":
    main()
