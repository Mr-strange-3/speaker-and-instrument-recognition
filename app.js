const express =require('express');
const { spawn }=require('child_process');
const multer =require ('multer');
const path=require('path');
const prompt=require('prompt-sync')({sigint:true});
const cors=require('cors');
const app=express();
//const port=3000;
app.use(express.json());
const storage=multer.diskStorage({destination:function(req,file,cb){cb(null,'uploads/');},filename:function(req,file,cb){cb(null,file.originalname);}});
const upload=multer({storage:storage});
app.use(cors());

// app.get('/', (req, res) => {
//     res.sendFile(path.join(__dirname, 'index.html'));
// });
const port=4000;
app.post('/audio',upload.single('audioFile'),(req,res)=>{
    console.log('entered the post request');
    //const audiofilepath=path.join(__dirname,'uploads',req.file.filename);
    //const audiofilepath=prompt("enter the path");
   //const audiofilepath='/Users/tusharkumar/Desktop/project2/TestingAudio/AamirKhan_6.wav';
    const python_path='testing.py';
    const python_process=spawn('python',[python_path,req.file.path]);

   // console.log(audiofilepath);
    python_process.stdout.on('data',(data)=>{
        const outputData=data.toString()
        console.log(`recieved output from python:${outputData}`);

        res.json({ outputData }); // Sending data as a JSON object
    });
     python_process.stderr.on('data', (data) => 
     {
         console.error(`Error from Python: ${data}`);
         res.status(500).json({ error: 'An error occurred' });
     });


});
app.post('/precisionA', (req, res) => {
    console.log('enterd precison');
    const python_path = 'speaker_precision.py';
    const python_process = spawn('python', [python_path]);
    console.log("getting data");
    python_process.stdout.on('data', (data) => {
        const outputData = data.toString();
        console.log(`Received output from python: ${outputData}`);

        res.json({ outputData }); // Sending data as a JSON object
    });

    python_process.stderr.on('data', (data) => {
        console.error(`Error from Python: ${data}`);
        res.status(500).json({ error: 'An error occurred' });
    });
});
app.post('/precisioni', (req, res) => {
    console.log('enterd precisoni');
    const python_path = 'instrument_p.py';
    const python_process = spawn('python', [python_path]);
    console.log("getting data");
    python_process.stdout.on('data', (data) => {
        const outputData = data.toString();
        console.log(`Received output from python: ${outputData}`);

        res.json({ outputData }); // Sending data as a JSON object
    });

    python_process.stderr.on('data', (data) => {
        console.error(`Error from Python: ${data}`);
        res.status(500).json({ error: 'An error occurred' });
    });
});


app.post('/instrument',upload.single('audioFile2'),(req,res)=>{
    console.log('entered the post request');
    //const audiofilepath=path.join(__dirname,'uploads',req.file.filename);
    //const audiofilepath=prompt("enter the path");
   //const audiofilepath='/Users/tusharkumar/Desktop/project2/TestingAudio/AamirKhan_6.wav';
    const python_path='instrument-testing.py';
    const python_process=spawn('python',[python_path,req.file.path]);

   // console.log(audiofilepath);
    python_process.stdout.on('data',(data)=>{
        const outputData=data.toString()
        console.log(`recieved output from python:${outputData}`);

        res.json({ outputData }); // Sending data as a JSON object
    });
     python_process.stderr.on('data', (data) => 
     {
         console.error(`Error from Python: ${data}`);
         res.status(500).json({ error: 'An error occurred' });
     });


});

app.listen(port, () =>
{
    console.log(`Server running at http://localhost:${port}`);
});
