const clock = document.getElementById("clock");
const amPm = document.getElementById("am-pm");
const day = document.getElementById("day");
const dateNumber = document.getElementById("date-number");
const month = document.getElementById("month");
const year = document.getElementById("year");

function updateTime() {
  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const seconds = now.getSeconds();
  const amOrPm = hours >= 12 ? "PM" : "AM";

  clock.textContent = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
  amPm.textContent = amOrPm;

  const days = [
    "SUN",
    "MON",
    "TUE",
    "WED",
    "THU",
    "FRI",
    "SAT",
  ];
  const daysIndex = now.getDay();
  day.textContent = days[daysIndex];

  const months = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
  ];
  const monthsIndex = now.getMonth();
  month.textContent = months[monthsIndex];

  dateNumber.textContent = now.getDate();
  year.textContent = now.getFullYear();
}

setInterval(updateTime, 1000);