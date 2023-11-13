from netmiko import ConnectHandler # Importa a classe ConnectHandler do módulo netmiko
# Cria a classe CiscoConnect
class CiscoConnect:
    def __init__(self,type,ip,username,password):
        self.type = type
        self.ip = ip
        self.username = username
        self.password = password
        self.device = None
        self.__connect()
    # Method to connect to the remote host
    def __connect(self):
        try:
            self.device = ConnectHandler(device_type=self.type,
                                         host=self.ip,
                                         username=self.username,
                                         password=self.password)
        except Exception as error:
            print('Error: {}'.format(error))
            return None
    #Method to disconnect from the remote host
    def disconnect(self):
        self.device.disconnect()
    #Method to execute one command on the remote host
    def exec_command(self,command):
        if self.device is None:
            self.device = self.__connect()
        output = self.device.send_command(command)
        return output
    #Method to execute multiple commands on the remote host
    def config_command(self,command):
        if self.device is None:
            self.device = self.__connect()
        output = self.device.send_config_set(command)
        return output
    #Method to save the configuration on the remote host
    def save_config(self):
        if self.device is None:
            self.device = self.__connect()
        output = self.device.save_config()
        return output
    


  