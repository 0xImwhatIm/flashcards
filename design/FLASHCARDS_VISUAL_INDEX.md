# FlashCards Visual Index / 視覺索引依據

> Status: `v0.1.1 + semantic v0.2 / user-selected final image set wired / character system approximately 85% defined`
>
> Created: 2026-09-20 (Asia/Taipei)
>
> Scope: ImageGen、Codex、Figma 與前端設計系統的共同視覺依據

> Related pilot manifest: `design/ILLUSTRATION_MANIFEST_UNIT1_UNIT2_PILOT.md`
>
> Related semantic revision: `design/SEMANTIC_DISAMBIGUATION_V0.2.md`
>
> Related batch: `design/ILLUSTRATION_BATCH_WAVE_01_SPATIAL.md`

> Related batch: `design/ILLUSTRATION_BATCH_WAVE_02_CONCRETE.md`

> Related batch: `design/ILLUSTRATION_BATCH_WAVE_03_EVERYDAY_OBJECTS.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_04_HOME_SOCIAL.md`

> Coverage inventory: `design/ILLUSTRATION_COVERAGE_INVENTORY.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_05_COLOR_GRAMMAR.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_06_ABSTRACT_GRAMMAR.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_07_PEOPLE_ROLES.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_08_FAMILY_ROLES.md`

> Generated batch: `design/ILLUSTRATION_BATCH_WAVE_09_SCHOOL_GREETINGS.md`

> Final selection record: `design/FINAL_IMAGE_SELECTION_2026-09-21.md` (63 user-selected assets, including the four Wave 12 Unit 1 repairs, covering all 63 Unit 1／Unit 2 words)
>
> Wave 10/11 selected: `design/ILLUSTRATION_BATCH_WAVE_10_TRAITS_EXPRESSIONS_PLAN.md` (`Woman` + `Young` + `New` + `Really v2` + `Very v2` + `Handsome` + `Beautiful`) and `design/ILLUSTRATION_BATCH_WAVE_11_RIGHT_SPATIAL.md` (`Right` turn-right asset); `Really v1`／`Very v1` remain history.
>
> Spatial overlay spec: `design/SPATIAL_INSTRUCTIONAL_OVERLAYS_V0.1.md`

> Wave 12 repair: `design/ILLUSTRATION_BATCH_WAVE_12_UNIT1_REPAIR.md`

> Wave 13 expansion: `design/ILLUSTRATION_BATCH_WAVE_13_UNIT2_EXPANSION.md` (`Above` + `Enough` + `Person`, review-ready candidates)

## 1. 定錨與權威範圍

### 正式定錨圖

- Project path: `assets/unit2/Codex 圖像 2026年9月20日 上午10_24_38.png`
- Canvas: 1254 × 1254 px, RGB PNG, 1:1
- SHA-256: `ad045f91e3254daad72fcd83262193f50fb5bc9bfe19f33098323d01fa1da233`

這張圖是目前角色造型與插畫語言的 primary visual anchor。它定義「角色身分、線條、色彩傾向、材質、構圖節奏與情緒」，但不直接定義 app 介面排版、字體或互動元件。

### House semantic anchor｜2026-09-20

- Project path: `assets/visual-prototypes/batch-v0.2/wave-02-concrete/house-anchor.jpg`
- Canvas: 1254 × 1254 px, RGB JPEG, 1:1
- SHA-256: `2e116e52ad6b468ca52ac25bdb019e5912ea13de3280c2c714228d974629a4d3`
- Role: approved reference and selected House card asset; it does **not** replace the global mascot anchor above.
- Additional semantic cues: pointing pose, slate-blue roof, sparse house vignette, short grass marks and warm cream facade.
- Consistency note: the mascot retains the compact bean body, three rounded back plates, dot eyes, short curved mouth, rounded limbs, charcoal contour and warm paper field. Its slightly darker green and more visible low tail are now the preferred House-specific reference cues.

### 與既有前端的關係

