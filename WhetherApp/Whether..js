document.getElementById("btn").addEventListener("click", getWeather);

// Enter key press
document.getElementById("city").addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    getWeather();
  }
});

// Default city on load
window.addEventListener('load', () => {
  getWeatherByLocation();
});

async function getWeather() {
  const city = document.getElementById("city").value;
  if (!city) {
    showError("Please enter a city name");
    return;
  }
  await fetchWeather(city);
}

async function getWeatherByLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;
        try {
          const response = await fetch(`https://api.openweathermap.org/geo/1.0/reverse?lat=${lat}&lon=${lon}&limit=1&appid=YOUR_API_KEY`);
          if (response.ok) {
            const locationData = await response.json();
            if (locationData.length > 0) {
              document.getElementById("city").value = locationData[0].name;
              await fetchWeather(locationData[0].name);
            }
          }
        } catch (error) {
          console.error("Error getting location:", error);
        }
      },
      (error) => {
        console.log("Geolocation permission denied");
        document.getElementById("city").value = "London";
        getWeather();
      }
    );
  } else {
    document.getElementById("city").value = "London";
    getWeather();
  }
}

async function fetchWeather(city) {
  document.querySelector('.loading').style.display = 'block';
  document.getElementById('weather').style.opacity = '0.5';
  hideError();

  try {
    await new Promise(resolve => setTimeout(resolve, 1000));

    // Mock weather data
    const mockWeatherData = {
      name: city,
      main: {
        temp: Math.round(Math.random() * 30 + 5),
        feels_like: Math.round(Math.random() * 30 + 5),
        humidity: Math.round(Math.random() * 100),
        pressure: Math.round(Math.random() * 200 + 1000)
      },
      weather: [
        {
          description: ["Sunny", "Cloudy", "Rainy", "Clear"][Math.floor(Math.random() * 4)],
          icon: "01d"
        }
      ],
      wind: {
        speed: (Math.random() * 10).toFixed(1)
      }
    };

    displayWeather(mockWeatherData);
  } catch (error) {
    showError("Failed to fetch weather data.");
    console.error("Error:", error);
  } finally {
    document.querySelector('.loading').style.display = 'none';
    document.getElementById('weather').style.opacity = '1';
  }
}

function displayWeather(data) {
  document.querySelector('.city-name').textContent = data.name;
  document.querySelector('.current-temp').textContent = `${data.main.temp}°C`;
  document.querySelector('.weather-desc').textContent = data.weather[0].description;

  document.getElementById('humidity').textContent = `${data.main.humidity}%`;
  document.getElementById('wind').textContent = `${data.wind.speed} m/s`;
  document.getElementById('feels-like').textContent = `${data.main.feels_like}°C`;
  document.getElementById('pressure').textContent = `${data.main.pressure} hPa`;

  const weatherIcon = document.querySelector('.weather-icon i');
  const desc = data.weather[0].description.toLowerCase();

  if (desc.includes('sunny') || desc.includes('clear')) {
    weatherIcon.className = 'fas fa-sun';
  } else if (desc.includes('cloud')) {
    weatherIcon.className = 'fas fa-cloud';
  } else if (desc.includes('rain')) {
    weatherIcon.className = 'fas fa-cloud-rain';
  } else if (desc.includes('snow')) {
    weatherIcon.className = 'fas fa-snowflake';
  } else {
    weatherIcon.className = 'fas fa-cloud-sun';
  }
}

function showError(message) {
  const errorElement = document.getElementById('error');
  errorElement.textContent = message;
  errorElement.style.display = 'block';
}

function hideError() {
  document.getElementById('error').style.display = 'none';
}

// Initial display with mock data
window.onload = function() {
  const mockData = {
    name: "London",
    main: {
      temp: 18,
      feels_like: 17,
      humidity: 65,
      pressure: 1012
    },
    weather: [
      {
        description: "Partly Cloudy",
        icon: "02d"
      }
    ],
    wind: {
      speed: 3.5
    }
  };
  displayWeather(mockData);
};
