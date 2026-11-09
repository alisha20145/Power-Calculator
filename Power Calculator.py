# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
base=int(input("Enter the base number: "))
exponent=int(input("Enter the exponent: "))



# ---------- PART 2: the running total ----------
result=1



# ---------- PART 3 + 4: the loop that multiplies ----------
for i in range(1, exponent + 1):
    result=result * base
    print("I am on step", i, "and the result is now",result)


# ---------- PART 5: the answer ----------
print("The result of", base, "to the power of", exponent, "is", result)