目前 `index.html` 內已有未提交的 Junior editorial UI 樣式與 `--jr-*` tokens。這份文件不覆寫該工作，也不宣稱兩者已完成同步；它先建立插畫層的單一依據。若日後將本文件 tokens 寫入 CSS 或 Figma Variables，應另開一次明確的設計同步變更。

2026-09-21 的本地整合在 `index.html` 以明確的 `IMAGE_OVERRIDES` 對照表接入使用者選定的 63 張圖；Wave 12 已將 `Too`、`Son`、`Office Worker`、`Cousin` 改為小恐龍規範版本，`But` 則依使用者決定改選 v1。`Colorful` 已在 Unit 2 字彙陣列中。2026-09-22 的 Wave 13 再加入 `Above`、`Enough`、`Person`、`People` 四個 Unit 2 字彙與 review-ready 圖像候選。這代表本機工作樹目前有 67 個已接圖字彙，其中 63 個是 final-selection set、4 個等待盲測確認；仍不等同 Git commit 或已發佈版本。

### Prototype 的地位

本批 v0.1／v0.2 圖片都是壓力測試與可用原型，不是新的定錨圖。若 prototype 與定錨圖衝突，定錨圖優先。

### 2026-09-20 角色數量決策

- 角色設定由 owner 評估為約 **85% 完成**；目前已足以進入真實單字的分批驗證，但仍保留 15% 給多人關係、年齡／身份差異、背面／側面與 production QA 修正。
- 系統固定的是同一套 mascot visual grammar，不是「每張只能有一個角色」。
- 場景可依語意使用 1–3 個角色；`classmate`、`cousin`、`family`、`too`、`husband`／`wife` 等關係型單字，應允許第二或第三個角色協助說明。
- 多角色圖仍只保留一個主要語意和一個主要視覺焦點；配角必須有明確語意功能，不能只是填滿留白。
- 本規則已進入 v0.2 語意擴充：主角維持 anchor，但可加入三角龍、甲龍、鳥、小型哺乳動物或必要的人物角色；詳見 `design/SEMANTIC_DISAMBIGUATION_V0.2.md`。

## 2. 一句話 Visual DNA

以大面積暖白留白承托一個圓潤、友善、略帶手繪不規則的綠色小怪獸；用厚實近黑墨線、低飽和自然色、非常輕微的紙張／顏料質感，講清楚一個可在縮圖辨識的單一情境。

## 3. 角色造型索引

### 3.1 必須保留的識別特徵

1. **整體輪廓**：頭與身體連成一體的直立 bean / gumdrop 形，不另畫脖子。
2. **比例**：頭身不是寫實比例；上半身約占角色高度 55–65%，視覺重心低而穩。
3. **頂部**：圓拱頭頂，左右不要求鏡像，輪廓可有輕微手繪偏差。
4. **手臂**：短、圓、無手指；以水滴或軟管狀從軀幹延伸。
5. **腿腳**：兩隻短腳，腳底平貼基準線；不畫鞋、不畫趾頭。
6. **尾部**：背部向後下方延伸成低矮、柔軟的尾形，末端鈍圓；只要場景沒有語意上的遮擋，尾巴必須在畫面中清楚可見，不能因正面姿勢而省略。
7. **背棘**：canonical anatomy 為三片小而圓的背棘，尺寸由上到下可漸小；被背包或手臂遮擋時仍應讓至少兩片可辨識，資料與角色規格仍記為三片。
8. **眼睛**：兩個小型實心黑色橢圓／圓點，無眼白、睫毛、高光或眉毛。
9. **嘴巴**：一條短弧線；開口、牙齒與舌頭只在語意必要時使用，預設不用。
10. **皮膚色**：綠色為唯一主體色，可有很輕的 emerald → teal 明度／色相變化，不做高光塑膠感。

### 3.2 可變項

