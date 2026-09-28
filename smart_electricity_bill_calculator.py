SERVICE_CHARGE = 100.0


def get_customer_details():
    """Ask for customer information and return it after validation."""
    customer_name = input("Enter customer name: ").strip()
    while not customer_name:
        print("Customer name cannot be empty.")
        customer_name = input("Enter customer name: ").strip()

    customer_id = input("Enter customer ID: ").strip()
    while not customer_id:
        print("Customer ID cannot be empty.")
        customer_id = input("Enter customer ID: ").strip()

    while True:
        try:
            units = float(input("Enter electricity units consumed: "))
            if units < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units
        except ValueError:
            print("Please enter a valid number of units.")


def calculate_bill(units):
    """Return the energy charge, service charge, and final bill amount."""
    if units <= 100:
        rate_per_unit = 2.0
    elif units <= 200:
        rate_per_unit = 4.0
    elif units <= 500:
        rate_per_unit = 6.0
    else:
        rate_per_unit = 8.0

    energy_charge = units * rate_per_unit
    final_amount = energy_charge + SERVICE_CHARGE
    return energy_charge, SERVICE_CHARGE, final_amount


def display_bill(customer_name, customer_id, units, energy_charge,
                 service_charge, final_amount):
    """Print a formatted electricity bill."""
    print("\n" + "=" * 42)
    print("           ELECTRICITY BILL")
    print("=" * 42)
    print(f"Customer name       : {customer_name}")
    print(f"Customer ID         : {customer_id}")
    print(f"Units consumed      : {units:.2f}")
    print("-" * 42)
    print(f"Energy charge       : Rs. {energy_charge:.2f}")
    print(f"Service charge      : Rs. {service_charge:.2f}")
    print("-" * 42)
    print(f"Final bill amount   : Rs. {final_amount:.2f}")
    print("=" * 42)


def main():
    customer_name, customer_id, units = get_customer_details()
    energy_charge, service_charge, final_amount = calculate_bill(units)
    display_bill(customer_name, customer_id, units, energy_charge,
                 service_charge, final_amount)


if __name__ == "__main__":
    main()