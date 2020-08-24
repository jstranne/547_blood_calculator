def interface():
    print("My Program")
    while(True):
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_driver()


def HDL_driver():
	# Get input
	hdl = get_HDL_input()
	# check if hdl is normal
	result = check_hdl_range(hdl)
	# output results
	output_hdl_results(result)
	# check if Low


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


interface()
