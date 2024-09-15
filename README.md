# unity-build-tool
build tooling for Unity game projects

## to use

## to build executable

Install Python 3 if you don't have it (this was built with Python 3.12.6)

Using Powershell, run the following from the root of this project:
```
pip install -r requirements.txt
python -m PyInstaller --onefile main.py 
```

If you have trouble running PyInstaller, see (this troubleshooting guide)[https://pyinstaller.org/en/stable/installation.html#pyinstaller-not-in-path]

## relevant links and sources

https://www.phillipsj.net/posts/executing-powershell-from-python/

https://pyinstaller.org/en/stable/