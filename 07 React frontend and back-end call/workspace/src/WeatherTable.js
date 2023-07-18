import React from 'react';

function WeatherTable({ data }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Temperature</th>
          <th>Weather</th>
        </tr>
      </thead>
      <tbody>
        {data.list.map((item) => (
          <tr key={item.dt}>
            <td>{new Date(item.dt * 1000).toLocaleDateString()}</td>
            <td>{item.main.temp}</td>
            <td>{item.weather[0].description}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default WeatherTable;
