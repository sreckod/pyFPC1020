import time
from FPC1020 import FPCconstants


def format_command_packet(command, u_id = None):
    request = []
    cmd = FPCconstants.commands[command]

    if command == 'Enroll1':  # Add fingerprint 1st
        request = [cmd, u_id >> 8, u_id & 0xff, 1, 0x00]
    elif command == 'Enroll2':  # Add fingerprint 2nd
        request = [cmd, u_id >> 8, u_id & 0xff, 1, 0x00]
    elif command == 'Enroll3':  # Add fingerprint 3rd
        request = [cmd, u_id >> 8, u_id & 0xff, 1, 0x00]
    elif command == 'Delete':  # Delete assigned user
        request = [cmd, u_id >> 8, u_id & 0xff, 0x00, 0x00]
    elif command == 'Clear':  # Delete all users
        request = [cmd, 0x00, 0x00, 0x00, 0x00]
    elif command == 'UserCount':  # Get number of users
        request = [cmd, 0x00, 0x00, 0x00, 0x00]
    elif command == 'Identify':  # Fingerprint matching 1:1
        request = [cmd, u_id >> 8, u_id & 0xff, 0x00, 0x00]
    elif command == 'Search':  # Fingerprint matching 1:N
        request = [cmd, 0x00, 0x00, 0x00, 0x00]
    elif command == 'UserID':
        request = [cmd, 0x00, 0x00, 0x00, 0x00]

    return request

def format_response_packet(packet, cmd):
    response = {
        'success': False,
        'error': None,
        'result': None
    }

    if cmd == FPCconstants.CMD_ENROLL1 or cmd == FPCconstants.CMD_ENROLL2 or cmd == FPCconstants.CMD_ENROLL3:
        if FPCconstants.ACK_SUCCESS == packet[4]:
            response['success'] = True
        elif FPCconstants.ACK_USER_EXIST == packet[4]:
            response['error'] = FPCconstants.ACK_USER_EXIST
            time.sleep(0.5)
        elif FPCconstants.ACK_USER_OCCUPIED == packet[4]:
            response['error'] = FPCconstants.ACK_USER_OCCUPIED
            time.sleep(0.5)

    # 1:N comparison
    elif cmd == FPCconstants.CMD_SEARCH:
        if (1 == packet[4]) or (2 == packet[4]) or (3 == packet[4]):
            response['success'] = True
            response['result'] = packet[3]

    # delete assigned user
    # delete all users
    # 1:1 comparison
    elif cmd == FPCconstants.CMD_DELETE or cmd == FPCconstants.CMD_CLEAR or cmd == FPCconstants.CMD_IDENTIFY:
        if FPCconstants.ACK_SUCCESS == packet[4]:
            response['success'] = True

    # get enroll user count
    # Get user ID
    elif cmd == FPCconstants.CMD_USER_COUNT or cmd == FPCconstants.CMD_USER_ID:
        if FPCconstants.ACK_SUCCESS == packet[4]:
            response['success'] = True
            response['result'] = packet[3]

    return response