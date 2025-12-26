# Flasky - Modern Flask 3.x Boilerplate

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Bootstrap 5](https://img.shields.io/badge/Bootstrap-5-purple.svg)](https://getbootstrap.com/)

> 基于 Miguel Grinberg 经典 Flasky 项目重构的现代 Flask 3.x 应用模板。

## 🚀 项目简介

这是一个基于 Flask 3.x 完全重构的社交博客应用。相比原版，本项目去除了过时的依赖（如 Flask-Bootstrap/Flask-Script），采用了现代的 Flask 生态最佳实践。

**核心更新：**
*   **Flask 3.x**: 适配最新 Flask 生态。
*   **Bootstrap 5**: 从 Bootstrap 3 迁移到 Bootstrap 5 (使用 `bootstrap-flask`)，界面更现代。
*   **Minimal Setup**: 简化 `flasky.py` 入口，拥抱原生 `flask` CLI。
*   **Docker Optimized**: 使用 Python 3.12-slim 的多阶段或精简构建。
*   **Modern Coding**: 根据 2025 年标准更新了代码风格，移除 `itsdangerous` 过期用法，修复 `bleach` 等已弃用库的问题。

## ✨ 功能特性

- 🔐 **用户认证** - 安全的注册、登录与令牌管理 (Flask-Login)
- 📝 **博客系统** - Markdown 文章发布，支持 HTML 净化 (Bleach)
- 💬 **互动评论** - 文章评论与管理
- 👥 **关注系统** - 社交关注与动态流
- 🛡️ **权限管理** - 基于角色的访问控制 (RBAC)
- 🐳 **Docker 支持** - 开箱即用的容器化部署配置

## 🛠️ 技术栈

- **Core**: Flask 3.x, Werkzeug 3.x
- **Database**: SQLAlchemy 2.x (via Flask-SQLAlchemy 3.x), Alembic
- **Frontend**: Bootstrap 5, Jinja2
- **Utilities**: Click, Python-Dotenv

## 🚀 快速开始

### 1. 环境准备

推荐使用 Python 3.12+。

```bash
git clone https://github.com/your/flasky.git
cd flasky
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 配置与初始化

创建 `.env` 文件（可选，Flask 会自动加载）：

```bash
flask deploy
```
> `flask deploy` 会自动执行数据库迁移、创建角色等初始化操作。

### 3. 运行应用

```bash
flask run
```
访问 http://localhost:5000

## 🐳 Docker 部署

```bash
docker build -t flasky:latest .
docker run -p 5000:5000 flasky:latest
```

## 🔧 开发指南

### 数据库迁移

使用 Flask-Migrate (Alembic) 管理数据库变更：

```bash
flask db migrate -m "migration message"
flask db upgrade
```

### 测试

运行单元测试：
```bash
flask test
```

## 📄 许可证

MIT License
