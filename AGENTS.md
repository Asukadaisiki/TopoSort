# AGENTS.md — 项目规范（人和 AI 代理都须遵守）

> 目标读者：本项目的人类组员**和任何 AI 编码代理**（Claude Code / Codex / Cursor / Copilot 等）。
> 本文件是本仓库的最高规范。AI 代理开始工作前必须先读完本文件。

## TOP RULE（最高规则，凌驾一切）

**决策必须留档，确保整个项目可复现。**

- 任何影响产品形态/技术选型/接口设计的决定 → 必须先开 GitHub Issue（标签 `discussion`）→ 定稿后把结论存入 `evidence/decisions/`。
- 禁止“凭记忆开发”：写代码前先查 `evidence/decisions/`，有冲突先提 issue，不许默默改。
- 任何人（或代理）可以随时从零重现项目：源码 + 本文件 + evidence/ 素材 ⇒ 应能还原所有关键结论。

## 一、仓库结构（固定，勿随意改名）

```
TopoSort/
├── AGENTS.md            # 本规范（最高优先级）
├── CONTRIBUTING.md      # 人类组员协作须知（简要，指向本文件）
├── app/                 # 全部源码（Python 3 + PySide6）
│   ├── models.py        # 图模型 + <a,b> 解析 + Kahn + 全序枚举 + 环检测（算法必须自研）
│   ├── events.py        # Step 事件流：Enqueue/Consume/Fork/Complete/DeadEnd/Cycle
│   ├── scene.py         # QGraphicsView 场景：分层布局、节点/边动画、候选池
│   ├── ui.py            # 输入区/控制条(速度·暂停·单步)/分支泳道/结果流
│   └── main.py          # 装配 + 程序入口
├── deliverables/        # 最终交付文档（写报告直接在这里写，编号固定）
│   ├── 01-可行性研究报告.md
│   ├── 02-需求分析.md
│   ├── 03-概要设计.md
│   ├── 04-详细设计.md
│   ├── 05-测试报告.md
│   ├── 06-用户手册.md
│   └── 00-项目报告.md   # 按 report-template.doc 组织（含分工表、截图、测试用例）
├── minutes/             # 会议记录，命名 YYYY-MM-DD-主题.md，按模板结构
├── evidence/            # ★ 素材库：只进不改（append-only）
│   ├── decisions/       # 已定稿决策：YYYY-MM-DD-主题.md（与 GitHub issue 一一对应）
│   ├── screenshots/     # 截图：功能名-日期-N.png，每完成一个可见效果立刻截
│   ├── benchmarks.csv   # 性能数据，一行一条：日期,用例名,节点数,边数,结果数,耗时ms,模式
│   └── test-data/       # 测试用例：编号-描述.in / .expected
├── tools/               # 辅助脚本（.doc 文本提取、md→PDF 等）
└── docs/                # 老师下发的原始作业文件（只读，勿改）
```

## 二、四条留档习惯（成本 = “顺手”，违反 = 报告没素材）

1. **决策 → Issue → 留档**：讨论定了就开 issue；定稿当天把结论写成 `evidence/decisions/YYYY-MM-DD-主题.md`（含背景、选项、结论、理由、日期、参与人）。
2. **完成一个可见功能 → 截图**：存 `evidence/screenshots/`，命名 `功能名-YYYYMMDD-N.png`。报告截图永远从这里挑。
3. **性能测试 → 追加一行 CSV**：极速模式每跑一次大图就往 `evidence/benchmarks.csv` 追加，格式见结构注释。不许删改旧行（append-only）。
4. **测试用例 → 存 test-data**：新写一个边界/异常输入，就落成 `.in` + `.expected` 两个文件。测试报告的用例表由此自动成形。

## 三、开发红线

- **算法必须自研**（Kahn 排序、全序枚举、环检测）——这是作业考点，禁用 networkx 等库的现成排序。
- 库只用于：GUI（PySide6）、打包（PyInstaller）。新增依赖须开 issue 讨论并留档。
- 技术栈已定案（见 Issue #1）：**Python 3 + PySide6 + PyInstaller 单文件**，组员不得私自更换。
- `docs/` 内老师文件只读。
- 提交信息格式：`类型: 摘要`，类型 ∈ {feat, fix, docs, test, refactor, evidence}。

## 四、AI 代理附加要求

- 开工前：读本文件 → `git log`/`evidence/decisions/` 了解已定决策 → 有疑问先提 issue。
- 完成任务后：按第二节留档习惯补齐素材（截图/CSV/决策 md），并更新本文件中已过时的描述。
- 不确定 = 不猜：向 issue 提问，等组长确认后再动手。
