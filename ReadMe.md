# Getting Started with Python

Welcome! Before you start writing Python, you’ll need Python itself and a place to write your code. This guide will help you get both set up.

## Install Python

### Windows

1. Head to [python.org/downloads](https://www.python.org/downloads/) and download Python for Windows.
2. Open the installer. Before you continue, check **Add python.exe to PATH** at the bottom of the first screen, then select **Install Now**.
3. When the installation finishes, open PowerShell or Command Prompt and make sure Python is ready:

	```powershell
	py --version
	```

### macOS

1. Visit [python.org/downloads](https://www.python.org/downloads/) and download the macOS installer.
2. Open the downloaded file and follow the steps on screen.
3. When it’s done, open Terminal and check that Python installed correctly:

	```bash
	python3 --version
	```

The command you’ll use depends on your computer: `py` on Windows, or `python3` on macOS.

## Install VS Code

1. Download [Visual Studio Code](https://code.visualstudio.com/) and follow the installer steps for your computer.
2. Open VS Code, then choose **File > Open Folder** to open the folder where you’d like to keep your Python practice files.

## Add the Python extensions

Extensions add Python support to VS Code. Open **Extensions** from the sidebar (or press `Ctrl+Shift+X` on Windows / `Cmd+Shift+X` on macOS), then search for:

- **Python** by Microsoft, so you can run and debug your Python files.
- **Pylance** by Microsoft, for helpful autocomplete and code checking. It may already be installed along with the Python extension.

The first time you open a `.py` file, VS Code may ask which Python interpreter to use. Choose the Python version you just installed.

## Run your first program

Let’s make sure everything works. Create a file called `hello.py` and type in:

```python
print("Hello, world!")
```

In VS Code, open **Terminal > New Terminal** and run this on Windows:

```powershell
py hello.py
```

On macOS, run:

```bash
python3 hello.py
```
