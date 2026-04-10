## Project Description
这是一个使用 Click 生成的简单 CLI 工具，用于打招呼。

## build package
```bash
uv build
```

## upload package
```bash
uv publish --publish-url https://test.pypi.org/legacy/
```

## Installation
```bash
pip install --index-url https://test.pypi.org/simple/ \
            --extra-index-url https://pypi.org/simple/ \
            andysimple
```
## Usage
```bash
simple --name <name> --repeat <repeat>
```



## Example
```bash
simple --name Alice --repeat 3
```
Output:
```
Hello, Alice!
Hello, Alice!
Hello, Alice!
Goodbye from simple!
```
