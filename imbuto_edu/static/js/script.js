/* ====================================
   IMBUTO EDU - JAVASCRIPT PART 1
   BASIC INTERACTIVITY
==================================== */

/* =========================
   MOBILE MENU TOGGLE
========================= */

// Get elements
const nav = document.querySelector("nav ul");
const menuToggle = document.createElement("div");

// Create menu button dynamically
menuToggle.innerHTML = "☰";
menuToggle.style.fontSize = "28px";
menuToggle.style.cursor = "pointer";
menuToggle.style.color = "white";

// Add it to navbar
const navbar = document.querySelector("nav");
navbar.prepend(menuToggle);

// Toggle menu on click
menuToggle.addEventListener("click", () => {
    nav.classList.toggle("active");
});


/* =========================
   SMOOTH SCROLL FOR LINKS
========================= */

document.querySelectorAll("nav ul li a").forEach(link => {
    link.addEventListener("click", function (e) {
        const targetId = this.getAttribute("href");

        if (targetId.startsWith("#")) {
            e.preventDefault();

            const target = document.querySelector(targetId);

            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 70,
                    behavior: "smooth"
                });
            }
        }
    });
});


/* =========================
   SIMPLE BUTTON FEEDBACK
========================= */

document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        btn.style.transform = "scale(0.95)";

        setTimeout(() => {
            btn.style.transform = "scale(1)";
        }, 150);
    });
});/* ====================================
   IMBUTO EDU - JAVASCRIPT PART 2
   SEARCH + DYNAMIC FEATURES
==================================== */

/* =========================
   SEARCH FUNCTIONALITY
========================= */

// Get search elements
const searchInput = document.querySelector(".search-box input");
const searchButton = document.querySelector(".search-box button");

if (searchInput && searchButton) {
    searchButton.addEventListener("click", () => {
        const query = searchInput.value.toLowerCase().trim();

        if (query === "") {
            alert("Please enter something to search.");
            return;
        }

        // Simple demo search logic
        alert("Searching for: " + query);

        // You can later connect this to real school data
    });
}


/* =========================
   FILTER SCHOOL CARDS (BASIC)
========================= */

const schoolCards = document.querySelectorAll(".school-card");

function filterSchools(keyword) {
    schoolCards.forEach(card => {
        const text = card.innerText.toLowerCase();

        if (text.includes(keyword.toLowerCase())) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}

// Example: live filtering from search input
if (searchInput) {
    searchInput.addEventListener("keyup", () => {
        const value = searchInput.value.trim();

        if (value.length > 0) {
            filterSchools(value);
        } else {
            schoolCards.forEach(card => {
                card.style.display = "block";
            });
        }
    });
}


/* =========================
   DYNAMIC HOVER INFO (CARDS)
========================= */

document.querySelectorAll(".category-card").forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.background = "#f0f4ff";
    });

    card.addEventListener("mouseleave", () => {
        card.style.background = "white";
    });
});


/* =========================
   SCROLL REVEAL EFFECT
========================= */

const revealElements = document.querySelectorAll(".school-card, .category-card, .stat-card");

const revealOnScroll = () => {
    const windowHeight = window.innerHeight;

    revealElements.forEach(el => {
        const elementTop = el.getBoundingClientRect().top;

        if (elementTop < windowHeight - 100) {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
            el.style.transition = "0.6s ease";
        } else {
            el.style.opacity = "0";
            el.style.transform = "translateY(20px)";
        }
    });
};

window.addEventListener("scroll", revealOnScroll);
revealOnScroll();/* ====================================
   IMBUTO EDU - JAVASCRIPT PART 3
   MINI DATA SYSTEM (SIMULATED DATABASE)
==================================== */

/* =========================
   FAKE SCHOOL DATABASE
========================= */

