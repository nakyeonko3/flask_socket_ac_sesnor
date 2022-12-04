let toggle = true;
const turnoff = () => {
  return fetch('/turnoff');
};
const turnon = () => {
  return fetch('/turnon');
};

const turnoffBtn = document.getElementById('turnoff');

const handleClick = async () => {
  if (toggle === true) {
    turnoff();
    toggle = false;
    turnoffBtn.innerText = 'turn on';
  } else {
    turnon();
    toggle = true;
    turnoffBtn.innerText = 'turn off';
  }
};

turnoffBtn.addEventListener('click', handleClick);
