#example 1
try:
    with open("testData.txt", 'r') as file:
        data=file.read()
        print(data)
except Exception as e:
    print(e)
finally:
    print("test data loaded")


#example 2
test_cases = {101:"login test",
              102:"logout test"}
def run_test_case(case_id):
    try:
        print(f"test case details:{case_id}-{test_cases[case_id]}")
    except Exception as e:
        print(f"Keyerror",e)
    finally:
        print("checked")

run_test_case(101)
run_test_case(103)