var mysql = require('mysql');

var con = mysql.createConnection({
  host: 'eu-cdbr-west-02.cleardb.net',
  user: 'b2243985041ca4',
  password: '24807411',
});

con.connect(function (err) {
  if (err) throw err;
  console.log('Connected!');
  con.query('CREATE DATABASE mydb', function (err, result) {
    if (err) throw err;
    console.log('Database created');
  });
});
