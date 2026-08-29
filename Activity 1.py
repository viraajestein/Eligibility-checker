print("Welcome to the eligibilyt checker for the Coding University!")

medical_condition = str(input("\nDo you have a medical condition? (Y/N): ")).strip().upper()

if medical_condition == "Y":
    print("\nCongrats! You are eligible.")
else:
    atten = input("\nSorry, you were not eligible that way so could you please tell us your attendence in percentile: ")

    if atten >= "75":
        print("\nCongrats! You are eligible.")
    else:
        print("\nSorry! You are not eligible, try next time. Good Luck!")

print("\nThank you for using this prorgram!")