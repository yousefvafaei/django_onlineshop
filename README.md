---

# Django Online Shop

## Introduction
This Django project is designed as an online shop application, offering features such as user authentication, product management, cart functionality, order processing, and integration with the ZarinPal payment gateway.

## Features
- **User Authentication:** Secure user registration, login, and account management.
- **Product Management:** Add, edit, delete, and list products with a detailed view.
- **Cart Functionality:** Add/remove items, and proceed to checkout.
- **Order Processing:** Seamless order creation and management.
- **Payment Integration:** ZarinPal API integration for secure payment handling.
- **Bilingual Support (Optional):** Easily configurable to support multiple languages using Django's internationalization tools.

## Requirements
- **Python:** 3.9 or higher
- **Django:** 4.x
- **Database:** PostgreSQL 14 or higher (or SQLite for development)
- **Other Tools:** Docker and Docker Compose (for deployment)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yousefvafaei/django_onlineshop.git
   cd django_onlineshop
   ```

2. **Set up environment variables:**  
   Create a `.env` file in the root directory with the following content:
   ```
   DJANGO_SECRET_KEY=your_secret_key
   DJANGO_DEBUG=True
   DJANGO_ZARINPAL_MERCHANT_ID=your_merchant_id
   ```

3. **Start the application with Docker:**
   ```bash
   docker-compose up --build
   ```

4. **Apply database migrations:**  
   Open a shell inside the Django container and run:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a superuser for the admin panel:**  
   Run the following command inside the container:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the application:**  
   Open your browser and visit: [http://localhost:8000](http://localhost:8000).

## Usage
- **Admin Panel:** Manage products, users, and orders at [http://localhost:8000/admin](http://localhost:8000/admin).  
- **User Views:** Explore products (`/`), manage the cart (`/cart/`), and place orders (`/order/`).

## Notes
- Customize templates and styles according to your project's branding needs.
- Ensure environment variables are securely stored, especially sensitive information like API keys.
- Use `DEBUG=False` and configure the database and server settings for production.

## Credits
Developed by **Yousef Vafaei**.  
Built with ❤️ using Python and Django.

---
