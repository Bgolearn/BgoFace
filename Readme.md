## BgoFace: The User Interface of the [Bgolearn](https://github.com/Bin-Cao/Bgolearn) Platform

![plot](https://github.com/Bin-Cao/Bgolearn/assets/86995074/d4e43900-eadb-4ddf-af46-0208314de41a)

### Dependent Packages
- **scikit-learn (sklearn)**: A machine learning library for Python.
- **Bgolearn**: A Bayesian global optimization package for Material Design.

### UI Encapsulation
To encapsulate the user interface and create a standalone application, follow these steps:

1. **Install necessary packages:**
   ```bash
   pip install pyqt5 pyinstaller
   ```

2. **Package the application using PyInstaller:**
   ```bash
   pyinstaller --onefile --windowed main.py
   ```
   This command creates a single executable file from `main.py` without opening a console window.

   
### Acknowledgement:
If you utilize the data/code from this repo, please reference our paper.

---

### License and Usage
© 2024 Bgolearn Development Team. All rights reserved.

This software is provided for academic and research purposes only. Commercial use is strictly prohibited. Any violation of these terms will be subject to appropriate actions.
