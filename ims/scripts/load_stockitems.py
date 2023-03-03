import csv
import os
import django
import sys

BASE_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(BASE_DIRECTORY)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ims.settings")
django.setup()

from core.models import Group, SubGroup, StockItem, Inventory


COLUMN_MAPPER = {
    "GROUP_COLUMN": "group",
    "SUBGROUP_COLUMN" : "subgroup",
    "ITEM_NAME" : "name",
    "ITEM_PRICE": "price",
    "ITEM_QUANTITY": "quantity"
}


def process_row(row):
    group_name = row[COLUMN_MAPPER["GROUP_COLUMN"]]
    subgroup_name = row[COLUMN_MAPPER["SUBGROUP_COLUMN"]]
    item_name = row[COLUMN_MAPPER["ITEM_NAME"]]
    item_price = row[COLUMN_MAPPER["ITEM_PRICE"]]
    item_quantity = row[COLUMN_MAPPER["ITEM_QUANTITY"]]

    group_obj, created = Group.objects.get_or_create(name=group_name)

    subgroup_obj, created = SubGroup.objects.get_or_create(group=group_obj, name=subgroup_name)

    item_obj, created = StockItem.objects.get_or_create(
        subgroup=subgroup_obj, 
        name=item_name, 
        defaults={
            "price": item_price
        }
    )

    if not item_quantity:
        item_quantity = 0

    inventory, created = Inventory.objects.get_or_create(
        stockitem=item_obj, 
        defaults={
            "quantity": item_quantity
        }
    )


def process(csvfile):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        i=1
        for row in reader:
            process_row(row)
            print(f"Processed Row {i}: {row}")

if __name__ == "__main__":
    csv_file = input("Please enter the csv path of the file to be loaded: \n")
    process(csv_file)