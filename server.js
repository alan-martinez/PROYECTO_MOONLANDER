const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/guardar-datos', (req, res) => {
  const { altura, velocidad, combustible } = req.body;
  
  // Guardar los datos en un archivo CSV
  const registro = `${altura},${velocidad},${combustible}\n`;
  fs.appendFileSync('datos_entrenamiento.csv', registro);
  
  res.sendStatus(200);
});

app.listen(3000, () => {
  console.log('Servidor iniciado en el puerto 3000');
});
