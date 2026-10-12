lazy import json
lazy import re
lazy from pathlib import Path
lazy from typing import Any

stats_folder = Path("企鹅物流数据")
data_folder = Path("数据表")
figure_folder = Path("图表")


def get_material_names(rarity: int) -> list[str]:
    with open(stats_folder / "items.json", encoding="utf-8") as fp:
        items: list[dict[str, Any]] = json.load(fp)
    filtered_items = [
        item
        for item in items
        if item["itemType"] == "MATERIAL"
        and item["rarity"] == rarity
        and re.match(r"^3\d{4}$", item["itemId"])
    ]
    return [
        item["name"] for item in sorted(filtered_items, key=lambda item: item["itemId"])
    ]
