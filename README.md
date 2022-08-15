# README

## Setup config.ini

Add config.ini file in project folder containing:

```
[vars]
bearer_token: YOUR_VALUE
api_application: YOUR_VALUE
api_company: YOUR_VALUE
template: YOUR_VALUE
```

## Create Virtual env

```
python3 -m venv .venv
```

## Windows venv activation

In cmd.exe

```
venv\Scripts\activate.bat
```

In PowerShell

```
venv\Scripts\Activate.ps1
```

## Linux and MacOS venv activation

```
$ source myvenv/bin/activate
```

## Install dependences

```
pip install -r requirements.txt
```

## Run program

```
python main.py
```
