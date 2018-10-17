var mysql = require('mysql');
var fs = require('fs');
var config = JSON.parse(fs.readFileSync('config.json', 'utf8'));



var con = mysql.createConnection({
  host: config.sqldatabase,
  user: config.sqlusername,
  password: config.sqlpassword,
  database: "mysql"
});


con.connect(function(err) {
  if(err) throw err;
  con.query("SELECT user,host FROM user", function (err, result, fields) {
    if (err) throw err;
    console.log(result[2]);
  });
});
