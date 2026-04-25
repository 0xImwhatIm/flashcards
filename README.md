# Flashcards

這是一個單頁版的英文閃卡練習工具，目前主要用於小學六下英語期中範圍的字卡練習。網頁入口檔案為 `index.html`，可直接用瀏覽器開啟，也已部署到 GitHub Pages。

## 線上版本

GitHub Pages:

https://0ximwhatim.github.io/flashcards/

## 目前功能

- Learn 模式：瀏覽字卡、圖片、發音與音標。
- Spell 模式：聽發音後輸入單字，練習拼字。
- Spell 分數統計：完成練習後顯示答對、答錯題目。
- 錯題複習：Spell 練習完成後，可針對答錯的題目再複習。
- SVG 圖卡優化：持續調整插圖辨識度，保留童趣但避免明顯誤導。
- Auto Read：切換是否自動朗讀。
- Auto 模式：自動播放下一張字卡。
- Shuffle：重新洗牌字卡順序。
- Speed：調整自動播放速度。

## 最新版本調整

- 將網頁主檔名改為 `index.html`，方便 GitHub Pages 自動作為首頁。
- 新增 `.gitignore`，避免提交 macOS 的 `.DS_Store`。
- 新增並整理 README 專案說明。
- 設定 GitHub Pages，使用 `main` 分支與 `/(root)` 資料夾部署。
- 重新觸發 Pages build，確認線上網址可正常開啟。
- 調整 TTS 發音設定，優先選擇較標準、清楚的英文語音，避免特殊效果或沙啞聲音。
- 將 `Golden Necklace` 修正為 `Gold Necklace`。
- 將相關音標修正為 `/ɡoʊld ˈnɛk.ləs/`。
- 在 Spell 模式加入 30 題完成後的答對/答錯統計。
- 在 Spell 模式加入錯題複習功能。
- 第一輪插圖辨識優化：調整 `Straight Brown`、`Navy Tie`、`By Train`。
- 第二輪插圖辨識優化：調整 `By Subway`、`Star Bridge`。

## 工作紀錄

1. 讀取專案資料夾，確認原本只有一個 `flashcards.html`。
2. 將 `flashcards.html` 改名為 `index.html`。
3. 建立第一版 `README.md`，記錄未來可擴充方向。
4. 初始化 git repository，建立 `main` 分支。
5. 搜尋並確認 GitHub repo：`0xImwhatIm/flashcards`。
6. 將本地專案連接到遠端 repo，提交並推送第一版。
7. 協助設定 GitHub Pages：
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/(root)`
8. 透過空 commit 重新觸發 GitHub Pages build。
9. 確認 Pages build and deployment 成功完成。
10. 依照使用回饋，改善朗讀語音清晰度。
11. 修正字卡文字與發音：`Golden Necklace` -> `Gold Necklace`。
12. 依照使用需求，評估 Spell 分數統計功能；實作難度不高，因為原本已有正誤判定，只需補上結果紀錄、完成畫面與錯題 deck。
13. 在 Spell 模式完成後顯示答對清單、答錯清單與總分。
14. 新增 `Review Wrong Words`，可將答錯題目重新組成一輪 Spell 複習。
15. 針對圖卡辨識性進行第一輪 review 與修正，優化 `Straight Brown`、`Navy Tie`、`By Train`，讓髮型、領帶與火車輪廓更容易第一眼辨識。
16. 進行第二輪圖卡辨識優化，調整 `By Subway` 與 `Star Bridge`，讓地鐵與火車的差異更清楚，並讓橋的主體辨識度高於名稱裝飾。

## 未來可擴充方向

這個版本之後還可以繼續擴充，例如：

1. 補齊或加入更多六下的學習範圍。
2. 延伸到國中或高中的學習範圍。
3. 增加考試範圍的複習模式，例如三卡複習。
4. 增加單字分類篩選或指定範圍練習。
5. 加入錯題紀錄與再次複習機制。
6. 儲存歷史成績，方便追蹤多次練習的進步狀況。
7. 建立整體圖卡辨識性巡檢流程，持續修正容易混淆的插圖。

## 檔案說明

- `index.html`：主要閃卡網頁。
- `README.md`：專案說明與未來擴充備註。
- `.gitignore`：排除不需要提交到 GitHub 的系統檔案。
