# 專案初步盤點

## Repository
- Repository：u6rmp602-afk/homework_2026
- 預設分支：main
- 維護分支：maintenance/initial-audit

## 已確認的現況
- README 定義的主要作業是 BMI 計算程式，要求檔名為 BMI 加上語言副檔名。
- 原始碼中有 TodoList.py，但根目錄尚未看到 BMI.py。
- gitignore 檔名缺少開頭的點，因此 Git 不會把它當成標準 .gitignore 設定檔。
- TodoList.py 讀取 JSON 後只檢查最外層是否為 list，尚未驗證每筆資料的欄位與型別；格式不符的資料可能造成例外。
- docs/BMI_ACCEPTANCE.md 是待核定草案，不能視為已正式公告的評分規範。

## 本次維護方向
1. 新增符合 README 命名規則的 BMI.py。
2. 新增標準函式庫 unittest 測試。
3. 新增標準 .gitignore。
4. 保留原有 TodoList.py 與課程提供的 README、驗收草案及 PR 範本，不擅自刪改課程文件。

## 測試狀態
- 尚未在 GitHub Actions 或其他 CI 環境執行。
- 新增測試涵蓋 8 筆 BMI 參考案例、非正數、非數值及非有限數值。