const schools = [
    {
        name: "Gasabo High School",
        location: "Kigali",
        type: "Academic",
        sports: "Football, Basketball",
        ranking: 1
    },
    {
        name: "Nyamata Secondary School",
        location: "Bugesera",
        type: "Academic",
        sports: "Volleyball",
        ranking: 2
    },
    {
        name: "Rwanda Science Academy",
        location: "Kigali",
        type: "Science & Tech",
        sports: "Athletics",
        ranking: 3
    },
    {
        name: "Elite Sports School",
        location: "Huye",
        type: "Sports",
        sports: "Football, Athletics",
        ranking: 4
    }
];


/* =========================
   RENDER SCHOOLS DYNAMICALLY
========================= */

const schoolGrid = document.querySelector(".school-grid");

function renderSchools(data) {
    if (!schoolGrid) return;

    schoolGrid.innerHTML = "";

    data.forEach(school => {
        const card = document.createElement("div");
        card.classList.add("school-card");

        card.innerHTML = `
            <h3>${school.name}</h3>
            <p><strong>Location:</strong> ${school.location}</p>
            <p><strong>Type:</strong> ${school.type}</p>
            <p><strong>Sports:</strong> ${school.sports}</p>
            <p><strong>Ranking:</strong> #${school.ranking}</p>
            <button>View Details</button>
        `;

        schoolGrid.appendChild(card);
    });
}

// Initial render
renderSchools(schools);


/* =========================
   SMART SEARCH (UPGRADED)
========================= */

function smartSearch(query) {
    const filtered = schools.filter(school => {
        return (
            school.name.toLowerCase().includes(query) ||
            school.location.toLowerCase().includes(query) ||
            school.type.toLowerCase().includes(query) ||
            school.sports.toLowerCase().includes(query)
        );
    });

    renderSchools(filtered);
}


/* =========================
   CONNECT SEARCH INPUT TO DATABASE
========================= */

const searchInput = document.querySelector(".search-box input");

if (searchInput) {
    searchInput.addEventListener("input", () => {
        const value = searchInput.value.toLowerCase().trim();

        if (value === "") {
            renderSchools(schools);
        } else {
            smartSearch(value);
        }
    });
}


/* =========================
   SORT BY RANKING (OPTIONAL FEATURE)
========================= */

function sortByRanking() {
    const sorted = [...schools].sort((a, b) => a.ranking - b.ranking);
    renderSchools(sorted);
}

// You can call this later from a button if you want/* ====================================
   IMBUTO EDU - JAVASCRIPT PART 4
   FILTER SYSTEM + FINAL FRONTEND LOGIC
==================================== */

/* =========================
   FILTER BY TYPE
========================= */

function filterByType(type) {
    if (type === "all") {
        renderSchools(schools);
        return;
    }

    const filtered = schools.filter(school => {
        return school.type.toLowerCase().includes(type.toLowerCase());
    });

    renderSchools(filtered);
}


/* =========================
   FILTER BY LOCATION
========================= */

function filterByLocation(location) {
    const filtered = schools.filter(school => {
        return school.location.toLowerCase().includes(location.toLowerCase());
    });

    renderSchools(filtered);
}


/* =========================
   FILTER BY SPORTS
========================= */

function filterBySport(sport) {
    const filtered = schools.filter(school => {
        return school.sports.toLowerCase().includes(sport.toLowerCase());
    });

    renderSchools(filtered);
}


/* =========================
   RESET VIEW (SHOW ALL)
========================= */

function resetView() {
    renderSchools(schools);
}


/* =========================
   GLOBAL FILTER SYSTEM (READY FOR BUTTONS)
========================= */

// You can connect these to buttons later in HTML

window.filterByType = filterByType;
window.filterByLocation = filterByLocation;
window.filterBySport = filterBySport;
window.resetView = resetView;


/* =========================
   AUTO HIGHLIGHT ACTIVE FILTER (OPTIONAL UX)
========================= */

const filterButtons = document.querySelectorAll("[data-filter]");

filterButtons.forEach(btn => {
    btn.addEventListener("click", () => {
        filterButtons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
    });
});