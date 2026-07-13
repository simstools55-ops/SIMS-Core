# SIMS-Core

SIMS-Coreは、SIMS-Blog-Managerまたは利用者から渡されたSEO改善依頼を、ClaudeなどのAIで実行するためのProductionパッケージです。

## 現在のリリース

Production Claude Package R2（UAT Ready）

## 現行インターフェース

- 入力：`SIMS_REQUEST_TEXT_V1`（自然文形式）
- 出力：`SIMS_FEEDBACK_V1` version `1.1`（回答末尾のJSON）

SIMS-Blog-Manager側をJSON入力へ変更する必要はありません。

## Claudeへの登録

`distribution/SIMS-Core-Claude-Upload/`だけを使用します。

1. `01_Project_Instructions/CLAUDE_PROJECT_INSTRUCTIONS.md`をClaude Projectの「手順」へ貼り付ける。
2. `02_Project_Knowledge/`の6ファイルを「コンテキスト」へ登録する。
3. SIMS-Blog-Managerの改善依頼文をClaudeへ貼り付ける。

詳細は`docs/setup-guide.md`を参照してください。

## 開発資産

- `product/contracts/`：正式な入出力契約
- `claude/`：Claude向け原本
- `tests/`：実記事UAT
- `tools/validate_feedback.py`：Feedback JSON検証
- `distribution/`：利用者向けClaude登録パッケージ
