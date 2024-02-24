from openpyxl import load_workbook

wb = load_workbook(filename="file.xlsx")
sheet = wb["Spring-2024"]


final_dict = {}

#  example  {
# Monday: {
#     time: {
#         room1: subject
#     }
# }
# }


time_scale = {}


def get_row(row):
    for i in range(2, len(row)):
        time_scale[i] = row[i].value
        final_dict[current_day][time_scale[i]] = {}


def update_room_data(row):
    room = row[0].value
    if room:
        for i in range(2, len(row)):
            if row[i].value:
                final_dict[current_day][time_scale[i]][room] = row[i].value


current_day = None

for row in sheet.rows:
    if row[0].value in [
        "MONDAY",
        "TUESDAY",
        "WEDNESDAY",
        "THURSDAY",
        "FRIDAY",
        "SATURDAY",
    ]:
        current_day = row[0].value
        final_dict[current_day] = {}
        print(row[0].value)
    elif row[0].value and row[0].value.strip().lower() == "venue":
        get_row(row)
    else:
        if current_day:
            update_room_data(row)

# print(final_dict)

import json

with open("second.json", "w+") as f:
    f.write(json.dumps(final_dict))
