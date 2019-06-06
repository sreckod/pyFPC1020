# Constants

DATA_START = 0xf5  # Data start
DATA_END   = 0xf5  # Data end


CMD_ENROLL1     = 'Enroll1'     # Add fingerprint 1st
CMD_ENROLL2     = 'Enroll2'     # Add fingerprint 2nd
CMD_ENROLL3     = 'Enroll3'     # Add fingerprint 3rd
CMD_DELETE      = 'Delete'      # Delete assigned user
CMD_CLEAR       = 'Clear'       # Delete all users
CMD_USER_COUNT  = 'UserCount'   # Get number of users
CMD_IDENTIFY    = 'Identify'    # Fingerprint matching 1:1
CMD_SEARCH      = 'Search'      # Fingerprint matching 1:N
CMD_USER_ID     = 'UserID'      # Get User ID and User Permission

commands = {
    'Enroll1':      0x01,  # Add fingerprint 1st
    'Enroll2':      0x02,  # Add fingerprint 2nd
    'Enroll3':      0x03,  # Add fingerprint 3rd
    'Delete':       0x04,  # Delete assigned user
    'Clear':        0x05,  # Delete all users
    'UserCount':    0x09,  # Get user count
    'Identify':     0x0b,  # Fingerprint matching 1:1
    'Search':       0x0c,  # Fingerprint matching 1:N
    'UserID':       0x2b   # Get User ID and User Permission
}

ACK_SUCCESS         = 0x00  # Operate success
ACK_FAIL            = 0x01  # Operate filed
ACK_FULL            = 0x04  # Fingerprint database is full
ACK_NO_USER         = 0x05  # User do not exist
ACK_USER_OCCUPIED   = 0x06  # User ID already exists
ACK_USER_EXIST      = 0x07  # Fingerprint already exists
ACK_TIMEOUT         = 0x08  # Acquisition timeout