console.log('hello world');

const submit_form = document.querySelector('.submit_form');
const sensor_data_span = document.querySelector('.sensor_data');
const date_span = document.querySelector('.date');
const ac_warning = document.getElementById('ac_warning');

let data = 0;
const init = () => {
  setInterval(renderSensorData, 1000);
  setInterval(renderNotDateTime, 1000);
};

const handleSubmit = (event) => {
  event.preventDefault();
  renderSensorData();
};

const getSensorData = () => {
  return fetch('/getSensorData')
    .then((response) => response.json())
    .then((data) => data.sensor_data);
};

const renderSensorData = async () => {
  data = await getSensorData();
  sensor_data_span.innerText = data;
  data = parseInt(data);
  if (data >= 15000) {
    ac_warning.innerText = '드라이기 사용중';
  } else {
    ac_warning.innerText = '';
  }
};

const getNowDateTime = () => {
  const now = new Date();
  const locale = navigator.language;
  return new Intl.DateTimeFormat(locale, {
    dateStyle: 'medium',
    timeStyle: 'medium',
  }).format(now);
};

const renderNotDateTime = () => {
  date_span.innerText = getNowDateTime();
};
// 24시간에 한 번씩, 날짜 변경될 때만 날짜가 바뀌도록 수정해보기

init();
