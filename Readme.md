
## BgoFace: A User Interface for the [Bgolearn](http://bgolearn.caobin.asia/) Platform

🔗 [Visit Bgolearn Homepage](http://bgolearn.caobin.asia/)

---

## 🌟 Design Materials Using BgoFace

![Design Interface](https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34)

---

### 🎥 Code Tutorial

Watch a hands-on tutorial on BiliBili:
[BiliBili Video](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## 🧠 Architecture of BgoFace

![Architecture Diagram](https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3)

---

## 🖥️ UI Encapsulation Guide

To package the BgoFace interface into a standalone desktop application:

1. **Install Required Packages**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **Build Executable with PyInstaller**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`: Bundle into one file
   * `-w`: No console window
   * `--add-data`: Include image assets
     This command will generate a standalone `.exe` for `main.py`.

---

## 📄 Acknowledgement

If you use the code or data from this repository, please cite our related paper.

---

## 📜 License & Usage

© 2024 Bgolearn Development Team. All rights reserved.

This software is intended for **academic and research purposes only**.
**Commercial use is strictly prohibited.** Unauthorized use will result in legal action.

![License Notice](https://github.com/user-attachments/assets/245278dd-522b-41aa-a330-212c3a615564)