- 姿勢：站、坐、走、揮手、指向、雙手舉起。
- 表情：以嘴弧角度、眼距微調與姿勢傳達；表情零件越少越好。
- 配件：每張 0–2 件，必須服務單字或情境語意。
- 朝向：正面、3/4 側面；完全背面只在教學語意需要時使用。
- 背棘可因遮擋少見一片，但不可改成尖刺、翅膀或恐龍硬甲。
- Cast size：可使用 1–3 個角色；角色數由單字語意決定，不把「單角色」當成全域限制。
- 配角可沿用同一 mascot grammar，並以高度、身形、單一配件或受控的輔助色區分身份；不得靠堆疊臉部零件製造差異。
- Companion species：每個物種只保留一個辨識性輪廓 cue（例如三角龍的角、甲龍的尾槌、鳥的喙）；維持相同墨線、紙感與低彩度世界，不把每張圖變成隨機動物園。
- Semantic cast：`Parents` 預設為兩位大人＋一位孩子；`Family` 可擴展為 4–5 位、跨年齡／跨物種的群體；`Each Other` 必須呈現雙向互動，現階段優先使用兩個角色同時互相指向。
- Age comparison：`Young` 可使用同一 mascot grammar 的老年配角作為對比；老年角色最多加入一個受控年齡 cue（例如小鬍鬚／圓鬍鬚或手杖），並以身形、姿勢與色彩差異輔助。指向年輕者的單一短箭頭是「語意標示」，不是移動軌跡。

### 3.3 角色禁止項

- 不使用寫實人體比例、肌肉、關節、手指或腳趾。
- 不增加鼻子、眉毛、眼白、瞳孔高光、牙齒等臉部零件。
- 不任意改成其他主色，不加服裝作為永久身分特徵。
- 不做毛茸茸、黏液、金屬、玻璃或高光 3D 材質。
- 不將輪廓變成完美對稱向量或 anime / kawaii 大眼風格。

### 3.3a 性別語意提示（受控例外）

性別提示只能服務明確的單字語意，不是角色的永久設定。當單字需要區分成人性別（例如 `Woman`，或日後經審核的 `Aunt`／`Wife`）時，每張圖最多選用**一種**稀疏的小提示：淡珊瑚口紅、極淡腮紅，或一至兩筆簡化睫毛。三者不可同時堆疊，也不可把提示擴散到 canonical anchor、一般場景或非性別單字。不得變成濃妝、時尚造型或刻板化身分；綠色 bean 身體、點狀眼睛與短弧嘴仍保持不變。`Woman` 目前使用的是受控的珊瑚色圍巾，而不是臉部化妝。

### 3.3b 年齡與比較語意提示（受控例外）

`Young`、`Old` 或需要年齡比較的單字可以使用第二個角色，但兩者仍必須沿用同一套 bean／gumdrop 角色 grammar。老年 cue 只選一種主要提示（例如小鬍鬚／圓鬍鬚或手杖），不得加入寫實皺紋、白髮貼圖或新的臉部解剖。指向被比較者的短、靜態箭頭可以作為單字級 semantic highlight；它不代表移動方向，也不取代位置／移動 overlay 規則。

### 3.3c 程度與確認語意提示（2026-09-21 修訂）

- `Really?` 的目前教學義為「真的嗎？」。畫面優先使用主角歪頭、短暫抬手／停住、與提出主張的配角眼神互動，以及一個簡單被提出的物件；不使用問號、對話框或任何文字。配角只在提供「被確認的主張」時出現，不能變成無關的故事角色。`really-v2.png` 是目前 review candidate；`really-v1.png` 僅保留作歷史比較。
- `Very` 的目前圖像語法是「程度非常高」而非一個具體物件名稱：可用單一 anchor mascot 的誇張張嘴與高強度反應來表示高程度，但不得複製使用者提供的貓梗圖、背景或可辨識細節，也不得讓畫面變成單純 `Surprised`。`very-v2.png` 是目前 review candidate；`very-v1.png` 僅保留作歷史比較。
- 這兩個語意提示都不會改寫 canonical mascot anatomy；任何眉線、強烈張嘴或反應符號仍需另行通過 character-consistency QA，未通過時保持 `review-ready`／`semantic hold`，不可自動接入 production。

### 3.4 Character consistency lock｜絕對設定

語意通過不等於角色通過。每一張含有 anchor hero 的新圖，都必須另外通過以下鎖定條件；任何一項 `HOLD` 都不得升格為 production asset：

