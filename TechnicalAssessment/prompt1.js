// Prompt #1
// You're given an array of objects representing products in an e-commerce system. Each product object has the following properties:

// | Key      | Type     | Description                       |
// | -------- | -------- | --------------------------------- |
// | id       | number   | Unique identifier for the product |
// | name     | string   | Name of the product               |
// | category | string   | Category of the product           |
// | price    | number   | Price of the product              |
// | stock    | number   | Current stock quantity            |
// | ratings  | number[] | Customer ratings (1-5)            |

// Your task is to create a function called analyzeInventory that takes this array of product objects and performs the following operations and returns a report object with the results:

// 1. Calculate the total value of the inventory (sum of price * stock for all products)
// 2. Find the product with the highest average rating
// 3. Group products by category
// 4. Identify products that are low in stock (less than 10 items)
// 5. Find the average price for each category

const products = [
  {
    id: 1,
    name: "Laptop",
    category: "Electronics",
    price: 999.99,
    stock: 50,
    ratings: [4, 5, 3, 5],
  },
  { id: 2, name: "Shirt", category: "Clothing", price: 24.99, stock: 100, ratings: [4, 4, 5] },
  {
    id: 3,
    name: "Coffee Maker",
    category: "Home Appliances",
    price: 89.99,
    stock: 30,
    ratings: [5, 4, 4, 5, 3],
  },
  { id: 4, name: "Book", category: "Books", price: 14.99, stock: 200, ratings: [4, 4, 4] },
  {
    id: 5,
    name: "Smartphone",
    category: "Electronics",
    price: 599.99,
    stock: 75,
    ratings: [3, 4, 4, 5, 5],
  },
  { id: 6, name: "Socks", category: "Clothing", price: 9.99, stock: 150, ratings: [5, 5, 4] },
  {
    id: 7,
    name: "Blender",
    category: "Home Appliances",
    price: 49.99,
    stock: 8,
    ratings: [4, 3, 4],
  },
];

// let reportObject = {
//   totalValue: 0,
//   highestRatedProduct: "", //name of the product
//   productsByCategory: {},
//   productsLowInStock: [],
//   averagePriceByCategory: {},
// };

const inventoryTotalValue = (products) => {
  let sum = 0;
  for (let i = 0; i < products.length; i++) {
    sum += products[i].price * products[i].stock;
  }
  return sum;
};

const highestRated = (products) => {
  let bestProductName = "";
  let maxRating = 1;
  for (let i = 0; i < products.length; i++) {
    // individual product rating
    let productAverageRating = 0;
    for (let j = 0; j < products[i].ratings.length; j++) {
      productAverageRating += products[i].ratings[j];
    }
    productAverageRating = productAverageRating / products[i].ratings.length;

    if (productAverageRating > maxRating) {
      maxRating = productAverageRating;
      bestProductName = products[i].name;
    }
  }
  return bestProductName;
};

const groupByCategory = (products) => {
  const categories = new Map();
  for (let i = 0; i < products.length; i++) {
    const category = products[i].category;
    if (!categories.has(category)) {
      categories.set(category, [products[i]]);
    } else {
      categories.set(category, [...categories.get(category), products[i]]);
    }
  }
  return categories;
};

const lowInStockProducts = (products) => {
  return products.filter((product) => product.stock < 10);
};

const getAveragePriceByCategory = (productCategoryMap) => {
  const averageCategoryPrice = new Map();
  for (const productType of productCategoryMap.keys()) {
    let averagePrice = 0;
    const productsInCategory = productCategoryMap.get(productType);
    for (let i = 0; i < productsInCategory.length; i++) {
      averagePrice += productsInCategory[i].price;
    }
    averagePrice = averagePrice / productsInCategory.length;
    averageCategoryPrice.set(productType, averagePrice);
  }
  return averageCategoryPrice;
};

const analyzeInventory = (products) => {
  // Calculate the total value of the inventory (sum of price * stock for all products)
  const total = inventoryTotalValue(products);
  // Find the product with the highest average rating
  const bestProduct = highestRated(products);
  // Group products by category
  const productsCategories = groupByCategory(products);
  // Identify products that are low in stock (less than 10 items)
  const itemsToRestock = lowInStockProducts(products);
  // Find the average price for each category
  const averagePriceByCategory = getAveragePriceByCategory(productsCategories);
  return {
    totalValue: total,
    highestRatedProduct: bestProduct,
    productsByCategory: productsCategories,
    productsLowInStock: itemsToRestock,
    averagePriceByCategory: averagePriceByCategory,
  };
};

// console.log(analyzeInventory(products));
