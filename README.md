
# Shopping Discount Calculator

A Python program that calculates shopping discounts, savings, and final purchase prices based on spending thresholds.

## Features

- Accepts a shopping subtotal.
- Applies a discount based on the subtotal.
- Calculates the discount amount.
- Calculates the final price after discount.
- Displays the results clearly.

## Discount Rules

The example rules are:

| Shopping Subtotal | Discount |
|---|---|
| 100,000 or more | 10% |
| 50,000–99,999.99 | 5% |
| Below 50,000 | No discount |

## Requirements

- Python 3

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Run the program:

   `python discount.py`

5. Enter the shopping subtotal.

## Example

Input:

`Subtotal: 120000`

Expected result:

- Discount rate: 10%
- Money saved: 12,000
- Final price: 108,000

*Example amounts use generic currency units.*

## Skills Demonstrated

- Variables and data types
- User input and type conversion
- Arithmetic operations
- Comparison operators
- Conditional statements
- Formatted output

## Future Improvements

- Validate negative and non-numeric amounts.
- Support multiple shopping items.
- Display a detailed receipt.
- Allow configurable discount rules.

## License

This project is licensed under the MIT License.