- 維持定錨圖的頭身輪廓與低重心比例；不得生成更長的脖子、更高更瘦的身體或不同的手臂比例。
- 低尾巴是角色識別的一部分；若畫面沒有合理遮擋，尾巴必須清楚可見。正面構圖本身不是省略尾巴的理由。
- 維持三片**小而圓**的背棘；被姿勢遮擋時至少兩片可辨識，不得變成大型尖刺或葉片。
- 手臂必須短、圓、無手指、無細長尖端；「互相指」只能用手臂方向與姿勢表達，不得破壞 anchor anatomy。
- 臉部預設只保留小黑點眼睛與短弧嘴；禁止腮紅、臉頰記號、眉毛、牙齒、額外斑點或高光。只有在上方「性別語意提示」明確批准的單字場景，才可加入一種極淡的口紅、腮紅或簡化睫毛提示；年齡比較場景可另依「年齡與比較語意提示」加入一個小鬍鬚／圓鬍鬚 cue。canonical anchor 本身永不加入這些例外。
- 腿腳不得畫腳趾線；綠色主體維持 `#18B985`／`#13A97C` 色系，不漂移成灰綠或高飽和螢光綠。
- 紙感只能是很輕的顆粒與顏料差；不得讓新圖的水彩／蠟筆紋理蓋過定錨圖的平面色塊。
- 每次 QA 必須分開記錄 `semantic pass` 與 `character pass`；前者通過、後者未通過時，狀態只能是 `character-consistency hold`。

## 4. 線條語言

- 主輪廓為 charcoal near-black，不是純幾何黑色向量感。
- 在 1254 px 方圖上，主輪廓視覺粗細約 8–12 px；內部細節約為主輪廓的 70–90%。
- 端點與轉角圓潤，保留輕微抖動、壓力差與不完全等距。
- 同一物件的外輪廓優先連續；內部分隔線只畫足以辨識的數量。
- 地面以單一細線建立，不畫透視網格；草叢／動作線每組 2–4 筆。
- 禁止極細灰線、機械式等寬描邊、鋒利尖角、重複密集紋理。

## 5. 色彩索引

以下是由定錨圖做「視覺取樣後正規化」的 operational tokens；原圖含柔和色差，不應把每一像素當作純色標準。

| Token | 建議值 | 用途 | 規則 |
|---|---:|---|---|
| `illustration.canvas` | `#F8F6F0` | 暖白背景 | 60–75% 畫面占比 |
| `illustration.ink` | `#202223` | 主輪廓與五官 | 避免純黑的數位銳利感 |
| `mascot.green.base` | `#18B985` | 角色主色 | 每張唯一高辨識主色 |
| `mascot.green.deep` | `#13A97C` | 角色微弱暗部 | 不超過主體 25% |
| `scene.cream` | `#F3EAD4` | 建築／卡片／紙面 | 維持溫暖，不用冷白 |
| `scene.blueGray` | `#86A8B7` | 屋頂、交通、燈具 | 低飽和，不能搶主角 |
| `scene.wood` | `#C8A687` | 木門、桌面、家具 | 可有少量顏料深淺 |
| `scene.sage` | `#86A47E` | 植物輔色 | 小面積使用 |
| `accent.mustard` | `#F2C44E` | 星星、燈光、重點 | 每張最多一個主 accent |
| `accent.coral` | `#EF735D` | 成功／提醒動作線 | 只作稀疏點綴 |
| `glass.paleAqua` | `#CDE5E2` | 玻璃／窗面 | 需以 ink 描邊定界 |

### 色彩節制規則

- 建議單張使用 1 個角色主色 + 2–4 個場景輔色 + 1 個 accent。
- 背景維持暖白，不用純白、全彩漸層或大面積飽和色。
- 對比由深色輪廓產生，不靠陰影或高飽和撞色。
- 若情境物件已有明確語意色，先降飽和，再保持可辨識性。

## 6. 構圖、留白與視覺節奏

### 定錨圖觀察

- 1:1 方形畫布。
- 主體群位於下半部，約落在畫布高度的 27–75%；上方保留大面積安靜留白。
- 角色在左、情境主物件在右，形成「角色 → 語意物件」的閱讀方向。
- 所有主要物件共用一條近水平基準線，避免漂浮。
- 角色與小屋形成一大一小、圓與三角屋頂的輪廓對比。
- 屋頂波線、窗格、門板與草叢以短線建立慢—快—慢節奏；沒有滿版裝飾。

### 可重複構圖規則

1. 畫面只講一個動詞或一個名詞情境。
2. 主要群組占畫面寬度約 60–82%，四周保留安全留白。
3. 主體通常放在下 55–65% 區域；上方不要為了「填滿」而加物件。
4. 角色面向、手勢或視線應引導到學習語意物件。
5. 附件依重要度排序：主語意物件 > 1–2 個支援物件 > 少量地面符號。
6. 先檢查 160 px 縮圖是否仍可理解，再檢查細節。
7. 多角色情境先指定 primary character、supporting character 與彼此關係；最多 3 個角色，並維持一個主要焦點。

### 禁止構圖

- 多角色、多事件、完整室內場景或城市背景同時出現。
- 背景物件排成素材庫拼貼，或使用滿版 pattern。
- 主要物件切出畫布、透視複雜、視覺中心不明。
- 用大量星星、彩帶、速度線或 emoji 補足空間。

## 7. 表情、情緒與敘事

- 基調：安全、溫和、好奇、可靠、略帶童趣但不幼兒化。
- 中性／學習：微笑弧線，眼睛保持小而穩定，姿勢表達專注。
- 困惑：嘴弧略平、身體微傾；不要加入誇張問號或皺眉，除非教學語意必要。
- 成功：手臂上舉、嘴弧上揚、1 個星形或少量動作線；不做勝負壓迫感。
- 錯誤／再試一次：使用鼓勵性的停頓與重新嘗試，不畫哭泣、羞辱或危險。
- 情緒主要依靠姿勢與單一重點物件，而不是複雜臉部動畫。

## 8. 材質、光影與背景

### 材質

- 平面插畫為主，帶非常輕微的紙張顆粒、鉛筆／水彩顏料色差。
- 色塊邊緣受墨線約束，不做油畫筆觸或數位噴槍光暈。
- 木、玻璃、布料只用 1–3 條內線或極小色差暗示，不追求寫實紋理。

### 光影

- 柔和、無明確方向的漫射日光。
- 可有非常淡的環境暗部或接觸陰影；不做長投影、rim light、強反射或 cinematic lighting。
- 立體感主要來自輪廓重疊與前後關係，不靠高反差明暗塑形。

### 背景

- 預設為暖白紙面，不畫牆角、天空地平線或空間漸層。
- 需要場景時，以一個主物件和少量符號交代，不建立完整環境。
- 基準線與少量草線可提供站立感；每側最多約 1–2 組。

## 9. 字體與文字

定錨圖內沒有文字，因此它不提供字體證據。插畫資產預設 **不烘焙任何單字、句子或 UI 標籤**；文字由前端／Figma 上層管理，以支援多語系、無障礙與資料更新。`Between` 的少量 `1`、`2` 與本批空間詞的方向／括號線，均只能作為獨立的 instructional overlay；箭頭與括號不得永久烘焙進 canonical raster，也不得擴散成一般裝飾。例外是已核准的 word-specific semantic mark：`Young` 的比較指示箭頭，以及 `Right` 交通號誌內的彎箭頭；它們是情境物件／語意標示，不是通用 UI overlay。詳見 `design/SPATIAL_INSTRUCTIONAL_OVERLAYS_V0.1.md`。

目前 repo 的 UI 使用 `Nunito` 與 `Fredoka One`，但這是既有產品層決策，不是由定錨圖推導。若要統一字體，應另行做 UI typography review，而不是在插畫內自行加入字樣。

## 10. ImageGen / Codex 生成規則

### 10.1 Reference 使用方式

