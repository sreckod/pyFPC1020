import FPC1020.fingerFPC as fp
import time

from FPC1020 import FPCconstants

f = fp.FingerFpc()

while True:
    print("============== Menu ================")
    print("Add a New User ----------------- 1")
    print("Fingerprint Matching --------------- 2")
    print("Get User Number and Print All User ID ------ 3 ")
    print("Delete Assigned User --------- 4")
    print("Delete All User ---------- 5")
    print("============== End =================")

    i = raw_input()
    if i == '1': # Fingerprint Input and Add a New User
        u_id = raw_input("Please input the new user ID (0 ~ 99).")
        response = f.enroll(int(u_id))

        if response['success']:
            print("Success, your User ID is: " + str(response['result']))
        else:
            if response['error'] == FPCconstants.ACK_USER_EXIST:
                print("Failed, this User ID already exists.")
            elif response['error'] == FPCconstants.ACK_USER_OCCUPIED:
                print("Failed, this fingerprint already exists.")
            else:
                print("Failed, please try again.")

        time.sleep(2)

    elif i == '2': # Fingerprint Matching
        print("Match Fingerprint, please put your finger on the Sensor.")
        response = f.search()

        if response['success']:
            print("Success, your User ID is: "+ str(response['result']))
        else:
            print("Failed, please try again.")

        time.sleep(1)
    elif i == '3': # Print user IDs
        response = f.print_user_id()
        if response['success']:
            print("Number of Fingerprint User is: "+ response['result'])
        else:
            print("Print User ID Fail!")

    elif i == '4': # Delete Assigned User ID
        u_id = raw_input("Please input the user ID(0 ~ 99) you want to delete.")
        response = f.delete(u_id)

        if response['success']:
            print("Delete Fingerprint User Success!")
        else:
            print("Delete Fingerprint User Fail!")

    elif i == '5': # Delete All User ID
        delete = raw_input("Delete All Users, Y/N ?")

        if delete == 'y' or delete == 'Y':
            response = f.clear()

            if response['success']:
                print("Delete All Fingerprint User Success!")
            else:
                print("Delete All Fingerprint User Fail!")

    else:
        break