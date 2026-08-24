  SauceDemo Automation Framework
# SauceDemo

[![Playwright Tests](https://github.com/sharbeen/SauceDemo/actions/workflows/tests.yml/badge.svg)](https://github.com/sharbeen/SauceDemo/actions)

Playwright automation test suite...
  This project is a test automation suite for the SauceDemo e-commerce website. It is designed to verify the end-to-end flow of a user from logging in to completing a purchase.
  
  🚀 Tech Stack

  - Language: Python 3.12+
  - Automation Tool: Playwright
  - Test Runner: Pytest
  - Design Pattern: Page Object Model (POM)

  🛠️Project Structure

  The project follows the Page Object Model to ensure maintainability and readability:
  - tests/: Contains the test scripts (e.g., testflow.py).
  - pages/: Contains the Page Object classes that encapsulate the locators and actions for each page:
    - loginpage.py: Handles login functionality.
    - inventorypage.py: Handles product selection.
    - checkout_info_page.py: Handles user shipping details.
    - checkout_finalpage.py: Handles final order review.
    - order_confirmation.py: Verifies the final success message.
  - data/: Stores external test data in JSON format (testdata.json) to keep tests data-driven.
  - conftest.py: contains global fixtures and configuration.

  📦 Installation & Setup

  1. Clone the repository:
  git clone <your-repo-url>
  cd SauceDemo
  2. Create and activate a virtual environment:
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  3. Install dependencies:
  pip install -r requirements.txt
  4. Install Playwright Browsers:
  playwright install

  🧪 Running the Tests

  To run the full test suite, use the following command:
  pytest

  To run the tests and see the console output (print statements), use:
  pytest -s

  To run the tests in headed mode (so you can see the browser), use:
  pytest --headed

  📝 Test Flow

  The current automation covers the following scenario:
  1. Navigate to SauceDemo.
  2. Login using credentials from testdata.json.
  3. Select products from the inventory.
  4. Enter shipping information.
  5. Review and finish the checkout process.
  6. Verify the "Thank you for your order!" confirmation message.