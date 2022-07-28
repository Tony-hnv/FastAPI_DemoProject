## 代码环境及软件
> MacOS 10.14.6

> Python 3.10

> MySQL 8.0.18

> PyCharm 2022.1.4


## 安装依赖
```shell
pip install pymysql
```
```shell
pip install fastapi
```
```shell
pip install uvicorn
```
```shell
pip install sqlalchemy
```

## 运行
### 1. 在sql_app同级目录下，使用以下命令：
```shell
uvicorn sql_app,main:app  --reload
```
### 2. 在浏览器地址栏中输入：
1. API接口地址：
```shell
127.0.0.1:8000
``` 
2. 交互式API文档地址：
```shell
127.0.0.1:8000/docs  
```
3. 备用API文档地址：
```shell
127.0.0.1:8000/redoc 
```

# Notice： 建议使用虚拟开发环境
## 1. 推荐使用virtualenv
```shell
pip install virtualenv  // 安装virtualenv
```
```shell
virtualenv --version // 检测是否安装成功
```

```shell
virtualenv 文件名  // 在该文件名目录下生成一个python环境
```
## 2. 然后在'虚拟环境'目录下进行安装依赖和运行