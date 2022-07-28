from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库连接配置
# 'mysql+pymysql://用户名:密码@服务器地址:端口/数据库名?charset=utf8mb4'
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:root@fwm@localhost:3306/fastapi?charset=utf8mb4'

# 创建引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 创建数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 声明基类
Base = declarative_base()
