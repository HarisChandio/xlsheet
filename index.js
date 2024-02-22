const xlsx = require("node-xlsx");
const workbook = xlsx.parse(`${__dirname}/file.xlsx`);
console.log(workbook[0].data);