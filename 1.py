from pathlib import Path

p = Path("docs\theme\assets\pymdownx-extras\自定義.css")  # 改成你的實際路徑
css = p.read_text(encoding="utf-8")

repl = {
    "#d6b77c": "#7ad3ff",
    "#f0d49a": "#7ad3ff",
    "#e9c98b": "#7ad3ff",
    "rgba(214, 183, 124": "rgba(122, 211, 255",
    "rgba(214,183,124": "rgba(122,211,255",
}

for a, b in repl.items():
    css = css.replace(a, b)

p.write_text(css, encoding="utf-8")
print("OK: gold -> code-blue")
