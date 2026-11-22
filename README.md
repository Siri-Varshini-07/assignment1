# GriidAi – AI-Powered Business Data Analyst

## Project Overview
This project is a business data analysis application developed as part of the GriidAi internship assignment. It analyzes sales data and allows users to ask natural-language questions to obtain useful business insights.

The application uses Python, Pandas, Streamlit, and Plotly to process, analyze, and visualize business data.

## Features
- Business summary showing total sales, profit, orders, and quantity sold.
- Sales analysis by city, product category, and region.
- Top-performing city rankings.
- Year-wise sales analysis.
- Natural-language question answering for supported question patterns.
- Filtering sales by city and product category.
- Interactive charts and tables.
- Explanations of the calculations behind answers.
- Handling of unsupported questions.

## Dataset
- Dataset: Sample Superstore Sales
- Source: Tableau Public – Sample Data
- Format: CSV
- Records: 10,194
- Columns: 21

The dataset contains information about orders, customers, locations, product categories, sales, quantities, discounts, and profits.

## Technologies Used
- Python
- Pandas
- Streamlit
- Plotly

## Project Structure
```text
GriidAi/
├── data/
│   └── superstore.csv
├── app.py
├── analysis.py
├── test_cases.py
├── requirements.txt
└── README.md
```

## Installation and Setup

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

4. Run the application:

```bash
python -m streamlit run app.py
```

5. Open the local URL displayed in the terminal.

## Example Questions
- Which city has the highest sales?
- Which category has the highest sales?
- Which region has the highest sales?
- Show top 5 cities by sales.
- Compare sales by category.
- Which year had the highest sales?
- Show sales in Seattle.
- Show sales for Technology.

## Validation and Testing
Four test cases were executed:

| Test | Description                   | Result |
|------|-------------------------------|--------|
| 1    | Highest sales city            | PASS   |
| 2    | Sales filtering by city       | PASS   |
| 3    | Sales filtering by category   | PASS   |
| 4    | Unsupported question handling | PASS   |

All four test cases passed.

## Limitations
- The question-answering system supports predefined natural-language patterns rather than unrestricted conversations.
- Customer satisfaction and other metrics not present in the dataset cannot be analyzed.
- Results depend on the accuracy and completeness of the source dataset.
- Follow-up questions are supported only for selected question patterns.

## AI Tool Usage
AI assistance was used during development for understanding requirements, debugging, improving code, and documenting the project. The current question-answering workflow uses rule-based Python logic and does not connect to an external large language model.

## Future Improvements
- Integrate a free or locally hosted language model.
- Support more flexible natural-language questions.
- Add additional filters and visualizations.
- Include map-based sales analysis.

## Author
Developed as part of the GriidAi Internship Assignment.
