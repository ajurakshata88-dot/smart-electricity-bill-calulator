# smart-electricity-bill-calulator

## Smart Electricity Bill Calculator

A beginner-friendly Python console program that collects customer details and
electricity usage, calculates a bill, and prints a formatted receipt. It uses
only Python's built-in features; no database, files, APIs, external libraries,
or classes are required.

## Program flow

1. `main()` calls `get_customer_details()` to collect the customer name, ID,
	and units consumed.
2. The program checks that the name and ID are not empty. It converts units to
	a number, rejects invalid input, and asks again if units are negative.
3. `calculate_bill(units)` chooses one rate based on the total units consumed:
	- 0-100 units: Rs. 2 per unit
	- 101-200 units: Rs. 4 per unit
	- 201-500 units: Rs. 6 per unit
	- More than 500 units: Rs. 8 per unit
4. The energy charge is the total units multiplied by the selected rate. A
	fixed service charge of Rs. 100 is added to get the final bill amount.
5. `display_bill()` prints the customer details, units, energy charge, service
	charge, and final amount.

The selected rate applies to **all units consumed** (a flat rate based on the
total-use band), rather than charging each band progressively.

## Run the program

```bash
python smart_electricity_bill_calculator.py
```