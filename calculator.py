def interface():
    print("My Program")
    while(True):
        print("Options:")
        print("1 - HDL")
        print("2 - LDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()
        elif choice == '2':
            LDL_driver()


def HDL_driver():
    # Get input
    hdl = get_HDL_input()
    # check if hdl is normal
    result = check_hdl_range(hdl)
    # output results
    output_hdl_results(result)


def LDL_driver():
    # Get input
    ldl = get_LDL_input()
    # check if ldl is normal
    result = check_ldl_range(ldl)
    # output results
    output_ldl_results(result)


def get_HDL_input():
    HDL_input = input("Enter your HDL result: ")
    return int(HDL_input)


def check_hdl_range(hdl):
    if(hdl >= 60):
        return "Normal"
    elif(hdl >= 40):
        return "Borderline Low"
    else:
        return "Low"


def output_hdl_results(result):
    print("Your HDL level is " + result)


def get_LDL_input():
    LDL_input = input("Enter your LDL result: ")
    return int(LDL_input)


def check_ldl_range(ldl):
    if(ldl < 200):
        return "Normal"
    elif(ldl < 240):
        return "Borderline High"
    else:
        return "High"


def output_ldl_results(result):
    print("Your LDL level is " + result)


interface()
