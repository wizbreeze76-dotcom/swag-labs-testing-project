# Swag Labs电商网站测试总结报告

## 测试概况
- 测试用例总数：**33个**（UI手动测试）
- 执行结果：**31 Pass，2 Fail**
- 接口测试：**6个**（5个单接口 + 1个场景用例），全部通过
- 发现真实Bug：**2个**（均已通过GitHub Issues管理）
- 特殊账号覆盖：全部6个预设账号
- 性能测试亮点：使用Chrome DevTools Performance面板完成对比测试

## 关键亮点
- 完整覆盖登录、商品浏览、购物车、结账、性能、兼容性、安全、全流程场景法
- 使用Playwright + POM实现核心UI自动化测试
- 使用Apifox对JSONPlaceholder进行接口测试（GET/POST/PUT/DELETE + 场景串联）
- 针对seeded defect账号设计负向测试用例并全部Pass

## Bug列表
- Bug-01 (#1)：TC-18 Continue Shopping 后商品排序状态丢失
- Bug-02 (#2)：TC-24 结账邮编字段对特殊字符缺少输入校验

## 测试报告附件
- UI测试用例执行表：`test-cases/test-cases.xlsx`
- UI自动化HTML报告：`reports/report.html`
- 接口测试完整报告：`reports/apifox-reports.html`
- 接口测试集合：`api-tests/jsonplaceholder-api-collection.json`

## 改进建议
- 可增加Locust性能压测脚本
- 可扩展移动端自动化测试

完成日期：2026年3月