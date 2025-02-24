# Automation Framework using Playwright and Pytest

## 📌 Overview
This project is an automated testing framework built using Playwright and Pytest. It is designed to test a Fleet Portal by automating login, searching trips, verifying device statuses, and other functionalities.

## 📌 What I Have Done 
- Developed a Page Object Model (POM) for better test organization.
- Implemented fixtures to manage browser sessions efficiently.
- Integrated API request tracking to extract device statuses.
- Designed tests for Login, Trip Search, and Device Status Verification.
- Generated HTML test reports using pytest-html.
- Ensured tests execute sequentially (Login → Trip Search → Drivers Page).

## 📌 What I Implemented 
- **Framework:** Playwright + Pytest
- **Test Design Pattern:** Page Object Model (POM)
- **Session Management:** Single browser session across multiple tests
- **API Response Extraction:** Captures backend API requests and extracts device status
- **Dynamic Locators Handling:** Implemented Playwright's advanced selectors
- **Custom Fixtures:** `conftest.py` manages browser, login session, and test dependencies
- **Test Execution Order:** Ensured proper flow using Pytest Fixtures
- **Test Reporting:** HTML reports via pytest-html

## 📌 Framework Used 
| Feature             | Technology Used          |
|---------------------|--------------------------|
| Automation Tool     | Playwright               |
| Test Runner         | Pytest                   |
| Programming Language| Python                   |
| Design Pattern      | Page Object Model (POM)  |
| Reporting           | pytest-html              |
| Session Management  | Playwright Fixtures      |

## 📌 Project Structure 
```
Playwright_Framework/
│── Pages/                  # Page Objects for different UI pages
│   ├── base_page.py        # Base class with common methods
│   ├── login_page.py       # Login page locators & methods
│   ├── trips_page.py       # Trips search page automation
│   ├── devices_page.py     # Device status verification
│
│── Tests/                  # Test scripts
│   ├── test_login.py       # Test for login functionality
│   ├── test_trips.py       # Test for trip search
│   ├── test_devices.py     # Test for device status API verification
│
│── conftest.py             # Fixtures for browser setup & login
│── config.template.json    # Template for configuration
│── requirements.txt        # Dependencies
│── pytest.ini             # Pytest configurations
│── README.md              # Project documentation
```

## Setup Instructions

### 1️⃣ Configuration Setup
1. Copy `config.template.json` to `config.json`
2. Update `config.json` with your credentials:
```json
{
    "base_url": "https://your-staging-url.com",
    "email": "your-email@example.com",
    "password": "your-password"
}
```

### 2️⃣ Install Dependencies
Ensure you have Python installed (recommended Python 3.10+). Install dependencies using:
```sh
pip install -r requirements.txt
```

### 3️⃣ Run Tests
####  Run All Tests:
```sh
pytest --html=Report/report.html --self-contained-html
```

#### Run Specific Test:
```sh
pytest Tests/test_login.py
```

#### Run Tests with Debug Mode:
```sh
pytest -s -v
```

####  Clear Pytest Cache:
```sh
pytest --cache-clear
```


