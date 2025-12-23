# Flasky

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-0.12.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 基于 Miguel Grinberg 所著《Flask Web Development》一书的 Flask 社交博客应用程序

## 📖 项目简介

Flasky 是一个功能完整的社交博客应用，包含用户认证、博客文章发布、评论系统和用户关注功能。本项目是 O'Reilly 出版的《[Flask Web Development](http://www.flaskbook.com)》第二版的配套源代码。

## ✨ 功能特性

- 🔐 **用户认证系统** - 注册、登录、密码重置、邮箱验证
- 📝 **博客文章** - 支持 Markdown 格式的文章发布与编辑
- 💬 **评论系统** - 文章评论功能，支持管理审核
- 👥 **社交功能** - 用户关注/取消关注、动态时间线
- 🔑 **角色权限** - 基于角色的权限管理系统
- 📮 **邮件通知** - 使用 Flask-Mail 发送邮件通知
- 🌐 **RESTful API** - 带令牌认证的完整 API 接口

## 🏗️ 项目结构

```
flasky/
├── app/                    # 应用程序主目录
│   ├── api/               # RESTful API 蓝图
│   ├── auth/              # 用户认证蓝图
│   ├── main/              # 主要视图蓝图
│   ├── templates/         # Jinja2 模板
│   ├── static/            # 静态资源
│   ├── models.py          # 数据库模型
│   └── email.py           # 邮件功能
├── migrations/            # 数据库迁移脚本
├── tests/                 # 测试文件
├── requirements/          # 依赖包配置
├── config.py              # 应用配置
├── flasky.py              # 应用入口
├── Dockerfile             # Docker 配置
└── docker-compose.yml     # Docker Compose 配置
```

## 🚀 快速开始

### 环境要求

- Python 3.9+
- pip

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/miguelgrinberg/flasky.git
cd flasky
```

2. **创建虚拟环境**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows
```

3. **安装依赖**

```bash
pip install -r requirements/dev.txt
```

4. **配置环境变量**

```bash
export FLASK_APP=flasky.py
export FLASK_CONFIG=development
```

5. **初始化数据库**

```bash
flask db upgrade
flask deploy
```

6. **运行应用**

```bash
flask run
```

访问 http://localhost:5000 即可查看应用。

## 🔧 常用命令

### 运行应用

```bash
# 开发环境
flask run

# 生产环境（使用 gunicorn）
gunicorn flasky:app
```

### 数据库操作

```bash
# 初始化/升级数据库
flask db upgrade

# 应用部署（运行迁移、插入角色）
flask deploy

# 生成迁移
flask db migrate -m "迁移信息"

# 回滚迁移
flask db downgrade
```

### 测试

```bash
# 运行所有测试
flask test

# 运行特定测试
flask test tests.test_user_model

# 带覆盖率测试
flask test --coverage
```

## 🐳 Docker 部署

### 使用 Docker Compose

```bash
docker-compose up -d
```

### 使用 Docker

```bash
docker build -t flasky .
docker run -p 5000:5000 flasky
```

## ☁️ Heroku 部署

项目已配置好 Heroku 部署所需文件：

- `Procfile` - Heroku 进程配置
- `requirements.txt` - 引用 Heroku 专用依赖

```bash
heroku create
git push heroku main
heroku run flask deploy
```

## ⚙️ 环境变量

| 变量名 | 描述 | 默认值 |
|--------|------|--------|
| `FLASK_CONFIG` | 配置环境 (development, testing, production, heroku, docker) | development |
| `SECRET_KEY` | Flask 密钥 | hard to guess string |
| `DATABASE_URL` | 生产环境数据库 URL | SQLite |
| `MAIL_SERVER` | 邮件服务器 | smtp.googlemail.com |
| `MAIL_PORT` | 邮件端口 | 587 |
| `MAIL_USERNAME` | 邮件用户名 | - |
| `MAIL_PASSWORD` | 邮件密码 | - |
| `FLASKY_ADMIN` | 管理员邮箱 | - |

## 📚 相关资源

- 📖 [《Flask Web Development》图书](http://www.flaskbook.com)
- 📂 [第一版源代码](https://github.com/miguelgrinberg/flasky-first-edition)
- 📘 [Flask 官方文档](https://flask.palletsprojects.com/)

## 📝 关于本书

本仓库中的提交和标签经过精心设计，与书中概念的呈现顺序相匹配。请阅读书籍前言中"如何使用示例代码"一节以获取详细说明。

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)。

Copyright © 2013 Miguel Grinberg
