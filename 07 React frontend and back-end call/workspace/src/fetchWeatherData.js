import axios from 'axios';

async function fetchWeatherData(placeId) {
  const response = await axios.get(`https://api.openweathermap.org/data/2.5/forecast/daily?placeid=${placeId}&appid=YOUR_OPENWEATHERMAP_API_KEY`);
  return response.data;
}

export default fetchWeatherData;
