# CONTRIBUTING.md — 组员协作须知

> 详细规范在 **AGENTS.md**（人和 AI 代理通用的最高规范），先读它。本文件只是人类组员的速查版。

## 快速上手

```bash
git clone git@github.com:STU-MS/TopoSort.git
# 环境要求：Python 3.10+，依赖清单见 app/requirements.txt（搭骨架时生成）
```

## 每天开工前

1. `git pull` 最新 master
2. 有新决策？看 `evidence/decisions/` 和 GitHub Issues（标签 `discussion`）

## 留档四习惯（详见 AGENTS.md 第二节）

| 场景 | 动作 |
|---|---|
| 做了一个技术/产品决定 | 开 issue → 定稿后写 `evidence/decisions/YYYY-MM-DD-主题.md` |
| 完成一个可见功能 | 截图存 `evidence/screenshots/功能名-YYYYMMDD-N.png` |
| 跑了一次性能测试 | `evidence/benchmarks.csv` 追加一行 |
| 写了边界/异常测试输入 | 存 `evidence/test-data/编号-描述.in/.expected` |

## 红线

- **算法自己写**（Kahn / 全序枚举 / 环检测），不许用 networkx 的现成排序
- 技术栈已定（Issue #1）：Python + PySide6 + PyInstaller，不许私自换
- `docs/` 是老师文件，只读
- 提交信息：`类型: 摘要`（feat/fix/docs/test/refactor/evidence）

## 会议记录

每周至少一篇：复制最近一篇的格式，写完放 `minutes/YYYY-MM-DD-主题.md`，群里同步链接。
