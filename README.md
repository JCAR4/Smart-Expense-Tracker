# Smart-Expense-Tracker

## Overview
**Smart Expense Categorizer** is a Python-based project that uses **Machine Learning** to automatically classify your expenses into categories such as **Food, Travel, and Utilities**. It provides **interactive visual dashboards** to track spending patterns and detect unusual expenses. Additionally, it can optionally extract expense details from **receipts using OCR**.

---

## Features
- Classify expenses using transaction descriptions with ML
- Visualize spending trends with **Matplotlib** and **Seaborn**
- Detect unusual/high-value expenses
- Optional **OCR integration** to read receipts and automatically categorize expenses

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Smart-Expense-Categorizer.git
cd Smart-Expense-Categorizer
````

2. Install required Python packages:

```bash
pip install -r requirements.txt
```

**Required libraries**:
`pandas`, `scikit-learn`, `matplotlib`, `seaborn`, `easyocr`, `opencv-python`

---

## Usage

1. Open `smart_expense.py` in any Python IDE (VS Code, PyCharm) or run from terminal:

```bash
python smart_expense.py
```

2. The script will:

   * Train a simple ML model on sample expense data
   * Predict categories for new expenses
   * Plot spending summaries and category distributions
   * Highlight unusual expenses

3. Optional: Add a receipt image in the folder and enable the OCR section to automatically extract text and categorize expenses.

---

## Sample Dataset

| Description      | Amount | Category  |
| ---------------- | ------ | --------- |
| Pizza Hut Dinner | 500    | Food      |
| Uber Ride        | 300    | Travel    |
| Electricity Bill | 1500   | Utilities |
| Bus Ticket       | 50     | Travel    |
| Dominos Lunch    | 400    | Food      |
| Water Bill       | 600    | Utilities |
| Flight Ticket    | 5000   | Travel    |
| Cafe Coffee      | 250    | Food      |
| Gas Bill         | 1200   | Utilities |

You can replace it with your own bank transaction CSV or manually typed expenses.

---

## Visualization

* **Category Distribution:** Shows the number of transactions per category
* **Spending Breakdown:** Pie chart showing the share of expenses per category
* **Unusual Expenses:** Highlights expenses significantly higher than average

*(Add screenshots here if you want for GitHub preview)*

---

## Future Improvements

* Add a **GUI interface** using Tkinter or Streamlit
* Connect to **real bank APIs** to automatically fetch transactions
* Expand ML model with more categories (Shopping, Entertainment, Bills, etc.)
* Add **monthly/weekly expense summary charts**

---

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for more information.

---

## Author

**Amulya Raj JC**
Indian Institute of Technology Madras

```

Do you want me to do that?
```