- 將定錨圖標為：`Image 1: character identity and visual-style reference; not an edit target.`
- 新圖是 generation，不是重畫或局部編輯定錨圖。
- 每次 prompt 重述角色 invariant；不要只寫「same style」。
- 不直接使用在世藝術家姓名或受保護角色作為風格捷徑。

### 10.2 Master prompt（可複用）

```text
Use case: illustration-story
Asset type: square FlashCards semantic illustration
Primary request: Create a new scene using Image 1 only as the exact character identity and visual-style anchor. [ONE CLEAR SCENE / ACTION].
Input images: Image 1: character identity and visual-style reference; do not edit or reproduce the house scene.
Scene/backdrop: warm off-white empty paper background, one thin hand-drawn ground line, only the minimum props required for meaning.
Subject: use the number of characters required by the word meaning, normally 1–3. Keep one clear primary character and only semantically necessary supporting characters. All mascot characters must follow the anchor's shared visual grammar: bean-shaped body, rounded head-body silhouette, short rounded arms and feet, low soft tail, canonical three small rounded back plates (at least two visibly readable if one is naturally occluded), tiny black oval eyes, short curved mouth, friendly childlike proportions. Preserve the primary mascot's emerald-to-teal green identity; distinguish supporting roles only with controlled size, shape, one accessory, or a muted secondary color.
Style/medium: simple children's editorial illustration; thick charcoal-black hand-drawn outline with slight natural wobble; flat matte color fields with very subtle watercolor/colored-pencil tonal variation; no glossy 3D rendering.
Composition/framing: 1:1 square, full subject visible, main group in the lower half, generous calm negative space, strong silhouette readable at 160 px.
Lighting/mood: soft diffuse daylight; warm, safe, encouraging.
Color palette: emerald/teal mascot, cream paper, muted blue-gray and warm tan props, at most one restrained mustard/coral accent, charcoal outlines.
Materials/textures: faint paper grain and soft pigment variation; no photoreal texture.
Constraints: one clear semantic action and one primary focal point; every character and prop must serve the word meaning; simple props; no text, letters, numbers, logos, border, speech bubble, watermark.
Avoid: semantically unnecessary characters, competing focal points, crowded scenery, hard cast shadows, perfect vector geometry, anime features, realistic anatomy, excessive highlights, neon colors, glossy effects.
```

### 10.3 建議生成流程

1. 先以定錨圖 + master prompt 生成 1 張。
2. 逐項檢查：角色輪廓、臉、背棘、墨線、背景、留白、單一語意、無文字。
3. 若失敗，只做一個 targeted edit；重述「change only X; preserve everything else」。
4. 最終資產需保存進 repo，不可只留在生成工具暫存位置。
5. 記錄 prompt、日期、尺寸與 SHA-256；prototype 不自動升格為新定錨。

## 11. Figma / Design System 轉譯

### Figma component 建議

```text
IllustrationFrame / Square
├─ Background / WarmPaper
├─ SceneGroup
│  ├─ Mascot / Pose=<stand|sit|walk|celebrate>
│  ├─ SemanticObject / <scene-specific>
│  └─ GroundMarks / Density=<none|sparse>
└─ OverlayText / none by default
```

### Variables 建議

- Color collection: `Illustration`
- Variables: 使用第 5 節 token 名稱，不與現有 `--jr-*` 自動合併。
- Stroke styles: `Ink/Main`、`Ink/Detail`。
- Effect styles: 原則上 `None`；若需要，僅設一個極淡 `Ambient/Soft`。
- Grid: 1:1 frame；以 8% canvas 作外部安全區，以 28–40% 高度保留上方安靜空間。

### 前端資產規則

- 優先輸出 1:1 PNG/WebP；保持原始 master PNG。
- 卡片呈現使用 `object-fit: cover` 時，要先確定不會裁切角色、手勢或主語意物件。
- alt text 描述「動作＋主物件」，不描述風格；例如「綠色角色在桌前寫作業」。
- 單字文字與插畫分離；資料庫只儲存語意、資產路徑與審核狀態。

## 12. 禁止項總表

