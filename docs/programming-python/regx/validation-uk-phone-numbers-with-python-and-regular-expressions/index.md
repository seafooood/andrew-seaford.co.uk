---
title: "Validation UK Phone Numbers With Python and Regular Expressions"
date: 2025-02-02
categories:
  - "prog"
keywords: [python, regex, validation, phone-numbers, uk]
---

To validate phone numbers, we need to consider the common formats for UK phone numbers. Generally, UK phone numbers have the following characteristics:

Landline numbers typically start with '01', '02', '03', or '084', followed by 9 or 10 digits. Mobile numbers start with '07' and are followed by 9 digits. We'll use regular expressions (regex) to match these patterns. Let's write the function and the unit tests.

## Phone Number Validation Function

```python
import re

def is_valid_uk_phone_number(phone_number: str) -> bool:
    # Define the regex pattern for UK phone numbers allowing spaces
    pattern = re.compile(r'^(?:0|\+?44)\s?(\d\s?){9,10}$')
    return bool(pattern.match(phone_number))
```

## Unit Tests

```python
import unittest
from UKPhoneNumberValidation import *

class TestUKPhoneNumberValidation(unittest.TestCase):

    def test_valid_landline_numbers(self):
        self.assertTrue(is_valid_uk_phone_number("01234567890"))
        self.assertTrue(is_valid_uk_phone_number("020 7946 0123"))
        self.assertTrue(is_valid_uk_phone_number("02079460123"))
        self.assertTrue(is_valid_uk_phone_number("+44 1234 567890"))
        self.assertTrue(is_valid_uk_phone_number("+441234567890"))
        self.assertTrue(is_valid_uk_phone_number("01625 611979"))

    def test_valid_mobile_numbers(self):
        self.assertTrue(is_valid_uk_phone_number("07123456789"))
        self.assertTrue(is_valid_uk_phone_number("07 123 456 789"))
        self.assertTrue(is_valid_uk_phone_number("+44 7123 456789"))
        self.assertTrue(is_valid_uk_phone_number("+447123456789"))

    def test_invalid_phone_numbers(self):
        self.assertFalse(is_valid_uk_phone_number("1234567890"))  # Missing leading zero or +44
        self.assertFalse(is_valid_uk_phone_number("07890 1234567"))  # Too many digits
        self.assertFalse(is_valid_uk_phone_number("07890 1234"))  # Too few digits
        self.assertFalse(is_valid_uk_phone_number("0800 123 45"))  # Too few digits for landline

    def test_non_numeric_characters(self):
        self.assertFalse(is_valid_uk_phone_number("07a23456789"))  # Alphabetic character
        self.assertFalse(is_valid_uk_phone_number("07-23456789"))  # Hyphen

if __name__ == "__main__":
    unittest.main()

```


## Related Files

-   [https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/regx/validation-uk-phone-numbers-with-python-and-regular-expressions](https://github.com/seafooood/andrew-seaford.co.uk/tree/main/docs/programming-python/regx/validation-uk-phone-numbers-with-python-and-regular-expressions)
