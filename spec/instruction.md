# Prompt logo hook

我想为 Claude Code 写一个 Hook, 每次用户提交 Prompt 时, 将用户的 Prompt记录在项目根目录的 .chat 文件夹下。

.chat 文件夹下按日期创建 markdown 文件，文件名格式为 `YYYY-MM-DD.md`。同一天的 Prompt 记录在同一个文件中，按时间顺序记录, prompt 之间用 --- 分隔。文件的标题为当天日期。

请使用 Python 脚本实现这个功能，Hook 的输入格式是：

```json
{
  "session_id": "abc123",
  "transcript_path": "/Users/.../.claude/projects/.../00893aaf-19fa-41d2-8238-13269b9b3ca0.jsonl",
  "cwd": "/Users/...",
  "permission_mode": "default",
  "hook_event_name": "UserPromptSubmit",
  "prompt": "Write a function to calculate the factorial of a number"
}
```

请将脚本添加到 @better-claude-code/hooks 中，并更新 hooks.json 文件。
