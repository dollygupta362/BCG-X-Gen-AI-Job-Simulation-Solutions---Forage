# financial_chatbot.py

import pandas as pd

# Dataset (from Task 1)
data = {
    "Company": ["Microsoft","Microsoft","Microsoft","Tesla","Tesla","Tesla","Apple","Apple","Apple"],
    "Fiscal Year": [2024,2023,2022,2024,2023,2022,2024,2023,2022],
    "Total Revenue ($)": [245122,211915,198270,97690,96773,81462,391035,383285,394328],
    "Net Income ($)": [88136,72361,72738,7153,14974,12587,93736,96995,99803],
    "Total Assets ($)": [512163,411976,364840,122070,106618,82338,364980,352583,352755],
    "Total Liabilities ($)": [243686,205753,198298,48390,43009,36440,308030,290437,302083],
    "Cash Flow from Operating Activities ($)": [118548,87582,89035,14923,13256,14724,118254,110543,122151],
    "Revenue Growth (%)": [0, -13.55, -6.44, 0, -0.94, -15.82, 0, -1.98, 2.88],
    "Net Income Growth (%)": [0, -17.90, 0.52, 0, 109.34, -15.94, 0, 3.48, 2.89]
}
df = pd.DataFrame(data)

# Predefined queries and responses
responses = {
    "Show the total revenue trend": 
        f"📊 Total Revenue Trend (2022–2024):\n{df.pivot(index='Fiscal Year', columns='Company', values='Total Revenue ($)')}",

    "Show the net income trend": 
        f"📈 Net Income Trend (2022–2024):\n{df.pivot(index='Fiscal Year', columns='Company', values='Net Income ($)')}",

    "Compare assets and liabilities": 
        f"🏦 Average Assets vs Liabilities (2022–2024):\n{df.groupby('Company')[['Total Assets ($)','Total Liabilities ($)']].mean().round(2).to_string()}",

    "Show the operating cash flow": 
        f"💵 Average Operating Cash Flow (2022–2024):\n{df.groupby('Company')['Cash Flow from Operating Activities ($)'].mean().round(2).to_string()}",

    "Show revenue and net income growth": 
        f"🚀 Average Growth (2022–2024):\n{df.groupby('Company')[['Revenue Growth (%)','Net Income Growth (%)']].mean().round(2).to_string()}"
}

def simple_chatbot(user_query):
    # Match the query with predefined responses
    return responses.get(user_query, "❌ Sorry, I can only answer the predefined queries listed.")

# Command-line interaction
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot!")
    print("You can ask predefined queries like:")
    for q in responses.keys():
        print(" -", q)
    
    while True:
        user_input = input("\nEnter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Thank you for using the Financial Chatbot. Goodbye!")
            break
        response = simple_chatbot(user_input)
        print(response)