import locale

def set_locale():
    try:
        # Try to set the locale to Indian for currency formatting
        locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
    except locale.Error:
        # Fallback to a default locale if 'en_IN.UTF-8' is not available
        print("Locale 'en_IN.UTF-8' not available. Falling back to default locale.")
        locale.setlocale(locale.LC_ALL, 'C')

def calculate(form_data: dict):
    # Ensure locale is set correctly
    set_locale()

    # Extract and convert form data
    sip = int(form_data['sip_amount'])
    years = int(form_data['tenure'])
    rate = int(form_data['AGR'])
    print(f"Rs {sip}; {years} Yr; {rate} %")

    # Perform calculations
    monthly_rate = rate / 12 / 100
    total_months = years * 12

    # Initialize yearly breakdown
    dataarea01 = []

    # Calculate future value, investment, and returns year by year
    cumulative_investment = 0
    future_value = 0

    for year in range(1, years + 1):
        months = year * 12
        cumulative_investment = sip * months
        future_value = sip * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
        returns_over_period = future_value - cumulative_investment
        
        # Round and format values
        returns_over_period = round(returns_over_period, 2)
        future_value = round(future_value, 2)
        # Append yearly data to breakdown
        dataarea01.append({
            "year": year,
            "future value": future_value,
            "investment": cumulative_investment,
            "returns": returns_over_period
        })

    # Calculate total future value and returns over the entire period
    total_future_value = locale.format_string("%0.2f", future_value, grouping=True)
    total_investment = locale.format_string("%0.2f", sip * total_months, grouping=True)
    total_returns = locale.format_string("%0.2f", future_value - sip * total_months, grouping=True)

    # Data for area chart
    datapie01 = [
        {"name": "Investment", "value": sip * total_months,"percent": round(((cumulative_investment/future_value)*100),2)},
        {"name": "Returns", "value": round(future_value - sip * total_months, 2),"percent": round(((returns_over_period/future_value)*100),2)}
    ]

    return total_future_value, total_investment, total_returns, dataarea01, datapie01


