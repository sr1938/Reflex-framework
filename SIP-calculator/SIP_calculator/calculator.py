# calculator.py
import locale

# Set the locale to Indian for currency formatting
locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')

def calculate(form_data: dict):
    sip = int(form_data['sip_amount'])
    years = int(form_data['tenure'])
    rate = int(form_data['AGR'])
    print("Rs", sip, ";", years, "Yr", ";", rate, "%")
    monthly_rate = rate / 12 / 100
    total_months = years * 12
    future_Val = sip * (((1 + monthly_rate) ** total_months - 1) / monthly_rate) * (1 + monthly_rate)
    investment_amount = sip * total_months
    returns_over_period = future_Val - investment_amount
    returns_over_period = round(returns_over_period, 2)
    data01 = [{"name":"Investment", "value": investment_amount},
              {"name":"Returns", "value": returns_over_period}]

    # Format the future value in Indian currency format
    future_value = locale.format_string("%0.2f", future_Val, grouping=True)
    invested = locale.format_string("%0.2f", investment_amount, grouping=True)
    returns = locale.format_string("%0.2f", returns_over_period, grouping=True)

    return future_value, invested, returns, data01
