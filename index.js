const xlsx = require("node-xlsx");
const workbook = xlsx.parse(`${__dirname}/file.xlsx`);
const data = workbook[0].data

const finalObj = {};

// console.log(workbook[0].data);
const days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"];
let check = false;
let day = "null"

for (let item of data){
    if (days.includes(item[0])){
        console.log("change")
        day = item[0]
        check = true
        continue
    }

    if (check) {
        check = false
        console.log(item);
    }

    for (let i =0; i< item.length; i++) {
        // console.log(interval);
        // if (interval == "Venue"){
        //     continue
        // }
        console.log(i)

        if (finalObj[day] == undefined || finalObj[day][i] == undefined){

            finalObj[day] = {}
            finalObj[day][i] = [item[i]]
        }
        else {
            console.log(item[i]);
            finalObj[day][i].push(item[i])
        }
    }
}

var fs = require('fs');
fs.writeFile('myjsonfile.json', JSON.stringify(finalObj), 'utf8', () => {
    console.log("work done")
});