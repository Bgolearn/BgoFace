<h1 align="center">BgoFace</h1>

<p align="center">
  自律実験と材料最適化を加速する、Bgolearn ベースの使いやすい能動学習プラットフォーム。
</p>

<p align="center">
  <a href="./Readme.md">English</a> |
  <a href="./Readme.zh-CN.md">中文</a> |
  <a href="./Readme.ja.md">日本語</a> |
  <a href="./Readme.ko.md">한국어</a> |
  <a href="./Readme.de.md">Deutsch</a>
</p>

<p align="center">
  <a href="https://github.com/Bgolearn/BgoFace/stargazers">
    <img src="https://img.shields.io/github/stars/Bgolearn/BgoFace?style=social" alt="GitHub Stars">
  </a>
  <a href="https://github.com/Bgolearn/BgoFace/network/members">
    <img src="https://img.shields.io/github/forks/Bgolearn/BgoFace?style=social" alt="GitHub Forks">
  </a>
  <a href="https://github.com/Bgolearn/BgoFace/issues">
    <img src="https://img.shields.io/github/issues/Bgolearn/BgoFace" alt="Open Issues">
  </a>
  <a href="https://github.com/Bgolearn/BgoFace/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Bgolearn/BgoFace" alt="License">
  </a>
  <a href="https://doi.org/10.1038/s41524-026-02226-3">
    <img src="https://img.shields.io/badge/npj%20Computational%20Materials-2026-red" alt="Bgolearn Paper">
  </a>
</p>

<p align="center">
  <a href="https://github.com/Bin-Cao/Bgolearn">
    <img src="https://img.shields.io/badge/Bgolearn-Core-2f80ed?logo=github" alt="Bgolearn Core">
  </a>
  <a href="https://github.com/Bin-Cao/MultiBgolearn">
    <img src="https://img.shields.io/badge/MultiBgolearn-Multi--Object-27ae60?logo=github" alt="MultiBgolearn">
  </a>
  <a href="https://github.com/Bgolearn/BgoFace">
    <img src="https://img.shields.io/badge/BgoFace-Official%20GUI-f2994a?logo=github" alt="BgoFace Official GUI">
  </a>
  <a href="https://github.com/Bgolearn/CodeDemo">
    <img src="https://img.shields.io/badge/CodeDemo-Examples%20%26%20Data-9b51e0?logo=github" alt="CodeDemo">
  </a>
</p>

---

**BgoFace** は [Bgolearn](https://github.com/Bin-Cao/Bgolearn) フレームワーク向けに開発されたユーザーフレンドリーな GUI です。[Cao Bin](https://www.caobin.asia/) チームが主導し、材料発見を加速するために **Bayesian global optimization (BGO)** ワークフローを簡素化します。

直感的な操作、実験制約への対応、能動学習アルゴリズムへのアクセスにより、機械学習の専門知識が深くなくても効率的な材料探索を行えます。

**Tianliang Li** 氏、**Siyuan Liu** 氏、ならびに **Tong-Yi Zhang 教授**、**Lingyan Feng 教授** のご指導に感謝します。

---

## リソース

| リソース | 説明 | リンク |
| --- | --- | --- |
| **Bgolearn** | ベイズ最適化のコアフレームワーク | [github.com/Bin-Cao/Bgolearn](https://github.com/Bin-Cao/Bgolearn) |
| **MultiBgolearn** | Bgolearn の多目的モジュール | [github.com/Bin-Cao/MultiBgolearn](https://github.com/Bin-Cao/MultiBgolearn) |
| **BgoFace** | Bgolearn 公式 GUI | [github.com/Bgolearn/BgoFace](https://github.com/Bgolearn/BgoFace) |
| **CodeDemo** | サンプルコードとデータ | [github.com/Bgolearn/CodeDemo](https://github.com/Bgolearn/CodeDemo) |

---

## BgoFace による材料設計

BgoFace は、直感的なグラフィカルインターフェースを通じて材料系の設計、可視化、解析を支援します。

<img src="https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34" width="60%"/>

---

### コードチュートリアル

ステップごとの動画チュートリアルはこちら：
[BiliBili: Intro to BgoFace](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## アプリケーションのダウンロード Windows

**BgoFace for Windows** のビルド済み最新版は [Releases ページ](https://github.com/Bgolearn/BgoFace/releases) から直接ダウンロードできます。

### 手順

1. [Releases Section](https://github.com/Bgolearn/BgoFace/releases) に移動します。
2. 最新リリースの `.exe` ファイルをダウンロードします。
3. インストールせずにそのまま実行できます。

---

## BgoFace のアーキテクチャ

次の図は、ユーザー入力からバックエンド計算までの BgoFace コンポーネントの関係を示します。

<img src="https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3" width="60%"/>

---

## UI パッケージングガイド

BgoFace のスタンドアロンデスクトップ版を作成する場合：

1. **必要なパッケージをインストール**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **PyInstaller で実行ファイルをビルド**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`: 単一ファイルにバンドル
   * `-w`: コンソールウィンドウを非表示
   * `--add-data`: 画像などの追加アセットを含める

---

## 謝辞と引用

このリポジトリのコードまたはデータを使用する場合は、関連研究を引用してください。

```bibtex
@article{Cao2026Bgolearn,
  author    = {Bin Cao and Jie Xiong and Jiaxuan Ma and Yuan Tian and Yirui Hu and Mengwei He and Longhan Zhang and Jiayu Wang and Jian Hui and Li Liu and Dezhen Xue and Turab Lookman and Jun Wang and Tong-Yi Zhang},
  title     = {Bgolearn: a unified Bayesian optimization framework for accelerating materials discovery},
  journal   = {npj Computational Materials},
  year      = {2026},
  volume    = {12},
  pages     = {Article xxx},
  doi       = {10.1038/s41524-026-02226-3},
  url       = {https://doi.org/10.1038/s41524-026-02226-3}
}

@article{li2025optimize,
  title     = {Optimize the quantum yield of G-quartet-based circularly polarized luminescence materials via active learning strategy-BgoFace},
  author    = {Li, Tianliang and Chen, Lifei and Cao, Bin and Liu, Siyuan and Lin, Lixing and Li, Zeyu and Chen, Yingying and Li, Zhenzhen and Zhang, Tong-yi and Feng, Lingyan},
  journal   = {Materials Genome Engineering Advances},
  volume    = {3},
  number    = {3},
  pages     = {e70031},
  year      = {2025},
  publisher = {Wiley Online Library}
}
```

---

## ライセンスと利用

© 2024 Bgolearn Development Team. All rights reserved.

本ソフトウェアは **学術・研究用途のみ** に利用できます。
**商用利用は禁止** されています。
