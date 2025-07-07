/* ---------- منو (۳ غذا در هر دسته) ---------- */
const menuItems = [
  /* 🔹 کباب‌ها */
  { id: "1",  name: "چلوکباب سلطانی",     category: "کباب‌ها", description: "کوبیده + برگ با برنج ایرانی", price: 250000, image: "images/kabab_soltani.jpg" },
  { id: "2",  name: "چلو جوجه‌کباب",      category: "کباب‌ها", description: "جوجه زعفرانی با کره",          price: 180000, image: "images/kabab_joojeh.jpg" },
  { id: "3",  name: "کباب برگ",           category: "کباب‌ها", description: "راسته گوساله گریل‌شده",        price: 270000, image: "images/kabab_barg.jpg" },

  /* 🔹 خورش‌ها */
  { id: "4",  name: "قرمه‌سبزی",          category: "خورش‌ها", description: "سبزی تازه، لوبیا قرمز، گوشت",  price: 140000, image: "images/ghorme.jpg" },
  { id: "5",  name: "فسنجان",             category: "خورش‌ها", description: "گردو + رب انار، مرغ ریش‌ریش",  price: 185000, image: "images/fesenjan.jpg" },
  { id: "6",  name: "قیمه",               category: "خورش‌ها", description: "لپه، گوشت، سیب‌زمینی خلالی",   price: 135000, image: "images/gheimeh.jpg" },

  /* 🔹 پلوها */
  { id: "7",  name: "زرشک‌پلو با مرغ",    category: "پلوها",   description: "مرغ زعفرانی + زرشک تازه",     price: 160000, image: "images/zereshk.jpg" },
  { id: "8",  name: "باقالی‌پلو با گوشت", category: "پلوها",   description: "برنج + شوید و باقالی، گوشت ماهیچه", price: 220000, image: "images/baghali.jpg" },
  { id: "9",  name: "لوبیاپلو",           category: "پلوها",   description: "لوبیا سبز، گوشت چرخ‌کرده، برنج", price: 150000, image: "images/lobia.jpg" },

  /* 🔹 دسرها */
  { id: "10", name: "بستنی سنتی",         category: "دسرها",   description: "زعفران، گلاب، خلال پسته",      price: 70000,  image: "images/bastani.jpg" },
  { id: "11", name: "فالوده شیرازی",      category: "دسرها",   description: "رشته یخی، آب‌لیمو و شربت",    price: 65000,  image: "images/faloodeh.jpg" },
  { id: "12", name: "شله‌زرد",            category: "دسرها",   description: "برنج، زعفران، خلال بادام",      price: 60000,  image: "images/sholezard.jpg" }
];

/* ---------- دسته‌ها ---------- */
const categories = ["کباب‌ها", "خورش‌ها", "پلوها", "دسرها"];

/* ---------- رندر دسته‌بندی ---------- */
const categoryListElem = document.getElementById("categoryList");
let selectedCategory = null;                     // null = همهٔ دسته‌ها

function renderCategories() {
  categoryListElem.innerHTML = "";
  categories.forEach(cat => {
    const li = document.createElement("li");
    li.className = "category-item" + (cat === selectedCategory ? " active" : "");
    li.textContent = cat;
    li.addEventListener("click", () => {
      selectedCategory = selectedCategory === cat ? null : cat;   // دوباره کلیک = لغو
      renderCategories();
      renderMenu();
    });
    categoryListElem.appendChild(li);
  });
}
renderCategories();

/* ---------- رندر فهرست غذا ---------- */
const menuContainer = document.getElementById("menuContainer");
function renderMenu() {
  menuContainer.innerHTML = "";
  const term = document.getElementById("searchInput").value.trim();

  const filtered = menuItems.filter(it =>
    (!selectedCategory || it.category === selectedCategory) &&
    it.name.includes(term)
  );

  filtered.forEach(item => {
    const card = document.createElement("div");
    card.className = "menu-card";
    card.innerHTML = `
      <img src="${item.image}" alt="${item.name}">
      <div class="menu-info">
        <h2>${item.name}</h2>
        <p>${item.description}</p>
        <div class="menu-actions">
          <span class="price">${item.price.toLocaleString()} تومان</span>
          <button class="add-btn">افزودن</button>
        </div>
      </div>`;
    card.querySelector(".add-btn").addEventListener("click", () => addToCart(item.id));
    menuContainer.appendChild(card);
  });
}
renderMenu();

/* ---------- سبد خرید ---------- */
const cart = {};                                   // { id: { ...item, quantity } }
const cartList  = document.getElementById("cartItemsList");
const cartTotal = document.getElementById("cartTotal");

function addToCart(id) {
  const item = menuItems.find(i => i.id === id);
  if (!item) return;
  cart[id] ? cart[id].quantity++ : cart[id] = { ...item, quantity: 1 };
  renderCart();
}
function updateQuantity(id, delta) {
  if (!cart[id]) return;
  cart[id].quantity += delta;
  if (cart[id].quantity <= 0) delete cart[id];
  renderCart();
}
function renderCart() {
  cartList.innerHTML = "";
  let total = 0;

  Object.values(cart).forEach(({ id, name, price, quantity }) => {
    total += price * quantity;
    const li = document.createElement("li");
    li.className = "cart-item";
    li.innerHTML = `
      <span class="cart-item-name" title="${name}">${name}</span>
      <div class="counter">
        <button onclick="updateQuantity('${id}', -1)">➖</button>
        <span>${quantity}</span>
        <button onclick="updateQuantity('${id}', 1)">➕</button>
      </div>
      <span>${(price * quantity).toLocaleString()}</span>`;
    cartList.appendChild(li);
  });

  cartTotal.textContent = total.toLocaleString();
}

/* ---------- جست‌وجو ---------- */
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", renderMenu);
