"""Обновляет карточку по открытым данным GitHub. Только стандартная библиотека."""
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.request import Request, urlopen
import argparse
import html
import json
import os
import re

from ocean_theme import oceanize

ROOT = Path(__file__).resolve().parents[1]
USER = "alphaserver777"


def fetch(path, api=True):
    origin = "https://api.github.com" if api else "https://github.com"
    headers = {"User-Agent": "alphaserver777-profile", "Accept-Language": "en-US"}
    token = os.environ.get("GH_TOKEN")
    if api and token:
        headers["Authorization"] = "Bearer " + token
    with urlopen(Request(origin + path, headers=headers), timeout=30) as response:
        return response.read().decode("utf-8")


class Calendar(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dates = {}
        self.counts = {}
        self.target = None
        self.buffer = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-date" in attrs and "id" in attrs:
            self.dates[attrs["id"]] = date.fromisoformat(attrs["data-date"])
        if tag == "tool-tip" and attrs.get("for") in self.dates:
            self.target = attrs["for"]
            self.buffer = []

    def handle_data(self, data):
        if self.target:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag != "tool-tip" or not self.target:
            return
        value = " ".join("".join(self.buffer).split())
        match = re.match(r"([\d,]+) contributions? on ", value)
        if match:
            number = int(match.group(1).replace(",", ""))
        elif value.startswith("No contributions on "):
            number = 0
        else:
            raise ValueError("Изменился формат календаря GitHub: " + value[:100])
        self.counts[self.dates[self.target]] = number
        self.target = None


def collect(today):
    first = today - timedelta(days=364)
    profile = json.loads(fetch(f"/users/{USER}"))
    repos = []
    for page in range(1, 101):
        batch = json.loads(fetch(f"/users/{USER}/repos?per_page=100&page={page}"))
        repos.extend(batch)
        if len(batch) < 100:
            break
    else:
        raise ValueError("Слишком много страниц репозиториев")
    counts = {}
    for year in range(first.year, today.year + 1):
        parser = Calendar()
        parser.feed(fetch(f"/users/{USER}/contributions?from={year}-01-01&to={year}-12-31", api=False))
        counts.update(parser.counts)
    days = [first + timedelta(days=i) for i in range(365)]
    if not all(day in counts for day in days):
        raise ValueError("GitHub вернул неполный календарь; прежняя карточка сохранена")
    return {
        "user": USER, "as_of": today.isoformat(), "from": first.isoformat(),
        "public_repositories": len(repos),
        "original_repositories": sum(not r["fork"] for r in repos),
        "joined_year": profile["created_at"][:4],
        "contributions": sum(counts[d] for d in days),
        "daily": {d.isoformat(): counts[d] for d in days},
    }


def render(data):
    def text(x, y, value, size=20, color="#A1A1A1", weight=400, extra=""):
        return f'<text x="{x}" y="{y}" fill="{color}" font-family="Noto Sans,DejaVu Sans,Arial,sans-serif" font-size="{size}" font-weight="{weight}" {extra}>{html.escape(str(value))}</text>'
    first = date.fromisoformat(data["from"])
    end = date.fromisoformat(data["as_of"])
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="380" viewBox="0 0 1600 380" fill="none">'
    svg += '<title>Открытая активность GitHub за последние 365 дней</title><rect x=".5" y=".5" width="1599" height="379" rx="18" fill="#141414" stroke="#303030"/>'
    svg += text(38, 52, "@" + data["user"], 32, "#EDEDED", 600)
    svg += text(1562, 49, first.strftime("%d.%m.%Y") + " — " + end.strftime("%d.%m.%Y"), 24, extra='text-anchor="end"')
    stats = [("public_repositories", "открытых репозиториев"), ("original_repositories", "без ответвлений"), ("joined_year", "год регистрации")]
    for i, (key, label) in enumerate(stats):
        y = 114 + 78 * i
        svg += text(38, y, data[key], 43, "#F4F4F5", 600)
        svg += text(158, y - 2, label, 23)
    svg += '<path d="M475 86V298" stroke="#303030"/>'
    svg += text(518, 111, f'{data["contributions"]} действий за 365 дней', 32, "#EDEDED", 600)
    svg += text(518, 145, 'Открытый календарь GitHub', 23)
    start = first - timedelta(days=(first.weekday() + 1) % 7)
    colors = ["#242424", "#173C61", "#245D94", "#3387D4", "#52A8FF"]
    maximum = max(data["daily"].values(), default=0)
    for ds, count in data["daily"].items():
        day = date.fromisoformat(ds)
        pos = (day - start).days
        column, row = divmod(pos, 7)
        level = 0 if count == 0 else min(4, max(1, (count * 4 + max(1, maximum) - 1) // max(1, maximum)))
        x = 518 + column * 19
        y = 169 + row * 19
        svg += f'<rect x="{x}" y="{y}" width="14" height="14" rx="3" fill="{colors[level]}"><title>{ds}: {count}</title></rect>'
    svg += '<path d="M38 321H1562" stroke="#303030"/>'
    svg += text(38, 356, "Источник: GitHub · Репозитории и календарь активности", 22)
    svg += text(1562, 356, "Обновлено " + end.strftime("%d.%m.%Y"), 22, extra='text-anchor="end"')
    return oceanize(svg + "</svg>")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=datetime.now(timezone.utc).date().isoformat())
    args = parser.parse_args()
    data = collect(date.fromisoformat(args.date))
    svg = render(data)
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "data/github-stats.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "assets/github-activity.svg").write_text(svg)
    print("Карточка обновлена по данным GitHub:", data["as_of"])


if __name__ == "__main__":
    main()
