"""Generate the OWASP MASWE YAML from the weakness front matter."""

from argparse import ArgumentParser
from pathlib import Path

import yaml


ROOT = Path(__file__).parent.parent

METADATA = {
    "title": "Mobile Application Security Weakness Enumeration (MASWE)",
    "remarks": "The OWASP MASWE (Mobile Application Security Weakness Enumeration) is a list of common security and privacy weaknesses in mobile applications. It acts as the bridge between the OWASP MASVS and the OWASP MASTG.",
}


def front_matter(path: Path) -> dict:
    _, contents = path.read_text().split("---", 1)
    contents, _ = contents.split("---", 1)
    return yaml.safe_load(contents)


def get_maswe_dict(maswe_version: str, weaknesses_dir: Path) -> dict:
    weaknesses = {}
    for path in sorted(weaknesses_dir.glob("**/MASWE-*.md"), key=lambda path: path.stem):
        entry = front_matter(path)
        weaknesses[entry["id"]] = entry

    return {"metadata": METADATA | {"version": maswe_version}, "weaknesses": weaknesses}


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("-w", "--weaknesses", help="Weaknesses Directory", type=Path, default=ROOT / "weaknesses")
    parser.add_argument("-v", "--version", help="MASWE version", default="vx.x.x")
    parser.add_argument("-o", "--output", help="Output file", type=Path, default=Path("OWASP_MASWE.yaml"))
    arguments = parser.parse_args()

    maswe = get_maswe_dict(arguments.version, arguments.weaknesses)

    with arguments.output.open("w") as f:
        yaml.dump(maswe, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=float("inf"))


if __name__ == "__main__":
    main()
