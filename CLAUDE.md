# CLAUDE.md

此文件为Claude Code (claude.ai/code)在此代码库中工作时提供指导。

## 项目概述

这是一个基于Miguel Grinberg所著《Flask Web Development》一书的Flask Web应用程序。它是一个具有用户认证、博客文章、评论和关注功能的社交博客应用。

## 代码架构

- **主应用程序**: `app/__init__.py` - 创建带有main、auth和API蓝图的Flask应用
- **配置**: `config.py` - 多种配置（开发、测试、生产、heroku、docker）
- **模型**: `app/models.py` - 用于User、Role、Post、Comment、Follow关系的SQLAlchemy模型
- **认证**: `app/auth/` - 用户注册、登录、密码重置的蓝图
- **主要视图**: `app/main/` - 博客文章、用户资料、关注功能的蓝图
- **API**: `app/api/` - 面向文章、评论、用户的RESTful API端点
- **数据库迁移**: `migrations/` - Flask-Migrate迁移脚本
- **测试**: `tests/` - 单元测试和集成测试

## 核心组件

1. **用户系统**: 基于角色权限的User、Role和Permission模型
2. **内容**: 支持Markdown的文章和评论
3. **社交功能**: 用户关注关系
4. **邮件**: 使用Flask-Mail的邮件通知
5. **API**: 带令牌认证的RESTful API

## 常用开发命令

### 运行应用程序
```bash
# 开发环境
flask run

# 生产环境（使用gunicorn）
gunicorn flasky:app
```

### 数据库操作
```bash
# 初始化/升级数据库
flask db upgrade

# 部署应用程序（运行迁移、插入角色）
flask deploy
```

### 测试
```bash
# 运行所有测试
flask test

# 运行特定测试文件
flask test tests.test_user_model

# 带覆盖率运行
flask test --coverage
```

### 数据库迁移
```bash
# 生成迁移
flask db migrate -m "迁移信息"

# 应用迁移
flask db upgrade

# 回退迁移
flask db downgrade
```

## 部署选项

1. **Heroku**: 使用带有gunicorn的Procfile
2. **Docker**: 提供了Dockerfile和docker-compose.yml
3. **传统部署**: 提供Unix配置

## 环境变量

关键环境变量：
- `FLASK_CONFIG` - 要使用的配置（development, testing, production, heroku, docker）
- `SECRET_KEY` - Flask密钥
- `DATABASE_URL` - 生产数据库URL
- `MAIL_USERNAME`/`MAIL_PASSWORD` - 邮件凭证