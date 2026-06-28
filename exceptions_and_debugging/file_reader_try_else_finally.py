"""
## 4. File Reader with try / except / else / finally  *(Medium)*

=================================================
FILE READER WITH FULL TRY BLOCK
=================================================

Problem Statement:
Write a Python FUNCTION called `read_numbers`
that reads a text file containing ONE number
per line and returns the SUM of those numbers.

The function must demonstrate ALL FOUR parts
of Python's exception model:
        try / except / else / finally.

Error cases to handle:
   - FileNotFoundError  -> file path is wrong
   - PermissionError    -> file cannot be read
   - ValueError         -> a line is not a number
   - any other Exception

The function returns a TUPLE:
        (status, value_or_message, lines_read)
   - status            -> "ok" or "error"
   - value_or_message  -> the total sum or
                          the error message
   - lines_read        -> number of lines
                          successfully parsed
                          before any error.

-------------------------------------------------
Instructions:
1. Define:
      def read_numbers(path):
2. Layout the try block as follows:
      try:
          open the file
          read lines and convert each to float
      except FileNotFoundError:
          ...
      except PermissionError:
          ...
      except ValueError:
          ...
      except Exception as e:
          ...
      else:
          this block ONLY runs if no exception
          was raised. Use it for the success
          path (e.g. compute the final sum).
      finally:
          this block ALWAYS runs. Use it to
          close the file if it was opened, or
          to print "Done reading".
3. Use a `with open(path) as f:` block, which
   already closes the file automatically.
4. Do NOT use:
   - bare `except:`
   - `os.path.exists()` to AVOID the
     FileNotFoundError. Let the exception be
     raised and handle it.

-------------------------------------------------
Debugging Skills to Practice:
- The four-part structure makes the intent of
  each block obvious:
        try     -> code that might fail
        except  -> what to do when it fails
        else    -> what to do when it does NOT fail
        finally -> cleanup that runs no matter what
- When the program behaves oddly, ask "which
  block is actually running?". Add a quick
  `print("entered else")` etc. to find out.
- For file errors, print `path` and
  `os.getcwd()` to confirm where Python is
  looking.

-------------------------------------------------
Input Example 1:
A file numbers.txt containing:
   10
   20
   30

read_numbers("numbers.txt")

Output Example 1:
('ok', 60.0, 3)
Done reading

-------------------------------------------------
Input Example 2:
read_numbers("missing.txt")

Output Example 2:
('error', 'File not found: missing.txt', 0)
Done reading

-------------------------------------------------
Input Example 3:
A file bad.txt containing:
   10
   abc
   30

read_numbers("bad.txt")

Output Example 3:
('error', 'Invalid number on a line', 1)
Done reading

-------------------------------------------------
Explanation:
- In example 1 every line parses, the `else`
  block computes the sum 60.0, and `finally`
  prints "Done reading".
- In example 2 the file does not exist; the
  FileNotFoundError branch runs, then
  `finally` still prints "Done reading".
- In example 3 the first line parses fine
  (lines_read becomes 1), then "abc" raises
  ValueError, which is caught and reported.
=================================================
def read_numbers(path):
    """
    Reads a text file containing one number per line and returns the sum.

    Demonstrates try / except / else / finally.

    Args:
        path (str): Path to the file.

    Returns:
        tuple: (status, value_or_message, lines_read)
            status: "ok" or "error"
            value_or_message: sum (float) on success, error message on error
            lines_read: number of lines successfully parsed before any error
    """
    lines_read = 0
    total = 0.0

    try:
        # ---- try block: code that might fail ----
        with open(path, 'r') as f:
            for line in f:
                # Convert line to float; raises ValueError if invalid.
                num = float(line.strip())
                total += num
                lines_read += 1

    # ---- except blocks: handle specific exceptions ----
    except FileNotFoundError:
        return ('error', f'File not found: {path}', 0)

    except PermissionError:
        return ('error', f'Permission denied: {path}', 0)

    except ValueError:
        # lines_read holds the count of lines parsed successfully before the error.
        return ('error', 'Invalid number on a line', lines_read)

    except Exception as e:
        # Catch any other unexpected exception.
        return ('error', str(e), lines_read)

    else:
        # ---- else block: runs only if no exception was raised ----
        # All lines were parsed successfully; return the sum.
        return ('ok', total, lines_read)

    finally:
        # ---- finally block: always runs ----
        print("Done reading")
"""
