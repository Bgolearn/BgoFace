<h1 align="center">BgoFace</h1>

<p align="center">
  Eine benutzerfreundliche Active-Learning-Plattform auf Basis von Bgolearn für autonome Experimente und beschleunigte Materialoptimierung.
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

**BgoFace** ist eine benutzerfreundliche grafische Oberfläche für das [Bgolearn](https://github.com/Bin-Cao/Bgolearn)-Framework. Die Entwicklung wird vom Team um [Cao Bin](https://www.caobin.asia/) geleitet. BgoFace vereinfacht **Bayesian global optimization (BGO)**-Workflows und unterstützt damit eine schnellere Materialentdeckung.

Mit intuitiven Bedienelementen, Unterstützung experimenteller Randbedingungen und direktem Zugang zu Active-Learning-Algorithmen ermöglicht BgoFace effiziente Materialsuche ohne tiefgehende Machine-Learning-Vorkenntnisse.

Besonderer Dank gilt **Tianliang Li**, **Siyuan Liu** sowie der Betreuung durch **Prof. Tong-Yi Zhang** und **Prof. Lingyan Feng**.

---

## Ressourcen

| Ressource | Beschreibung | Link |
| --- | --- | --- |
| **Bgolearn** | Kernframework für Bayessche Optimierung | [github.com/Bin-Cao/Bgolearn](https://github.com/Bin-Cao/Bgolearn) |
| **MultiBgolearn** | Multi-Objective-Modul für Bgolearn | [github.com/Bin-Cao/MultiBgolearn](https://github.com/Bin-Cao/MultiBgolearn) |
| **BgoFace** | Offizielle Bgolearn-GUI | [github.com/Bgolearn/BgoFace](https://github.com/Bgolearn/BgoFace) |
| **CodeDemo** | Beispielcode und Datensätze | [github.com/Bgolearn/CodeDemo](https://github.com/Bgolearn/CodeDemo) |

---

## Materialien mit BgoFace entwerfen

BgoFace unterstützt das Entwerfen, Visualisieren und Analysieren von Materialsystemen über eine intuitive grafische Oberfläche.

<img src="https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34" width="60%"/>

---

### Code-Tutorial

Der schnelle Einstieg erfolgt über das Schritt-für-Schritt-Video:
[BiliBili: Intro to BgoFace](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## Anwendung herunterladen Windows

Die aktuelle vorgefertigte Version von **BgoFace for Windows** kann direkt über die [Releases-Seite](https://github.com/Bgolearn/BgoFace/releases) heruntergeladen werden.

### Schritte

1. Öffnen Sie die [Releases Section](https://github.com/Bgolearn/BgoFace/releases).
2. Laden Sie die `.exe`-Datei der neuesten Version herunter.
3. Fuhren Sie die Datei direkt aus, eine Installation ist nicht erforderlich.

---

## Architektur von BgoFace

Das folgende Diagramm zeigt, wie die Komponenten von BgoFace vom Benutzereingang bis zur Backend-Berechnung zusammenwirken.

<img src="https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3" width="60%"/>

---

## Anleitung zur UI-Paketierung

So erstellen Sie selbst eine eigenständige Desktop-Version von BgoFace:

1. **Erforderliche Pakete installieren**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **Ausführbare Datei mit PyInstaller bauen**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`: Bundelt alles in eine Datei
   * `-w`: Unterdrückt das Konsolenfenster
   * `--add-data`: Bindet zusätzliche Assets wie Bilder ein

---

## Danksagung und Zitation

Wenn Sie Code oder Daten aus diesem Repository verwenden, zitieren Sie bitte die zugehörigen wissenschaftlichen Arbeiten.

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

## Lizenz und Nutzung

© 2024 Bgolearn Development Team. All rights reserved.

Diese Software ist ausschließlich für **akademische Zwecke und Forschung** bestimmt.
**Kommerzielle Nutzung ist streng untersagt**.
