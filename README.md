# 裴秀珉老婆機器人陪你寫程式

[![Python](https://img.shields.io/badge/Python-3-3776AB)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Bot-5865F2)](https://discord.com/)

## 專案描述

Discord 機器人（測試中），需將機器人邀請至伺服器。

在 Discord 頻道輸入 `>help` 即可了解指令。

## 目標功能

- 連結 YouTube 最新影片即時通知
- 串接 OpenAI 的 API 並進行對話
- 24 小時常駐
- 播放音樂

## 技術資訊

| 項目 | 說明 |
|------|------|
| **語言** | Python |
| **平台** | Discord Bot API |

## 專案結構

```
sumin_bot/
├── bot.py          # 機器人主程式
├── cmds/           # 指令模組
│   ├── event.py    # 事件處理
│   ├── main.py     # 主要指令
│   ├── react.py    # 反應指令
│   └── task.py     # 排程任務
├── core/
│   └── classes.py  # 核心類別
├── pic/            # 圖片素材
│   ├── sumin1.jpg
│   ├── sumin2.jpg
│   └── sumin3.jpg
└── README.md
```

## 執行方式

```bash
python bot.py
```

## 教學材料

- [Proladon](https://www.youtube.com/@Proladon)
- [OpenAI](https://chatgpt.com/)
