"""TopoSort 应用包。

依赖单向规则（不可违反）：
    ui → scene → events → models
其中 models / events 零 Qt 依赖（CI 强制检查）。
"""
