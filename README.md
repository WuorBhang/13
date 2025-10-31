# Django M-Pesa Integration 💳

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![M-Pesa](https://img.shields.io/badge/M--Pesa-00A651?style=for-the-badge)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A robust Django integration for Safaricom's M-Pesa Daraja API, providing seamless implementation of STK Push, Query, and Callback functionalities.

## ✨ Features

- 🔐 Automatic OAuth Access Token generation
- 💰 **STK Push** payment initiation
- 🔍 **Transaction Status Query** support
- 📨 **Callback** response handling
- 🔧 Built for **Sandbox** environment and easily configurable for production
- 📝 Comprehensive documentation
- 🛡️ Secure credential management

## 📁 Project Structure

```plaintext
django_mpesa/
│
├── 📄 stkPush.py           # Handles M-Pesa STK Push request
├── 📄 query_stk.py         # Handles STK push query status
├── 📄 callback.py          # Handles M-Pesa callback responses
├── 📄 generateAccessToken.py # Fetches OAuth access token
├── 📄 views.py             # API views and endpoints
├── 📄 urls.py             # URL routing configuration
├── 📄 settings.py         # Django settings and configurations
└── 📄 asgi.py/wsgi.py     # Application servers
```

## ⚙️ Requirements & Installation

### Prerequisites

- Python 3.10 or higher
- Django 4.0 or higher
- pip (Python package manager)

### Dependencies

```plaintext
python-dotenv>=0.19.0  # Environment variable management
requests>=2.26.0       # HTTP requests
django>=4.0.0         # Web framework
```

### Quick Start 🚀

1. Clone the repository:

    ```bash
    git clone https://github.com/WuorBhang/13.git
    cd 13
    ```

2. Create and activate virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables:

    ```bash
    cp .env.example .env  # Copy example env file
    # Edit .env with your credentials
    ```

5. Run migrations:

    ```bash
    python manage.py migrate
    ```

6. Start development server:

    ```bash
    python manage.py runserver
    ```

## 🔐 Environment Variables Configuration

Create a `.env` file in your project root with the following variables:

```plaintext
# M-Pesa API Credentials
MPESA_ENVIRONMENT="sandbox"  # or "production"
MPESA_CONSUMER_KEY="your_consumer_key"
MPESA_CONSUMER_SECRET="your_consumer_secret"

# Business Configuration
MPESA_SHORTCODE="174379"  # Your organization's shortcode
MPESA_PASSKEY="bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
MPESA_BUSINESS_NAME="Your Business Name"

# Endpoint URLs
MPESA_CALLBACK_URL="api/mpesa/callback"
MPESA_TIMEOUT_URL="api/mpesa/timeout"
MPESA_RESULT_URL="api/mpesa/result"

# Transaction Configuration
MPESA_TRANSACTION_TYPE="CustomerPayBillOnline"

# API Base URLs (Sandbox)
MPESA_API_BASE="api.safaricom.co.ke"
MPESA_AUTH_ENDPOINT="oauth/v1/generate"
MPESA_PAYMENT_ENDPOINT="mpesa/stkpush/v1/processrequest"
MPESA_QUERY_ENDPOINT="mpesa/stkpushquery/v1/query"

# Optional Configuration
MPESA_ACCOUNT_REFERENCE="CompanyXYZ"
MPESA_TRANS_DESC="Payment for service"
```

## 📚 Usage Examples

### Token Generation

```python
from django_mpesa.generateAccessToken import generate_access_token

# Get access token
access_token = generate_access_token()
print(access_token)  # Returns: {"access_token": "ACCESS_TOKEN_STRING"}
```

### Payment Initiation

```python
from django_mpesa.stkPush import initiate_stk_push

# Payment details
phone_number = "254712345678"
amount = "100"
account_reference = "INV001"
transaction_desc = "Payment for service"

# Initiate payment
response = initiate_stk_push(phone_number, amount, account_reference, transaction_desc)
```

### Status Query

```python
from django_mpesa.query_stk import query_stk_status

# Check transaction status
checkout_request_id = "ws_CO_123456789"
response = query_stk_status(checkout_request_id)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch:

    ```bash
    git checkout -b feature/AmazingFeature
    ```

3. Commit your changes:

    ```bash
    git commit -m 'Add some AmazingFeature'
    ```

4. Push to the branch:

    ```bash
    git push origin feature/AmazingFeature
    ```

5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Safaricom Daraja API](https://developer.safaricom.co.ke/) - Official M-Pesa API documentation
- [Django Framework](https://www.djangoproject.com/) - The web framework for perfectionists with deadlines

## 📮 Support

Need help? We're here for you!

- Create an issue in this repository
- Star this repo if you find it helpful
- Follow for updates

---

Made with ❤️ for the Django community