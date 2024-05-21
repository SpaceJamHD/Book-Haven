const btn = document.querySelector(".switch-btn");
const video = document.querySelector(".video-container");

btn.addEventListener("click", function () {
  if (!btn.classList.contains("slide")) {
    btn.classList.add("slide");
    video.pause();
  } else {
    btn.classList.remove("slide");
    video.play();
  }
});

// preloader
const preloader = document.querySelector(".preloader");

window.addEventListener("load", function () {
  preloader.classList.add("hide-preloader");
});

// aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
document.addEventListener("DOMContentLoaded", function () {
  const buttonNext = document.querySelector(".button-next");
  const buttonPrev = document.querySelector(".button-prev");
  const cards = document.querySelector(".cards");
  const cardWidth = document.querySelector(".card").offsetWidth + 20; // Шаг прокрутки (ширина карточки + отступы)

  let currentPosition = 0;

  buttonNext.addEventListener("click", function () {
    const maxScrollPosition = -(cards.scrollWidth - cards.offsetWidth);
    if (currentPosition > maxScrollPosition) {
      currentPosition -= cardWidth;
      moveCards();
    }
  });

  buttonPrev.addEventListener("click", function () {
    if (currentPosition < 0) {
      currentPosition += cardWidth;
      moveCards();
    }
  });

  function moveCards() {
    cards.style.transition = "transform 0.5s ease";
    cards.style.transform = `translateX(${currentPosition}px)`;
  }
});

const reviews = [
  {
    id: 1,
    name: "Євгеній Казан",
    job: "Письменник",
    img: "../media/items/222.jpg",
    text: "Одна з найвідоміших теорій про Євгена стверджує, що він був самоучкою письменником, який жив у глибоких лісах, подалі від цивілізації. Його твори були написані на листях дерев або вирізані на корі, а потім поширювалися за допомогою усної народної творчості.",
  },
  {
    id: 2,
    name: "Ілля Федяєв",
    job: "Письменник",
    img: "../../media/items/11.webp",
    text: "Легенда стверджує, що Ілля покинув світ буденності, та вирушив у ліси, щоб знайти натхнення у самотності й гармонії з природою. Його твори, повні мудрості та філософії, надихали людей протягом багатьох поколінь.",
  },
  {
    id: 3,
    name: "Іван Авраменко",
    job: "Письменник",
    img: "../../media/items/17.webp",
    text: "Загадкова постать, що оточена легендами та міфами й до цього дня. Дехто стверджує, що він був великим українським письменником,",
  },
];
// select items
const img = document.getElementById("person-img");
const author = document.getElementById("author");
const job = document.getElementById("job");
const info = document.getElementById("info");

const prevBtn = document.querySelector(".prev-btn");
const nextBtn = document.querySelector(".next-btn");
const randomBtn = document.querySelector(".random-btn");

// set starting item
let currentItem = 0;

// load initial item
window.addEventListener("DOMContentLoaded", function () {
  const item = reviews[currentItem];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
});

// show person based on item
function showPerson(person) {
  const item = reviews[person];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
}
// show next person
nextBtn.addEventListener("click", function () {
  currentItem++;
  if (currentItem > reviews.length - 1) {
    currentItem = 0;
  }
  showPerson(currentItem);
});
// show prev person
prevBtn.addEventListener("click", function () {
  currentItem--;
  if (currentItem < 0) {
    currentItem = reviews.length - 1;
  }
  showPerson(currentItem);
});
// show random person
randomBtn.addEventListener("click", function () {
  console.log("hello");

  currentItem = Math.floor(Math.random() * reviews.length);
  showPerson(currentItem);
});
