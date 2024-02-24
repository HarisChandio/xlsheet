import json

with open("second.json", "r") as f:
    data = json.loads(f.read())

class_list = [
    "BBA-4B",
    "BSAF-8",
    "BSSS-8",
    "BBA-3A",
    "BSAF-3",
    "BSSS-2",
    "BSAF-7",
    "BBA-1A",
    "BBA-1B",
    "BSSE-6A",
    "BSSE-6B",
    "BBA-5B",
    "BBA-7A",
    "BSSE-4A",
    "BBA-2A",
    "BBA-8B",
    "BSAF-1",
    "BSSS-1",
    "BSSE-2B",
    "BBA-6A",
    "BBA-7B",
    "BSCS-8A",
    "BSCS-2A",
    "BBA-6B",
    "MBA-72",
    "BSAF-6",
    "BSAF-4",
    "BSAI-2A",
    "BSSE-2A",
    "BSSS-4",
    "BSCS-4B",
    "BSSE-4B",
    "BSSE-8A",
    "BSCS-2B",
    "BBA-2B",
    "BBA-8A",
    "BSAF-2",
    "BBA-7",
    "BSSS-7",
    "BSSS-5",
    "BSCS-6A",
    "BBA-3B",
    "BSCS-4A",
    "BSCS-2C",
    "BSSS-3",
    "BBA-4A",
    "BBA-8",
    "BBA-5A",
    "BSAF-5",
    "MSCS-2",
    "MSCS-4",
]
time = [
    "8:15AM to 10:45AM",
    "11:30AM to 2:00PM",
    "2:45PM to 5:15PM",
    "6:00PM to 8:30PM",
]

final_obj = {}


def looping_data(class_name):
    final_obj[class_name] = {}

    for key, values in data.items():
        for time, name in values.items():
            # print(time)
            for room, info in name.items():
                # print(info)
                if class_name in info:
                    if not final_obj[class_name].get(key, None):
                        final_obj[class_name][key] = {}

                    # print(final_obj)
                    if not final_obj[class_name][key].get(time, None):
                        final_obj[class_name][key][time] = {}
                    #     print(final_obj)

                    final_obj[class_name][key][time] = {
                        room: [data.strip() for data in info.split(class_name)]
                    }
                    # print(key, room, time, info.split(class_name))


for i in class_list:
    looping_data(i)


print(final_obj)

with open("final.json", "w+") as f:
    f.write(json.dumps(final_obj))

""" 
{
 class: {
     day: {
      time: {
        room : [sub, prof]
      }
     }
 }
}

"""
