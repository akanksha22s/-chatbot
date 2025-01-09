print("Welcome to the Sales Measurement and Forecasting System!")
print("I can help you save sales data, analyze it, and provide simple sales forecasts.")

# Step 1: Collect sales data from the user
sales_data = []
while True:
    user_input = input("Enter sales data (or type 'done' to finish): ").strip()
    if user_input.lower() == "done":
        break
    try:
        sales = float(user_input)
        if sales < 0:
            print("Sales cannot be negative. Please try again.")
        else:
            sales_data.append(sales)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if sales data is available
if not sales_data:
    print("No data entered. Exiting.")
else:
    # Step 2: Save the sales data to a CSV file
    file_name = input("Enter the full file path to save the CSV (e.g., C:\\Users\\YourName\\sales_data.csv): ").strip()
    try:
        with open(file_name, "w") as file:
            for sales in sales_data:
                file.write(f"{sales}\n")
        print(f"CSV file has been created successfully at: {file_name}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
    
    # Step 3: Generate a simple sales forecast
    print("\nAnalyzing sales data to predict future trends...")
    total_sales = sum(sales_data)
    num_entries = len(sales_data)
    average_sales = total_sales / num_entries

    print(f"Your average sales so far are: {average_sales:.2f}")
    print(f"Based on current trends, your predicted sales for the next 5 periods are:")

    # Generate predictions (basic trend forecasting)
    forecast = []
    for i in range(1, 6):
        next_sales = average_sales * (1 + (0.05 * i))  # 5% growth per period
        forecast.append(next_sales)
        print(f"Period {i}: {next_sales:.2f}")
    
    # Step 4: Chatbot for Queries
    print("\nYou can now ask me about your sales data or forecasts!")
    print("Type 'current' to see your current sales data, 'forecast' for future predictions, or 'exit' to quit.")
    
    while True:
        query = input("\nEnter your query: ").strip().lower()
        if query == "current":
            print(f"Your current sales data: {sales_data}")
        elif query == "forecast":
            print(f"Future predictions: {forecast}")
        elif query == "exit":
            print("Thank you for using the Sales Measurement and Forecasting System. Goodbye!")
            break
        else:
            print("Invalid query. Please type 'current', 'forecast', or 'exit'.")
