# TopoSort — 拓扑排序应用软件

> CST4823A 高级算法原理实践 · 小组课程项目

输入 `<a,b>` 先修关系 → 有向图分层渲染 → **动画演示排序全过程**（候选队列、节点逐个消耗、分叉点多路并推）→ 输出尽可能多的拓扑序列，含环检测。

## 新成员 / AI 代理请先读这两份

1. **[AGENTS.md](AGENTS.md)** — 项目最高规范（仓库结构、留档规则、开发红线）
2. **[CONTRIBUTING.md](CONTRIBUTING.md)** — 协作速查

## 技术栈

| 项 | 选择 | 备注 |
|---|---|---|
| 语言 | Python 3.11+ | |
| GUI | PySide6（QGraphicsView） | 动画完全可控 |
| 打包 | PyInstaller | 单文件，双击即跑 |
| **工程管理** | **uv（唯一标准）** | 依赖、虚拟环境、运行、测试全走 uv |
| 测试 | pytest | 用例数据在 `evidence/test-data/` |

决策记录：`evidence/decisions/` · [Issue #1](https://github.com/STU-MS/TopoSort/issues/1)

## 快速开始（uv，唯一姿势）

```bash
# 0. 装 uv（仅需一次）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 1. 克隆 + 创建虚拟环境 + 安装依赖（uv.lock 锁定版本，所见即所得）
git clone git@github.com:STU-MS/TopoSort.git && cd TopoSort
uv sync

# 2. 运行
uv run python app/main.py

# 3. 测试
uv run pytest

# 4. 打包单文件（产物在 dist/）
uv run pyinstaller --onefile --noconsole app/main.py
```

> ⚠️ 本项目**禁止** `pip install` 裸装依赖：加依赖 = 改 `pyproject.toml` → `uv add 包名` → 提交 `uv.lock`。

## 仓库结构

```
├── app/            # 源码（models / events / scene / ui / main）
├── deliverables/   # 最终交付文档（报告 + 6 份文档，md 撰写）
├── minutes/        # 会议记录（每周 ≥1 篇，模板见 _模板.md）
├── evidence/       # ★ 素材库：决策/截图/性能数据/测试数据（只进不改）
├── tools/          # 辅助脚本
└── docs/           # 老师下发的原始作业文件（只读）
```

## 红线（详见 AGENTS.md）

- 算法（Kahn 排序、全序枚举、环检测）**必须自研**，禁用 networkx 等现成实现
- 决策必须留档：issue → `evidence/decisions/`
- 完成可见功能立刻截图进 `evidence/screenshots/`
