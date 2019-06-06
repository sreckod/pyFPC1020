import serial, time

from FPC1020 import FPCconstants, helpers

head = [0xef01, 0xffffffff, 0x01]

rBuf = []

class FingerFpc:
    __serial = None

    __loop = True

    # raspberry pi 3 port /dev/serial0
    def __init__(self, port = '/dev/serial0', baud_rate = 19200):
        """
        Constructor
        @param string port
        @param integer baud_rate
        """

        if baud_rate < 9600 or baud_rate > 115200 or baud_rate % 9600 != 0:
            raise ValueError('The given baudrate is invalid!')

        ## Initialize PySerial connection
        self.__serial = serial.Serial(port = port, baudrate = baud_rate, bytesize = serial.EIGHTBITS, timeout = 2)

        if self.__serial.isOpen():
            self.__serial.close()

        self.__serial.open()


    def __del__(self):
        """
        Destructor
        """

        ## Close connection if still established
        if self.__serial is not None and self.__serial.isOpen() == True:
            self.__serial.close()


    def __send_command(self, command, u_id = None):

        packet = helpers.format_command_packet(command, u_id)
        request = [FPCconstants.DATA_START]  # command head
        request.extend(packet)
        request.append(self.__generate_checksum(packet))  # Generate checkout data
        request.append(FPCconstants.DATA_END)

        self.__serial.write(request)
        self.__serial.flush()


    # checksum
    @staticmethod
    def __generate_checksum(data):
        temp = 0

        for i in range(len(data)):
            temp ^= data[i]

        return temp


    # get response
    def __get_response(self, cmd):
        response = {
            'success': False,
            'error': None,
            'result': None
        }

        packet = self.__wait_for_data()
        if not packet: return response  # wait response info

        return helpers.format_response_packet(packet, cmd)

    def __wait_for_data(self):

        packet = []

        try:
            while True:
                wait = self.__serial.inWaiting()
                #if not self.__serial.isOpen(): break

                if wait >= 8:
                    response = self.__serial.read(8)
                    sd = bytearray(response)
                    packet.extend(sd)

                    return packet

                time.sleep(0.05)
        except TypeError as e:
            return False


    #enrolling steps
    def enroll_step_1(self, u_id):
        self.__send_command(FPCconstants.CMD_ENROLL1, u_id)
        return self.__get_response(FPCconstants.CMD_ENROLL1)


    def enroll_step_2(self, u_id):
        self.__send_command(FPCconstants.CMD_ENROLL2, u_id)
        return self.__get_response(FPCconstants.CMD_ENROLL2)


    def enroll_step_3(self, u_id):
        self.__send_command(FPCconstants.CMD_ENROLL3, u_id)
        return self.__get_response(FPCconstants.CMD_ENROLL3)


    # Add a new user
    def enroll(self, u_id):
        response = self.enroll_step_1(u_id)
        if not response['success'] == True: return response
        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger second time...')
        response = self.enroll_step_2(u_id)
        if not response['success'] == True: return response
        print('Remove finger...')
        time.sleep(2)

        print('Waiting for same finger third time...')
        response = self.enroll_step_3(u_id)
        if not response['success'] == True: return response
        print('Remove finger...')
        time.sleep(2)

        response['result'] = u_id

        return response


    # Fingerprint identify 1:N
    def search(self):
        self.__send_command(FPCconstants.CMD_SEARCH)
        return self.__get_response(FPCconstants.CMD_SEARCH)


    # Fingerprint identify 1:1
    def identify(self, u_id):
        self.__send_command(FPCconstants.CMD_IDENTIFY, u_id)
        self.__get_response(FPCconstants.CMD_IDENTIFY)


    # Delete assigned user
    def delete(self, u_id):
        self.__send_command(FPCconstants.CMD_DELETE, u_id)
        return self.__get_response(FPCconstants.CMD_DELETE)


    # Delete assigned user
    def clear(self):
        self.__send_command(FPCconstants.CMD_CLEAR)
        return self.__get_response(FPCconstants.CMD_CLEAR)


    # Get enroll user count
    def get_enroll_count(self):
        self.__send_command(FPCconstants.CMD_USER_COUNT)
        return self.__get_response(FPCconstants.CMD_USER_COUNT)


    # Get user ID number unsigned char
    def print_user_id(self):
        self.__send_command(FPCconstants.CMD_USER_ID)
        return self.__get_response(FPCconstants.CMD_USER_ID)


    def close(self):
        if self.__serial.isOpen():
            self.__serial.close()