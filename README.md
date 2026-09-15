# TopoSort — 拓扑排序应用软件

CST4823A 高级算法原理实践 · 小组课程项目。

输入 `<a,b>` 先修关系 → 有向图渲染 → 动画演示拓扑排序全过程（候选队列、节点消耗、分叉多路并推）→ 输出尽可能多拓扑序列 + 环检测。

## 新成员 / AI 代理请从这两份读起

1. **[AGENTS.md](AGENTS.md)** — 项目最高规范（含仓库结构、留档规则、开发红线）
2. **[CONTRIBUTING.md](CONTRIBUTING.md)** — 协作速查

## 技术栈

Python 3 + PySide6 + PyInstaller 单文件（决策记录见 `evidence/decisions/` 与 [Issue #1](https://github.com/STU-MS/TopoSort/issues/1)）。

## 快速运行（骨架搭好后更新此节）

```bash
cd app && pip install -r requirements.txt
python main.py
```
