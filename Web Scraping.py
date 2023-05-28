import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import connect

parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse", type=int)
parser.add_argument("--dbname", help="Enter the name of the database", type=str)
args = parser.parse_args()

amazon_url = "https://www.amazon.in/s?k=mobile&page=3&crid=9DWBZZCNHSU5&qid=1685249070&sprefix=mo%2Caps%2C644&ref" \
             "=sr_pg_ "
page_num_MAX = args.page_num_max
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1, page_num_MAX + 1):
    url = amazon_url + str(page_num)
    print("Get Request for: " + url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")
    all_device = soup.find_all("div", {"class": "s-card-container"})

    for device in all_device:
        device_dict = {}
        device_model = device.find("span", {"class": "a-size-medium a-color-base a-text-normal"})
        if device_model is not None:
            device_dict["device_model"] = device_model.text
            print(device_model.text)

        device_rating = device.find("span", {"class": "a-icon-alt"})
        if device_rating is not None:
            device_dict["device_rating"] = device_rating.text
            print(device_rating.text)

        delivery_by = device.find("span", {"class": "a-color-base a-text-bold"})
        if delivery_by is not None:
            device_dict["delivery_by"] = delivery_by.text
            print("Delivery by: " + delivery_by.text)

        device_tuple = (
            device_dict.get("device_model", None),
            device_dict.get("device_rating", None),
            device_dict.get("delivery_by", None)
        )
        connect.insert_into_table(args.dbname, device_tuple)

        scraped_info_list.append(device_dict)

dataFrame = pd.DataFrame(scraped_info_list)
print("Creating csv file...")
dataFrame.to_csv("Amazon.csv")
connect.get_devices_info(args.dbname)
