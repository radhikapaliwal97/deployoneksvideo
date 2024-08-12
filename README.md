# ITV Content Technology Python Coding Exercise

Please read the [exercise instructions](instructions.md).

## Setup environment

```bash
python -m venv .venv
```

### Activate venv

#### mac os / linux

```bash
source .venv/bin/activate
```

#### windows

cmd
```cmd
.\.venv\Scripts\activate.bat
```

powershell
```powershell
.\.venv\Scripts\activate.ps1
```

## Install requirements

```bash
pip install -r tests/test_requirements.txt
```

## Install ffmpeg

[Binary downloads](https://www.ffmpeg.org/download.html)

[Example installation tutorial](https://www.hostinger.co.uk/tutorials/how-to-install-ffmpeg)

### Mac OS

```bash
brew install ffmpeg
```

### Windows

```powershell
choco install ffmpeg
```

### Linux

#### Fedora
```bash
sudo dnf install -y ffmpeg
```

#### Debian / Ubuntu
```bash
sudo apt install ffmpeg
```

#### Arch / Manjaro
```bash
sudo pacman -S ffmpeg
```

## Install test requirements

```bash
pip install -r tests/test_requirements.txt
```


## Linting

Please install pre-commit to enable Black to auto format your code before you commit your work.

```bash
pip install black
pip install pre-commit
pre-commit install
```

## Running the code

Execute the main module from the root of the project

```bash
python -m main {asset_id} {timestamp}
```

example:
```bash
python -m main valid "00:00:5"
```

Execute the tests from the root of the project

```bash
pytest
```

## Assumptions

 - 

## Design decisions

 -