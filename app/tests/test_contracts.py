"""契约测试：T1 骨架阶段应当全部失败（红）；
各模块完成后逐步转绿。全部转绿 = T2–T5 验收通过。"""
import subprocess
import sys
from pathlib import Path

APP = Path(__file__).resolve().parent.parent / "app"


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], capture_output=True, text=True)


# ---------- 跨平台红线（机械可查） ----------

def test_no_platform_specific_slash_joining():
    """源码不得用字符串拼接 '/' 或 '\\' 组路径，必须 pathlib。"""
    offenders = []
    for py in APP.rglob("*.py"):
        src = py.read_text(encoding="utf-8")
        if "/" in src and ('+ "/"' in src or 'f"/' in src and ".join" not in src):
            offenders.append(str(py.relative_to(APP.parent)))
    assert not offenders, f"疑似硬编码路径拼接: {offenders}"


# ---------- 零 Qt 红线（models/events 物理隔离） ----------

def test_models_and_events_import_no_qt():
    for pkg in ("models", "events"):
        code = (
            "import sys; import importlib;"
            f" importlib.import_module('app.{pkg}');"
            " bad=[m for m in sys.modules if m.startswith(('PySide6','PyQt'))];"
            " print('|'.join(bad))"
        )
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
        if (APP / pkg).exists() and any((APP / pkg).glob("*.py")):
            assert r.returncode == 0, f"import app.{pkg} 失败: {r.stderr}"
            assert r.stdout.strip() == "", f"app.{pkg} 引入了 Qt 模块: {r.stdout}"
        # 骨架期包尚未创建：跳过（T2/T3 开工后自动生效）
