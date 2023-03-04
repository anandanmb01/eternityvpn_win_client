import subprocess

class sys():
    def __init__(self):
        self.connection_status=False
        
    def exec(self,command):
        try:
            # Execute the command on PowerShell and capture its output
            process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
            output, error = process.communicate()
    
            # Decode the result bytes to a string
            output = output.decode('utf-8').strip()
    
            # Print the output
            if '\r\n' in output:
                return([output.split('\r\n'),False])
            else:
                return([output.split('\n'),False])
    
        except subprocess.CalledProcessError as error:
            # An error occurred while executing the command
            output = error.output.decode('utf-8').strip()
            # Print the error output
            if '\r\n' in output:
                return([output.split('\r\n'),True])
            else:
                return([output.split('\n'),True])
    