class Synchronization:
    """"""

    MAX_CONNECTIONS = 10
    WRITE_FLAG = False

    def __init__(self, action):
        """"""

        if action != "threads" or action != "processes":
            print("invalid action")
        else:
            self.action = action


    







    def new_client(self, clients_num, client_socket, max_con=MAX_CONNECTIONS, write_flag=WRITE_FLAG):
        """handles new client entry and permissions given
        if no permission given, returns false"""
        if clients_num >= max_con:
            return False
        elif not write_flag:
            return "writing permission given"
        else: return True