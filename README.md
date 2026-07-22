# Kalshi Predictive Trading Dashboard (Q.U.A.D.S)

## Overview
This project is a Python application designed to monitor Kalshi prediction markets and run automated probability models. 

It features a visual dashboard built with Streamlit (for now) for easy interaction, while keeping the background trading logic completely separate. This design keeps the app organized, easy to test, and flexible for future updates.

---

## Key Functionalities

* **Live Market Dashboard:** Interactive interface to search tickers, inspect live order books, and view prediction metrics.
* **Decoupled Architecture:** The visual dashboard (`app.py`) only communicates with the backend orchestrator (`main.py`), making it easy to swap out the interface later without rewriting core algorithms.
* **Safe Key Management:** Uses a custom environment loader to read local `.env` keys securely, keeping private credentials out of source code and version control.
* **Data Validation & Error Handling (planned):** Validates inputs (e.g., tickers and numeric parameters) before making network requests.
* **Isolated Testing Sandbox:** Includes `kalshi_test.py` to ping the Kalshi API and verify credentials without having to launch the full web interface.

---

## File Structure

* **`app.py`**: The Streamlit user interface (buttons, input boxes, dashboard layouts).
* **`main.py`**: The backend orchestrator that handles data flow and commands the trading logic.
* **`kalshi_test.py`**: A lightweight sandbox script for testing API keys and network connections.
* **`src/`**: Contains core modules for handling API orders (`kalshi_trader.py`), reading secrets (`env_loader.py`), validating data (`conflict_detector.py`), and logging operations (`trade_logger.py`).

---

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt