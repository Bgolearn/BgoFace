<h1 align="center">BgoFace</h1>

<p align="center">
  基于 Bgolearn 的友好型主动学习平台，用于自主实验与材料优化加速。
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

**BgoFace** 是为 [Bgolearn](https://github.com/Bin-Cao/Bgolearn) 框架开发的用户友好型图形界面，由 [Cao Bin](https://www.caobin.asia/) 团队主导。BgoFace 面向材料发现加速，简化 **Bayesian global optimization (BGO)** 工作流，帮助用户连接实验设计与计算分析。

BgoFace 提供直观控件、实验约束支持和主动学习算法入口，使用户无需深度机器学习背景也能开展高效材料探索。

特别感谢 **Tianliang Li**、**Siyuan Liu**，以及 **Tong-Yi Zhang 教授** 和 **Lingyan Feng 教授** 的指导。

---

## 资源路径

| 资源 | 说明 | 链接 |
| --- | --- | --- |
| **Bgolearn** | 贝叶斯优化核心框架 | [github.com/Bin-Cao/Bgolearn](https://github.com/Bin-Cao/Bgolearn) |
| **MultiBgolearn** | Bgolearn 多目标模块 | [github.com/Bin-Cao/MultiBgolearn](https://github.com/Bin-Cao/MultiBgolearn) |
| **BgoFace** | Bgolearn 官方 GUI | [github.com/Bgolearn/BgoFace](https://github.com/Bgolearn/BgoFace) |
| **CodeDemo** | 示例代码和数据 | [github.com/Bgolearn/CodeDemo](https://github.com/Bgolearn/CodeDemo) |

---

## 使用 BgoFace 设计材料

BgoFace 支持通过直观图形界面完成材料体系设计、可视化与分析。

<img src="https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34" width="60%"/>

---

### 代码教程

可通过视频教程快速上手：
[BiliBili: Intro to BgoFace](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## 下载应用程序 Windows 版

可在 [Releases 页面](https://github.com/Bgolearn/BgoFace/releases) 直接下载最新的 **BgoFace for Windows** 预构建版本。

### 步骤

1. 进入 [Releases Section](https://github.com/Bgolearn/BgoFace/releases)。
2. 下载最新版本中的 `.exe` 文件。
3. 直接运行，无需安装。

---

## BgoFace 架构

下图展示了 BgoFace 从用户输入到后端计算的组件交互关系：

<img src="https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3" width="60%"/>

---

## UI 打包指南

如需自行创建 BgoFace 独立桌面版本：

1. **安装依赖包**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **使用 PyInstaller 构建可执行文件**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`：打包为单文件
   * `-w`：隐藏控制台窗口
   * `--add-data`：包含图片等额外资源

---

## 致谢与引用

如果您使用本仓库中的代码或数据，请引用以下相关研究成果。

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

## 许可与使用

© 2024 Bgolearn Development Team. All rights reserved.

本软件仅限 **学术与科研用途**。
**严禁商业使用**，并保留追究权利。
