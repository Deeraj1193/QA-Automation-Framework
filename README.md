# QA Automation Framework (Python + Selenium + Pytest)

![Tests](https://github.com/Deeraj1193/QA-Automation-Framework/actions/workflows/tests.yml/badge.svg)

A test automation framework demonstrating **UI and API automation testing** using Python.
The project uses the **Page Object Model (POM)** design pattern and integrates **GitHub Actions CI** to automatically run tests on every push.

---

## Features

* Selenium WebDriver UI automation
* API testing using Requests
* Pytest test runner
* Page Object Model (POM) architecture
* HTML test reports
* GitHub Actions Continuous Integration
* Automated test execution on every push

---

## Tech Stack

* Python
* Selenium
* Pytest
* Requests
* GitHub Actions

---

## Project Structure

```
QA-Automation-Framework
│
├── .github/workflows
│   └── tests.yml          
│
├── pages                  
│   ├── login_page.py
│   ├── inventory_page.py
│   └── checkout_page.py
│
├── tests
│   ├── api                
│   │   ├── test_posts_api.py
│   │   └── test_users_api.py
│   │
│   └── ui                 
│       ├── test_login.py
│       ├── test_cart.py
│       └── test_checkout.py
│
├── utils                 
│   ├── driver_factory.py
│   └── config.py
│
├── requirements.txt
├── pytest.ini
└── conftest.py
```

---

## Running Tests

Install dependencies:

```
pip install -r requirements.txt
```

Run all tests:

```
pytest tests
```

Generate HTML report:

```
pytest tests --html=reports/report.html
```

---

## Continuous Integration

This project uses **GitHub Actions** to automatically run tests on every push.

The pipeline installs dependencies and runs the test suite using Pytest.

---

## Future Improvements

* Add screenshot capture on test failure
* Implement logging system
* Add parallel test execution
* Integrate Allure reporting
