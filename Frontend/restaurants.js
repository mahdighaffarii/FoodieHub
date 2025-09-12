/*  
const restaurants = [
  { id: "1", name: "رستوران نایب", type: "ایرانی", address: "ولیعصر، تهران", image: "images/naeb.jpg" },
  { id: "2", name: "پیتزا هات", type: "فست‌فود", address: "ونک، تهران", image: "images/pizzahut.jpg" },
  { id: "3", name: "کافه لمیز", type: "کافه", address: "انقلاب، تهران", image: "images/lamiz.jpg" }
];

const categories = ["ایرانی", "فست‌فود", "بین‌المللی", "کافه"];*/
let selectedCategory = null;

const categoryListElem = document.getElementById("categoryList");
const restaurantContainer = document.getElementById("restaurantContainer");

/* ---------- رندر دسته‌ها ---------- */
function renderCategories() {
  categoryListElem.innerHTML = "";
  categories.forEach(cat => {
    const li = document.createElement("li");
    li.className = "category-item" + (cat === selectedCategory ? " active" : "");
    li.textContent = cat;
    li.addEventListener("click", () => {
      selectedCategory = selectedCategory === cat ? null : cat;
      renderCategories();
      renderRestaurants();
    });
    categoryListElem.appendChild(li);
  });
}
renderCategories();

/* ---------- رندر رستوران‌ها ---------- */
function renderRestaurants() {
  restaurantContainer.innerHTML = "";
  const term = document.getElementById("searchInput").value.trim();

  const filtered = restaurants.filter(r =>
    (!selectedCategory || r.type === selectedCategory) &&
    r.name.includes(term)
  );

  if (filtered.length === 0) {
    restaurantContainer.innerHTML = "<p class='empty-msg'>🍴 رستورانی یافت نشد</p>";
    return;
  }

  filtered.forEach(r => {
    const card = document.createElement("div");
    card.className = "menu-card";
    card.innerHTML = `
      <img src="${r.image}" alt="${r.name}">
      <div class="menu-info">
        <h2>${r.name}</h2>
        <p>نوع: ${r.type}</p>
        <p>آدرس: ${r.address}</p>
        <div class="menu-actions">
          <button class="add-btn" onclick="viewMenu('${r.id}')">مشاهده منو</button>
        </div>
      </div>`;
    restaurantContainer.appendChild(card);
  });
}
renderRestaurants();

/* ---------- جستجو ---------- */
document.getElementById("searchInput").addEventListener("input", renderRestaurants);

/* ---------- دکمه مشاهده منو ---------- */
function viewMenu(id) {
  // اینجا می‌تونی به صفحه منو redirect کنی
  window.location.href = `menu.html?restaurant=${id}`;
}
