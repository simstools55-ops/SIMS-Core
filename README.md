# SIMS-Core

SIMS-Coreは、SIMS-Blog-Managerが生成する記事改善依頼を受け取り、Claudeなどの生成AIで記事改善を実行するための製品リポジトリです。

## Production Architecture Release 1

本リリースでは、旧SIMS-Claude-EngineのEngine中心構成を整理し、次の現行運用を正式仕様として固定します。

- 入力：人間と複数AIが読める自然文形式 `SIMS_REQUEST_TEXT_V1`
- 出力：記事改善結果と、回答末尾の `SIMS_FEEDBACK_V1` version `1.1`
- SIMS-Blog-Manager側の入力JSON化は必須としない
- Claude固有設定と、AI非依存の製品契約を分離する
- 内部Engineは利用者に意識させない

## リポジトリ構成

- `claude/`：Claude Projectへ設定する実装資産
- `product/`：AI非依存の製品仕様、契約、設計、移行資料
- `tests/`：実記事UAT用フィクスチャと期待結果
- `docs/`：セットアップ・運用資料
- `distribution/`：Claudeへ登録するファイルだけを集約した配布領域

## Claudeへの登録

1. `distribution/SIMS-Core-Claude-Upload/01_Project_Instructions/CLAUDE_PROJECT_INSTRUCTIONS.md` の本文をClaude Projectの「手順」へ貼り付けます。
2. `02_Project_Knowledge/` 内のMarkdownをClaude Projectの「コンテキスト」へ登録します。
3. 実際の改善依頼はSIMS-Blog-Managerからコピーしてチャットへ貼り付けます。

Release 1はProduction設計の確定版です。実記事UATを経て、Knowledgeと出力品質を調整します。
