<h1 align="center">BgoFace</h1>

<p align="center">
  자율 실험과 재료 최적화 가속을 위한 Bgolearn 기반 사용자 친화형 능동학습 플랫폼입니다.
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

**BgoFace** 는 [Bgolearn](https://github.com/Bin-Cao/Bgolearn) 프레임워크를 위한 사용자 친화형 GUI입니다. [Cao Bin](https://www.caobin.asia/) 팀이 주도하여 개발했으며, 재료 발견을 가속하기 위해 **Bayesian global optimization (BGO)** 워크플로를 단순화합니다.

직관적인 조작, 실험 제약 조건 지원, 능동학습 알고리즘 접근 기능을 통해 사용자는 깊은 머신러닝 전문 지식 없이도 효율적인 재료 탐색을 수행할 수 있습니다.

**Tianliang Li**, **Siyuan Liu**, 그리고 **Tong-Yi Zhang 교수**와 **Lingyan Feng 교수**의 지도에 감사드립니다.

---

## 리소스 경로

| 리소스 | 설명 | 링크 |
| --- | --- | --- |
| **Bgolearn** | 베이지안 최적화 핵심 프레임워크 | [github.com/Bin-Cao/Bgolearn](https://github.com/Bin-Cao/Bgolearn) |
| **MultiBgolearn** | Bgolearn 다목적 모듈 | [github.com/Bin-Cao/MultiBgolearn](https://github.com/Bin-Cao/MultiBgolearn) |
| **BgoFace** | Bgolearn 공식 GUI | [github.com/Bgolearn/BgoFace](https://github.com/Bgolearn/BgoFace) |
| **CodeDemo** | 예제 코드와 데이터 | [github.com/Bgolearn/CodeDemo](https://github.com/Bgolearn/CodeDemo) |

---

## BgoFace로 재료 설계

BgoFace는 직관적인 그래픽 인터페이스를 통해 재료 시스템의 설계, 시각화, 분석을 지원합니다.

<img src="https://github.com/user-attachments/assets/30870d63-9f60-4837-897d-8453d48e5b34" width="60%"/>

---

### 코드 튜토리얼

단계별 영상 튜토리얼로 빠르게 시작할 수 있습니다:
[BiliBili: Intro to BgoFace](https://www.bilibili.com/video/BV1LTtLeaEZp/?spm_id_from=333.337.search-card.all.click)

---

## 애플리케이션 다운로드 Windows

**BgoFace for Windows** 최신 사전 빌드 버전은 [Releases 페이지](https://github.com/Bgolearn/BgoFace/releases)에서 직접 다운로드할 수 있습니다.

### 단계

1. [Releases Section](https://github.com/Bgolearn/BgoFace/releases)으로 이동합니다.
2. 최신 릴리스의 `.exe` 파일을 다운로드합니다.
3. 설치 없이 바로 실행합니다.

---

## BgoFace 아키텍처

다음 그림은 사용자 입력부터 백엔드 계산까지 BgoFace 구성 요소의 상호 작용을 보여줍니다.

<img src="https://github.com/user-attachments/assets/17d5b63a-6f10-4783-b95e-d645c39709f3" width="60%"/>

---

## UI 패키징 가이드

BgoFace 독립 실행형 데스크톱 버전을 직접 만들려면:

1. **필수 패키지 설치**

   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **PyInstaller로 실행 파일 빌드**

   ```bash
   pyinstaller -F -w --add-data "Images;Images" main.py
   ```

   * `-F`: 단일 파일로 번들링
   * `-w`: 콘솔 창 숨김
   * `--add-data`: 이미지 등 추가 자산 포함

---

## 감사 및 인용

이 저장소의 코드 또는 데이터를 사용하는 경우 관련 연구 논문을 인용해 주십시오.

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

## 라이선스 및 사용

© 2024 Bgolearn Development Team. All rights reserved.

이 소프트웨어는 **학술 및 연구 목적** 으로만 사용할 수 있습니다.
**상업적 사용은 엄격히 금지** 됩니다.
