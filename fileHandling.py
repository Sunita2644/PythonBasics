results = {
    101:"PASS",
    102:"FAIL",
    103:"Pass"
}

try:
    with open("results.txt","w") as f:
        for case_id, status in results.items():
            f.write(f"Test Case {case_id}-{status}\n")
except Exception as e:
    print(e)
finally:
    f.close()

try:
    with open("results.txt","r") as f:
        print("reading file data")
        data=f.read()
        print(data)
except Exception as e:
    print(e)
finally:
    f.close()