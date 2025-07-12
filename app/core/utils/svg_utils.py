from pathlib import Path

def load_svg(path: Path, size: str = "w-4 h-4") -> str:
    try:
        svg = path.read_text()
        return svg.replace("<svg", f'<svg class="{size}"')
    except FileNotFoundError:
        return ""
