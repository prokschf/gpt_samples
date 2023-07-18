import React, { useState } from 'react';
import SearchBox from './SearchBox';
import WeatherTable from './WeatherTable';
import fetchWeatherData from './fetchWeatherData';

function App() {
  const [weatherData, setWeatherData] = useState(null);

  const handlePlaceSelect = async (placeId) => {
    const data = await fetchWeatherData(placeId);
    setWeatherData(data);
  };

  return (
    <div className="App">
      <SearchBox onPlaceSelect={handlePlaceSelect} />
      {weatherData && <WeatherTable data={weatherData} />}
    </div>
  );
}

export default App;