- 預設無文字、字母、數字、logo、水印、對話框；`Between` 等空間詞僅可依 v0.2 規格使用少量 `1`、`2` 與空間導引線。
- 不限制必須單角色；可依語意使用 1–3 個角色，但禁止加入與單字關係無關的群眾或裝飾性角色。
- 多角色圖仍只能有一個主要焦點；配角以姿勢、比例、單一配件或受控輔色區分，不另開新的視覺 grammar。
- 不把第二角色一律做成 anchor 的換色複製品；需要時使用三角龍、甲龍、鳥、小型動物或必要人物角色，但每個都有明確語意功能。
- 無寫實人體、動畫大眼、過度擬人手指、服裝細節堆疊。
- 無 neon、彩虹主色、純白背景、厚重黑色陰影或 glossy 3D。
- 無完整繁忙背景、照片合成、深景深、鏡頭光暈。
- 無完美幾何向量感，也不要故意製造髒污或過重紙紋。
- 無與語意無關的裝飾物；留白是系統的一部分，不是待填空區。
- prototype 不得自行覆寫定錨圖或角色 canonical anatomy。

## 13. 三張情境 prototype

所有成品為 1254 × 1254 px PNG，以 built-in ImageGen 產生，定錨圖作 character/style reference。

### P01 — Study at Desk / 桌前學習

- File: `assets/visual-prototypes/v0.1/01-study-at-desk.png`
- Semantic target: study、read、write、homework、learn
- Scene: 角色坐在小木桌前，以鉛筆操作攤開的圖畫書；桌燈與兩張小卡作支援物件。
- Mood: calm curiosity / 專注而輕鬆。
- SHA-256: `9e40543ef35f8614fbf52cd762c563333441218794546f0595ad73d17197e633`

```text
Create the same green mascot studying attentively at a tiny warm wooden desk, seated on a simple stool, looking down at one open picture book while holding a yellow pencil. Add only a small stack of two flashcards and a low desk lamp. Keep exactly one mascot, the canonical bean-shaped body and rounded back plates, a warm off-white paper background, one ground line, generous negative space, thick wobbly charcoal outlines, restrained cream / dusty blue-gray / warm wood / mustard colors, subtle pigment variation, no text or watermark.
```

### P02 — Waiting for Bus / 等公車

- File: `assets/visual-prototypes/v0.1/02-waiting-for-bus.png`
- Semantic target: bus、wait、go to school、travel、arrive
- Scene: 角色背著小型 mustard 背包，在圓形無字站牌旁揮手；右側一台 dusty blue-gray 公車靠近。
- Mood: safe anticipation / 安全、期待、準備出發。
- SHA-256: `f0cfb36b427f7c5113b6cf94b0c755aaad704c52b766e63004e10d56af820ad5`

```text
Create the same green mascot waiting cheerfully at a simple roadside bus stop, wearing one small muted-mustard backpack, while a compact dusty blue-gray bus approaches from the right. Use a plain circular bus-stop marker with no writing and only sparse grass marks. Keep exactly one mascot, a small wave, canonical three rounded back plates with at least two readable around natural backpack occlusion, a warm off-white paper background, generous upper negative space, thick wobbly charcoal outlines, no city clutter, no text, logos, numbers, or watermark.
```

### P03 — Correct Answer Celebration / 答對慶祝

- File: `assets/visual-prototypes/v0.1/03-correct-answer-celebration.png`
- Semantic target: correct、success、great job、complete、reward
- Scene: 角色雙手舉起，一顆 muted mustard 星星位於手勢上方；腳邊三張空白卡片，搭配少量 coral／blue-gray 動作短線。
- Mood: proud encouragement / 有成就感但不喧鬧。
- SHA-256: `c6fa596860c4f4c5256f3764e2dd59f3f2d4ed27515a548b13a8b3ad99997b11`

```text
Create the same green mascot celebrating a correct answer with both short rounded arms raised. Place one large muted-mustard star above one hand, three blank flashcards near its feet, and only a few restrained coral and dusty blue-gray confetti marks. Keep exactly one mascot, a minimal joyful expression, canonical rounded back plates, a warm off-white paper background, one ground line, ample negative space, thick wobbly charcoal outlines, no visible symbols on the cards, no text, logos, numbers, or watermark.
```

