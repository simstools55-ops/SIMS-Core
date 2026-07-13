# Feedback Acceptance Criteria

A000012 UATでは次を確認します。

- ArticleIDとURLが正しい
- タイトル、導入、見出し、FAQの実施内容と変更フラグが一致する
- 変更していない項目はfalse
- new_valuesに実際の新タイトル等が入る
- improvement_type、confidence、next_actionが許可値
- recommended_review_daysが7/14/30
- JSONが回答末尾に1つだけ
- 記事の良い部分を残した差分改善になっている
- 一般論ではなくコピペ可能な改善文がある
