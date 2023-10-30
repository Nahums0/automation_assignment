# Automation Assignment

## Personal Notes

- Optional features (as listed below) were added for more complex application and for a better showcase of skills.
- There are multiple tests that could have been solved in one test, but I chose to have more than 2 tests to showcase the parallel feature.

# Table of Contents
- [Automation Assignment](#automation-assignment)
  - [Personal Notes](#personal-notes)
- [Table of Contents](#table-of-contents)
  - [Installation Instructions](#installation-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Initialize and Activate Python Virtual Environment](#2-initialize-and-activate-python-virtual-environment)
    - [3. Install Required Packages](#3-install-required-packages)
    - [4. Run the Main Script](#4-run-the-main-script)
  - [Constants Configuration](#constants-configuration)
    - [1. PARALLEL\_WORKERS\_COUNT](#1-parallel_workers_count)
    - [2. DEFAULT\_BROWSER](#2-default_browser)
    - [3. LOG\_FILE\_NAME](#3-log_file_name)
    - [4. WEBSITE\_URL](#4-website_url)
    - [5. EXPECTED\_COMPLETED\_TRANSACTIONS](#5-expected_completed_transactions)
    - [6. EXPECTED\_TOTAL\_BALANCE\_VALUE](#6-expected_total_balance_value)
- [Test Cases](#test-cases)
- [Optional Features](#optional-features)
- [Program Design](#program-design)
      - [Notes](#notes)
      - [Todos](#todos)

## Installation Instructions

Follow the steps below to get started:

### 1. Clone the Repository

```bash
git clone https://github.com/Nahums0/controlup_home_assignment.git
cd controlup_home_assignment
```

### 2. Initialize and Activate Python Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

### 4. Run the Main Script
```bash
python main.py
```

## Constants Configuration

The `constants` file serves as a central configuration file for the project. It contains various constants that define the behavior and settings for the tests. Below are the constants used in the project:

### 1. PARALLEL_WORKERS_COUNT
- **Value:** `3`
- **Description:** Defines the number of parallel workers to be used when running tests concurrently.

### 2. DEFAULT_BROWSER
- **Value:** `"firefox"`
- **Description:** Sets the default browser for the Selenium tests. In this project, Firefox is the default browser.

### 3. LOG_FILE_NAME
- **Value:** `'test.log'`
- **Description:** Specifies the name of the log file.

### 4. WEBSITE_URL
- **Value:** `'https://demo.applitools.com/'`
- **Description:** The URL of the website that the tests will target.

### 5. EXPECTED_COMPLETED_TRANSACTIONS
- **Value:** `3`
- **Description:** The expected number of completed transactions in the transactions table. This value is used for assertions in the tests.

### 6. EXPECTED_TOTAL_BALANCE_VALUE
- **Value:** `"$350"`
- **Description:** The expected total balance value displayed on the page. This value is used for assertions in the tests.

Update these values to achieve different configuration: failing tests, different parallel configuration, etc...

---

# Test Cases

1. **Login functionality:** Function to log into [Demo Applitools](https://demo.applitools.com/). Assume success if redirect.
2. **Completed Transactions Count Assertion:** Count rows marked as "Succeeded" in the transactions table and assert count number to a specific value.
3. **Total Balance Assertion:** Assert total balance value to a specific value

---

# Optional Features

- **Modularized testing:** Create multiple distinct flows, where each independently handles actions like login and transaction count assertion, simulating a real user session.
- **Parallel Testing:** Running each flow in parallel.

---

# Program Design

The primary function initiates multiple flows in parallel, with each flow independently executing a series of actions that simulate a complete user session.

**Wrapper Responsibilities:**
- Keeps data flow.
- Logs progress.
- Error handling.
- Gracefully closes the browser when finished.

---

#### Notes

- Keep the project organized.
- Implement the page object design pattern.
- Create a git repo and document the installation process.

#### Todos

- [x] Init git repo with proper requirements in a virtual environment while writing documentation on how to set up the project.
- [x] Create classes for pages of the application following the page object design pattern.
- [x] Implement basic user flow: login, assertion.
- [x] Implement the entry code to handle parallel execution, logs, and error handling.
- [x] Final refactoring and code review.
- [x] Push and message the recruiter.
