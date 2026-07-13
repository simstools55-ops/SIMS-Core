# SIMS_FEEDBACK_V1 version 1.1

## 1. 目的

記事改善後の結果をSIMS-Blog-Managerへ戻すための機械可読フィードバックです。

## 2. 出力位置

- 回答の最後にJSONコードブロックを必ず1つだけ出力する。
- JSONコードブロックより後に文章を追加しない。
- JSON内にコメント、Markdown、末尾カンマを入れない。

## 3. 整合規則

- 実際に変更した項目だけ `changes` を `true` にする。
- 変更していない項目は `false` にする。
- 変更後の値が存在しない `new_values` は空文字にする。
- `article_id` と `article_url` は依頼文の値をそのまま返す。
- `completed_at` は実行日を `YYYY-MM-DD` で返す。
- 本文で提示した変更とJSONの変更フラグを一致させる。
- `summary` は実施内容を短く具体的に記録する。
- `warnings` は本当に必要な注意だけを配列で返す。

## 4. 列挙値

- `improvement_type`: `minor` / `normal` / `major`
- `confidence`: `high` / `medium` / `low`
- `next_action`: `monitor` / `remeasure` / `rewrite` / `none`
- `recommended_review_days`: `7` / `14` / `30`

## 5. 判定目安

### improvement_type

- `minor`: メタデータ、軽微な導入文、FAQなど限定的変更
- `normal`: タイトル、導入、見出し、複数本文節の改善
- `major`: 検索意図の再設計、構成変更、大幅な本文改稿

### confidence

- `high`: 入力情報と記事内容が十分で、改善根拠が明確
- `medium`: 一部情報が不足するが、妥当な改善が可能
- `low`: 本文未確認、意図の競合、重要情報不足などがある

### next_action

- `monitor`: 改善後に経過観察
- `remeasure`: データ不足または短期間で再測定
- `rewrite`: 追加の大幅改稿が必要
- `none`: 追加対応不要
