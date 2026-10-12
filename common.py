import json
from pathlib import Path

stats_folder = Path("企鹅物流数据")
data_folder = Path("数据表")
figure_folder = Path("图表")


def get_material_names(rarity: int) -> list[str]:
    with open(stats_folder / "items.json", encoding="utf-8") as fp:
        items: list[dict] = json.load(fp)
    materials = [item for item in items if item["itemType"] == "MATERIAL"]
    return [
        item["name"]
        for item in sorted(materials, key=lambda item: item["itemId"])
        if item["rarity"] == rarity
    ]
