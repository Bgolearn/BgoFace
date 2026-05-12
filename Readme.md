

<h1 align="center">BgoFace</h1>


<p align="center">
  A user-friendly active learning platform built on Bgolearn for autonomous experimentation and accelerated materials optimization.
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

  <a href="https://github.com/Bgolearn/BgoFace/issues?q=is%3Aissue+is%3Aclosed">
    <img src="https://img.shields.io/github/issues-closed/Bgolearn/BgoFace" alt="Closed Issues">
  </a>

  <a href="https://github.com/Bgolearn/BgoFace/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Bgolearn/BgoFace" alt="License">
  </a>

  <a href="https://onlinelibrary.wiley.com/doi/10.1002/mgea.10107">
    <img src="https://img.shields.io/badge/MGE%20Advances-2025-red" alt="Paper">
  </a>
</p>



---

**BgoFace** is a user-friendly interface developed for the [Bgolearn](https://github.com/Bin-Cao/Bgolearn) framework, led by [Cao Bin](https://www.caobin.asia/) and published in *MGE Advances*. Designed to accelerate materials discovery, BgoFace simplifies **Bayesian global optimization (BGO)** workflows by bridging the gap between experimental and computational domains.

With intuitive controls, integrated support for experimental constraints, and seamless access to active learning algorithms, BgoFace empowers users to conduct efficient materials exploration—without requiring deep expertise in machine learning.

Special thanks to **Mr. Tianliang Li**, **Mr. Siyuan Liu**, and to the guidance of **Prof. Tong-Yi Zhang** and **Prof. Lingyan Feng**.

---



## Design Materials Using BgoFace

BgoFace allows users to design, visualize, and analyze material systems via an intuitive graphical interface.

<img src="https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34" 
     width="60%"/>

---

### Code Tutorial

Get started quickly by watching our step-by-step video tutorial:
[BiliBili: Intro to BgoFace](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## Download the Application (Windows)

You can directly download the latest pre-built version of **BgoFace for Windows** from our [Releases Page](https://github.com/Bgolearn/BgoFace/releases).

### Steps:

1. Navigate to the [Releases Section](https://github.com/Bgolearn/BgoFace/releases).
2. Download the `.exe` file from the **latest release**.
3. Run the file — no installation is required!

---

## Architecture of BgoFace

This diagram outlines how the components of BgoFace interact, from user input to backend computation:


<img src="https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3" 
     width="60%"/>
     
---

## UI Encapsulation Guide

To create a standalone desktop version of BgoFace yourself:

1. **Install Required Packages**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **Build Executable with PyInstaller**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`: Bundle into one file
   * `-w`: Suppress console window
   * `--add-data`: Include additional assets like images

---

## Acknowledgement

If you use the code or data from this repository, please cite our related research publication.

---

## License & Usage

© 2024 Bgolearn Development Team. All rights reserved.

This software is for **academic and research use only**.
**Commercial use is strictly prohibited** and subject to enforcement.
