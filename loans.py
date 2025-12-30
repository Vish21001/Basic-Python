has_good_credit = True
has_criminal_record = True 

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

if has_good_credit and has_criminal_record:
    print("Not eligible for loan due to criminal record")
