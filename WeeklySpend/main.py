import pandas as pd
import random

# Set the number of users
num_users = 1000

# Generate user IDs
user_ids = list(range(1, num_users + 1))

# Generate random weekly spend values between 100 and 4000
weekly_spend = [random.randint(100, 4000) for _ in range(num_users)]

# Create a DataFrame
data = {'User ID': user_ids, 'Weekly Spend': weekly_spend}
df = pd.DataFrame(data)

# Create an Excel file
excel_file = 'user_weekly_spend.xlsx'
df.to_excel(excel_file, index=False)

print(f'Excel file "{excel_file}" created successfully.')
