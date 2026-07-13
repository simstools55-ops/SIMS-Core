# UAT Checklist

## 入力処理

- [ ] ArticleIDを正しく認識した
- [ ] URLを正しく認識した
- [ ] メインクエリを正しく認識した
- [ ] GSC数値を取り違えていない
- [ ] 改善目的と優先箇所を守った

## 改善品質

- [ ] 一般論ではなく完成文がある
- [ ] タイトル案が検索意図と本文に一致する
- [ ] 導入文で結論が早く示される
- [ ] 見出しの回答順序が明確
- [ ] FAQが本文の単純重複ではない
- [ ] 未確認情報を捏造していない

## Feedback JSON

- [ ] JSONは1つだけ
- [ ] JSONは回答末尾
- [ ] ArticleIDとURLが正しい
- [ ] changesが出力内容と一致
- [ ] new_valuesが提示値と一致
- [ ] 列挙値が契約内
- [ ] recommended_review_daysが7・14・30
- [ ] JSONの後に文章がない

## 判定

- [ ] PASS
- [ ] CONDITIONAL PASS
- [ ] FAIL
