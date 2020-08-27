# Logical operators - and, or, not

has_high_income = False
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income:
    print("Eligible for Loan")
# the above uses a logical "and" operator which returns true only when both the operands are true
# i.e "Eligible for Loan" will be printed only when both
# "has_high_income" and "has_good_credit" are true.

if has_high_income or has_good_credit:
    print("Eligible for Loan")
# The above is the logical "or" operator which returns true when atleast one of the operands is true.

if has_good_credit and not has_criminal_record:
    print("Eligible for Loan")
# the logical "not" operator is just like "!" in Java or Kotlin.
# the "not" operator reverses any boolean value.
