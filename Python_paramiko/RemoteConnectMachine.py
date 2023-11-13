
from paramiko import SSHClient,AutoAddPolicy,AuthenticationException,SCPClient,SCPException #import the SSHClient,AutoAddPolicy,AuthenticationException,SCPClient,SCPException classes from the paramiko module


class RemoteConnect:
    #constructor for the class 
    def __init__(self,host):
        self.host = host
        self.client = None
        self.scp = None
        self.__connect()
    
    #private method to connect to the remote host
    def __connect(self):
        try:
            self.client = SSHClient()   #create a new SSHClient object
            self.client.load_system_host_keys() #load the system host keys
            self.client.set_missing_host_key_policy(AutoAddPolicy()) #set the policy to auto add the host key
            self.client.connect(hostname=self.host, 
                                username=USERNAME, 
                                key_filename=KEY) #connect to the host
            self.scp = SCPClient(self.client.get_transport()) #create a new SCPClient object
        except AuthenticationException as error:
            print('Authentication Failed: Please check your network/ssh key')
        finally:
            return self.client
    #scp is a file transfer protocol that uses ssh for data transfer not like sftp which uses ftp for data transfer
    
    #public method to disconnect from the remote host    
    def disconnect(self):
        self.client.close()
        self.scp.close()
    
    #public method to execute a command on the remote host
    def exec_command(self,command):
        if self.client is None:
            self.client == self.__connect()
        stdin,stdout,stderr = self.client.exec_command(command)
        status = stdout.channel.recv_exit_status()
        if status is 0:
            return stdout.read()
        else:
            return None
        
    #public method to transfer a file to the remote host           
    def transfer(self,file,remotepath):
        try:
            if self.client is None:
                self.client = self.__connect()
            self.scp.put(file,
                         remotepath,
                         recursive=True)
        except SCPException as error:
            print('SCPException: Failed transferring data')