## 14. Prototype QA

| Check | P01 | P02 | P03 |
|---|---|---|---|
| 同一角色基本輪廓 | Pass | Pass | Pass |
| 綠色主體＋近黑墨線 | Pass | Pass | Pass |
| 單一語意清楚 | Pass | Pass | Pass |
| 暖白背景與上方留白 | Pass | Pass | Pass |
| 無文字／logo／水印 | Pass | Pass | Pass |
| 道具數量受控 | Pass | Pass | Pass |
| 160 px 縮圖可辨識 | Pass | Pass | Pass |
| 背棘 canonical anatomy | 3 片可見 | 背包遮擋，2 片清楚可見 | 手勢／輪廓遮擋，2 片清楚可見 |

P02 與 P03 的 underlying character spec 仍為三片背棘，但現成 prototype 只有兩片清楚可數。它們可作構圖與風格 prototype；若升格為 production asset，應在 Figma／繪圖階段補正第三片，或重新生成到三片皆可辨識。這不改變定錨圖的 canonical 規則。

### 2026-09-20｜Each other mutual-pointing QA

`each-other-pointing-v2.png` 的互相指語意通過；角色一致性暫停。主要偏差是綠色 anchor 變得更高、更長頸，手臂過長且尖，出現腳趾線／腮紅與較重的水彩紋理。`each-other-pointing-v3.png` 已依本節 3.4 重新生成，通過目前的靜態 character lock 與 160 px 檢查，但仍須完成 blind learner review 才能升格。

## 15. Production 驗收清單

- [ ] 使用指定定錨圖作 reference，而不是只使用文字風格描述。
- [ ] 一張圖只有一個主要語意與主要焦點；角色數量依語意使用 1–3 個，`Family` 可因群體詞擴展至 4–5 個。
- [ ] `Parents` 讀為兩位大人＋一位孩子；`Family` 讀為更廣的家庭群體。
- [ ] `Between` 的 clean／instructional 版本已比較，標示沒有造成序列誤解。
- [ ] `Each Other` 是雙向互動，不是單向送信或單向贈與。
- [ ] 角色是同一 bean-shaped 綠色角色，五官零件未增加。
- [ ] 背棘 canonical 數量為三；若被遮擋，至少兩片可辨識。
- [ ] 主輪廓厚、圓、略不規則；沒有完美向量或極細描邊。
- [ ] 背景暖白且保留足夠上方留白。
- [ ] 主色不超過約 5–6 種，accent 不超過 1 個主色系。
- [ ] 光線柔和，沒有硬投影、glossy 或 cinematic 效果。
- [ ] 無文字、字母、數字、logo、對話框與水印。
- [ ] 160 px 縮圖仍能辨識動作與主物件。
- [ ] Prompt、輸出尺寸、路徑、SHA-256 與審核狀態已記錄。
- [ ] 新成品未自動取代定錨圖；升格需明確設計決策。

### 15.1 Arrow semantic split

- **Position-directional overlay**：短、圓角、單一關係箭頭／括號，只表示 `behind`、`in front of`、`inside` 或 `near` 的靜態存在性；不得加入速度線或連續箭頭。
- **Movement-directional overlay**：未來另建一套 token 與元件，可使用較長箭身、重複箭頭、拖影或速度標記，表示角色／物件正在往某方向移動；不可直接重用位置箭頭。

### 15.2 `Right` 的目前語意

`Right` 目前採用「右轉／turn right」的方向語意，不是 `correct`，也不再把靜態右側位置當成主要候選。使用低干擾的藍灰交通號誌與一個清楚向右彎的黃色／白色箭頭；角色可站在號誌旁並略朝右，但不加入文字、車流或複雜道路。號誌內的彎箭頭是語意物件，不是 app overlay；不得把它與未來的移動性箭頭元件混用。原 `right-v1.png` 靜態位置候選保留為歷史資料，現行候選為 `right-v2-turn.png`。
