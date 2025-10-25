const monthYear = document.getElementById("monthYear");
const daysContainer = document.getElementById("days");

const today = new Date();
const currentMonth = today.getMonth();
const currentYear = today.getFullYear();
const currentDay = today.getDate();

const months = [
  "Janeiro","Fevereiro","Março","Abril","Maio","Junho",
  "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"
];

// Cabeçalho
monthYear.textContent = `${months[currentMonth]} ${currentYear}`;

// Primeiro dia do mês
const firstDay = new Date(currentYear, currentMonth, 1).getDay();
// Último dia do mês
const lastDate = new Date(currentYear, currentMonth + 1, 0).getDate();

// Espaços em branco antes do primeiro dia
for (let i = 0; i < firstDay; i++) {
  const emptyCell = document.createElement("div");
  daysContainer.appendChild(emptyCell);
}

// Preencher os dias
for (let day = 1; day <= lastDate; day++) {
  const dayElem = document.createElement("div");
  dayElem.textContent = day;

  if (day === currentDay) {
    dayElem.classList.add("today");
  }

  daysContainer.appendChild(dayElem);
}
