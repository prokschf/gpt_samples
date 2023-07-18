const cityInput = document.getElementById('city');
const weatherTable = document.getElementById('weather');

cityInput.addEventListener('input', async () => {
  const response = await fetch(`/autocomplete?input=${cityInput.value}`);
  const data = await response.json();
  cityInput.value = data.predictions[0].description;
});

cityInput.addEventListener('change', async () => {
  const response = await fetch(`/weather?city=${cityInput.value}`);
  const data = await response.json();
  weatherTable.innerHTML = `
    <tr>
      <th>Temperature Now</th>
      <td>${data.main.temp}°C</td>
    </tr>
    <tr>
      <th>Weather Now</th>
      <td>${data.weather[0].description}</td>
    </tr>
    <!-- Forecast data will be inserted here -->
  `;
});
