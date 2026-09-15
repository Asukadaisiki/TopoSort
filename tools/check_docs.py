#!/usr/bin/env python3
"""文档/素材检查：PR 中被改动的文档所引用的 evidence/ 文件必须真实存在。
用法：python tools/check_docs.py [文件...]  无参数时检查全部 deliverables/*.md
退出码非0 = 检查失败（CI 中直接卡 PR）。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = re.compile(r'evidence/[\w\-./]+\.(?:png|csv|in|expected|md)', re.IGNORECASE)
MIN_BYTES = 20 * 1024  # 截图小于 20KB 视为可疑（可能是空图/占位）


def fail(msg: str) -> None:
    print(f"❌ {msg}")
    global failed
    failed = True


failed = False


def check(md_path: Path) -> None:
    text = md_path.read_text(encoding="utf-8")
    for ref in set(REF.findall(text)):
        target = ROOT / ref
        if not target.exists():
            fail(f"{md_path.name} 引用了不存在的文件: {ref}")
        elif target.suffix.lower() == ".png" and target.stat().st_size < MIN_BYTES:
            fail(f"{md_path.name} 引用的截图过小(<20KB，疑似占位): {ref} ({target.stat().st_size}B)")
        else:
            print(f"✅ {md_path.name} -> {ref}")


def main() -> int:
    args = sys.argv[1:]
    files = [Path(a) for a in args] if args else sorted((ROOT / "deliverables").glob("*.md"))
    if not files:
        print("（无可检查的文档）")
        return 0
    for f in files:
        if f.exists():
            check(f)
    print("---")
    print("❌ 存在不合格项，禁止合并" if failed else "✅ 文档引用检查全部通过")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
