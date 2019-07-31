const extract = require("string-extract-class-names");
const fs = require('fs');
const spawn = require("child_process").spawn;

fs.readFile('test.css', (err, data) => {
  f = extract(data.toString());
  for(var i = 0; i < f.length; i++) {
    f[i] = f[i].substring(1);
    if(!isNaN(parseInt(f[i][0], 10))) {
      f.splice(i, 1)
    }
  }
  const pythonProcess = spawn('python',["./script.py", f.join(', ').replace(/\./g,'')]);
  console.log('====================================');
  console.log(f.join(', ').replace(/\./g,''));
  console.log('====================================');

  pythonProcess.stdout.on('data', (d) => {
    // Do something with the data returned from python script
    console.log('====================================');
    console.log(d);
    console.log('====================================');
    });

})
