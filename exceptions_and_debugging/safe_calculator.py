"""
## 1. Safe Calculator with try / except  *(Easy)*

=================================================
SAFE CALCULATOR
=================================================

Problem Statement:
Write a Python FUNCTION called `safe_divide`
that takes two values from the user and
performs a division, but never crashes the
program.

Handle the following error cases gracefully:
   - non-numeric input        -> ValueError
   - division by zero         -> ZeroDivisionError
   - any other unexpected bug -> generic Exception

The function must always return a TUPLE:
        (status, value_or_message)
   - status -> "ok" or "error"
   - value_or_message -> the result on success,
                         or an error string on
                         failure.

-------------------------------------------------
Debugging Skills to Practice:
- Read the FULL traceback. The last line of a
  traceback names the exception class — match
  it to your `except`.
- Use a temporary print(type(a), type(b))
  before the division to confirm the inputs.
- Insert breakpoint() and step through with
  the Python debugger (pdb) commands:
       n  -> next line
       s  -> step into
       p  -> print a variable
       q  -> quit

-------------------------------------------------
Input Example 1:
safe_divide("10", "2")

Output Example 1:
('ok', 5.0)
Calculation finished

-------------------------------------------------
Input Example 2:
safe_divide("10", "0")

Output Example 2:
('error', 'Cannot divide by zero')
Calculation finished

-------------------------------------------------
Input Example 3:
safe_divide("ten", "2")

Output Example 3:
('error', 'Inputs must be numbers')
Calculation finished
=================================================
def safe_divide(a, b):
    """
    Safely divides two numbers, handling common errors.

    Args:
        a (str): First number as a string.
        b (str): Second number as a string.

    Returns:
        tuple: (status, value_or_message)
            status: "ok" or "error"
            value_or_message: result (float) on success, error message on failure.
    """
    try:
        # Convert inputs to float – may raise ValueError
        num_a = float(a)
        num_b = float(b)

        # Perform division – may raise ZeroDivisionError
        result = num_a / num_b

        # If we reach here, success
        return ("ok", result)

    except ValueError:
        # Non‑numeric input
        return ("error", "Inputs must be numbers")

    except ZeroDivisionError:
        # Division by zero
        return ("error", "Cannot divide by zero")

    except Exception as e:
        # Any other unexpected error – capture its message
        return ("error", str(e))


# ========== DRIVER CODE (for demonstration) ==========
if __name__ == "__main__":
    # Example 1
    print(safe_divide("10", "2"))
    print("Calculation finished")

    # Example 2
    print(safe_divide("10", "0"))
    print("Calculation finished")

    # Example 3
    print(safe_divide("ten", "2"))
    print("Calculation finished")
"""
