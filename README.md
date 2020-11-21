# Pytest Tutorial

# Installation

There are three methods to get this repo up and running, 

## Local

```
conda create -n pytest python=3.7
conda activate typedpy
pip install -r requirements.txt requirements-test.txt
```

and run `python -m pytest test` 

## Docker (Mac/linux)

If you do not have make installed:

* Mac
  * `brew install make`
* Linux
  * `apt-get install build-essential`

and run `make dockerbash` to access the bash, and `make localrun` 

## vscode - Remote development

Download [vscode](https://code.visualstudio.com/) and install the recommended installations. 

Open settings and choose `Open folder in Container` 

If you are coming back / made changes, select `Rebuild and Reopen in Container` 

similarity, `make localrun` in the terminal within vscode.

----

