import matplotlib.pyplot as plt
# Read the CSV data
data = '''date,transaction,transaction type,value
1/10/24,catering order,income,$500
1/11/24,new dough mixer,expense,($200)
1/11/24,sampling platters,income,$250
1/12/24,flour order,expense,($100)
1/12/24,wedding catering,income,$600
1/13/24,party order,income,$300
1/15/24,flour order,expense,($100)
1/16/24,specialty flour order,expense,($500)
1/18/24,specialty cake,income,$400
'''

# Convert the CSV data to a DataFrame
from io import StringIO
df = pd.read_csv(StringIO(data), parse_dates=['date'])

# Clean the 'value' column and convert it to numeric
df['value'] = df['value'].replace('[$,()]', '', regex=True).astype(float)
df.loc[df['transaction type'] == 'expense', 'value'] *= -1

# Plot the transactions over time
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['value'].cumsum(), marker='o', linestyle='-')
plt.title('Cumulative Transactions Over Time')
plt.xlabel('Date')
plt.ylabel('Balance')
plt.grid(True)
plt.savefig('transactions.png')
plt.show()

# Calculate gross income, net income, and total expenses
gross_income = df[df['transaction type'] == 'income']['value'].sum()
net_income = df['value'].sum()
total_expenses = df[df['transaction type'] == 'expense']['value'].sum()

print(f"Gross Income: ${gross_income}")
print(f"Net Income: ${net_income}")
print(f"Total Expenses: ${total_expenses}")

# Suggestions for saving money
# Analyze the frequency and type of expenses
expenses = df[df['transaction type'] == 'expense']
common_expenses = expenses.groupby('transaction')['value'].sum().sort_values()

print("\nSuggestions to Save Money:")
if common_expenses.empty:
    print("No expenses to analyze.")
else:
    # Suggest negotiating better deals on the most common expenses
    print(f"Consider negotiating better prices or seeking alternative suppliers for your most common expenses: {common_expenses.index[-1]}.")

    # Suggest bulk purchasing or alternative solutions for high-cost items
    if 'specialty flour order' in common_expenses.index:
        print("You may save money by purchasing specialty flour in bulk or considering alternative suppliers.")

# Additional analysis can be done here based on the data
                          