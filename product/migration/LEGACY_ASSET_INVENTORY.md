# Legacy Asset Inventory

旧 `SIMS-Claude-Engine` の資産を次の方針で移行します。

## 統合して継承

- `claude/instructions/CLAUDE_PROJECT_INSTRUCTIONS.md`
- `claude/engines/SEO_IMPROVEMENT_ENGINE.md`
- `claude/engines/QUALITY_ENGINE.md`
- `claude/knowledge/KNOWLEDGE_POLICY.md`
- `docs/CLAUDE_ENGINE_INTERFACE_SPEC_v1.0.md`

これらの中核原則をProduction版のInstructions、Knowledge、契約書へ統合します。

## UAT時に参照

- Engine01〜Engine10
- Engine v2系監査資料
- 品質チェックリスト
- Improvement Resultテンプレート群
- Exchange Processor関連仕様

内容を比較し、現行運用に必要なルールだけを採用します。

## Claude Projectへ直接登録しない

- `legacy/`
- `docs/`
- `product/audits/`
- 重複した旧テンプレート
- Apps Script・Spreadsheet・GitHub運用資料
- Knowledge Masterの管理用ファイル

## 保留

- カテゴリ別Knowledge
- 内部リンク一覧
- Knowledge Master.xls

ブログ固有データとして有効ですが、Production共通Knowledgeへ混在させません。将来、ブログプロフィールまたはサイト別追加Knowledgeとして扱います。
