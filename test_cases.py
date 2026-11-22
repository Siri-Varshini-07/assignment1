
from analysis import load_data, answer_question

# Load the dataset
df = load_data()

# Define test cases
test_cases = [
    {
        "question": "Which city has the highest sales?",
        "expected": "New York City has the highest sales, with total sales of 256,368.16."
    },
    {
        "question": "Show sales in Seattle",
        "expected": "Total sales in Seattle are 119,540.74."
    },
    {
        "question": "Show sales for Technology",
        "expected": "Total sales for Technology are 839,893.28."
    },
    {
        "question": "What is the customer satisfaction score?",
        "expected": "I'm unable to answer that question yet.\n\n"
                    "You can try questions like:\n"
                    "1. Which city has the highest sales?\n"
                    "2. Which category has the highest sales?\n"
                    "3. Which region has the highest sales?\n"
                    "4. Show top 5 cities by sales.\n"
                    "5. Compare sales by category.\n"
                    "6. Which year had the highest sales?\n\n"
                    "Please try rephrasing your question."
    }
]

print("===== VALIDATION TEST RESULTS =====")

for i, test in enumerate(test_cases, start=1):

    actual = answer_question(df, test["question"])

    passed = actual == test["expected"]

    print(f"\nTest Case {i}")
    print("Question:", test["question"])
    print("Expected:", test["expected"])
    print("Actual:", actual)
    print("Status:", "PASS" if passed else "FAIL")
