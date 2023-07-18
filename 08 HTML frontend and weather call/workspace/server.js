require('dotenv').config();
const express = require('express');
const axios = require('axios');

const app = express();

app.use(express.static('public'));

app.get('/autocomplete', async (req, res) => {
  const response = await axios.get(`https://maps.googleapis.com/maps/api/place/autocomplete/json?input=${req.query.input}&key=${process.env.GOOGLE_PLACES_API_KEY}`);
  res.json(response.data);
});

app.get('/weather', async (req, res) => {
  const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${req.query.city}&appid=${process.env.OPENWEATHERMAP_API_KEY}`);
  res.json(response.data);
});

app.listen(3000, () => console.log('Server is running on port 3000'));
