# Swag Labs电商网站测试计划

## 1. 项目背景
测试对象：https://www.saucedemo.com/（开源电商演示网站）

## 2. 测试范围
- 登录模块
- 商品浏览 & 排序
- 购物车
- 结账流程
- 登出与异常处理
- 性能测试
- 兼容性测试
- 安全测试
- 6个预设账号（standard_user、locked_out_user、performance_glitch_user、problem_user、error_user、visual_user）

## 3. 测试类型
- 手动功能测试
- Chrome DevTools性能分析
- UI自动化测试（Playwright + POM）

## 4. 测试环境
- 系统：Windows
- 浏览器：Chrome（无痕模式）
- 工具：PyCharm + Playwright + Pytest + GitHub Issues + Chrome DevTools

## 5. 测试资源
独立完成

## 6. 时间计划
2026.3 - 2026.4

## 7. 通过标准
- 高优先级（P0/P1）用例100%通过
- 所有Bug已记录并模拟回归

## 8. 风险
网站第三方服务偶尔出现Console噪音（已分析忽略）