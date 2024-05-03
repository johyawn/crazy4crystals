document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const cartItemCount = document.getElementById('cart-items-count');
    const cartItemsList = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    const checkoutButton = document.getElementById('checkout-button');

    let cart = []; // Initialize an empty array to store cart items

    // Add event listener to each "Add to Cart" button
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const name = event.target.dataset.name;
            const price = parseFloat(event.target.dataset.price);

            addToCart(name, price);
            updateCartItemCount();
            updateCartItemsList(); // Update the cart items list
            updateCartTotal(); // Update the cart total
        });
    });

    // Function to add item to the cart
    function addToCart(name, price) {
        // Check if the item already exists in the cart
        const existingItemIndex = cart.findIndex(item => item.name === name);
        if (existingItemIndex !== -1) {
            // If the item already exists, increment its quantity
            cart[existingItemIndex].quantity++;
        } else {
            // If the item does not exist, add it to the cart with quantity 1
            cart.push({ name, price, quantity: 1 });
        }
    }

    // Function to update cart items count displayed in the header
    function updateCartItemCount() {
        // Calculate the total quantity of items in the cart
        const totalQuantity = cart.reduce((total, item) => total + item.quantity, 0);
        cartItemCount.textContent = totalQuantity;
    }

    // Function to update the cart items list displayed in the overlay
    function updateCartItemsList() {
        // Clear previous items in the list
        cartItemsList.innerHTML = '';
        // Add each item to the list
        cart.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name} - $${item.price.toFixed(2)} x ${item.quantity}`;
            cartItemsList.appendChild(li);
        });
    }

    // Function to update the total price of all items in the cart
    function updateCartTotal() {
        // Calculate the total price of all items in the cart
        const totalPrice = cart.reduce((total, item) => total + (item.price * item.quantity), 0);
        cartTotal.textContent = `$${totalPrice.toFixed(2)}`;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const openCartBtn = document.getElementById('open-cart-btn');
    const closeCartBtn = document.getElementById('close-cart-btn');
    const cartOverlay = document.getElementById('cart-overlay');

    // Open cart overlay when the open cart button is clicked
    openCartBtn.addEventListener('click', function() {
        cartOverlay.style.display = 'block';
    });

    // Close cart overlay when the close cart button is clicked
    closeCartBtn.addEventListener('click', function() {
        cartOverlay.style.display = 'none';
    });
});

checkoutButton.addEventListener('click', () => {
    // Redirect user to the checkout page
    window.location.href = '/checkout';
});