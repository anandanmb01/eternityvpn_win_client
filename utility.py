import subprocess
from gui import *

connection_status=False
##########################################################
def update_status(status_msg):
    canvas.itemconfig(status, text=status_msg)
    
########################################
def update_message(msg):
    canvas.itemconfig(message, text=msg)

############################################################

def exec(command):
    try:
        # Execute the command on PowerShell and capture its output
        result = subprocess.check_output(['powershell', '-Command', command], stderr=subprocess.STDOUT)

        # Decode the result bytes to a string
        output = result.decode('utf-8').strip()
        
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
        
        

class vpn():
    def __init__(self):
        pass
    
    def create_profile(self):
        res=exec('Get-NetAdapter -Name "My VPN" -IncludeHidden')
        if res[-1]:
            exec('Add-VpnConnection -Name "My VPN" -ServerAddress "eternityvpn.ddns.net" -TunnelType L2tp -EncryptionLevel Optional -L2tpPsk "eternitykey" -AuthenticationMethod PAP -RememberCredential -SplitTunneling -PassThru -Force')
        else:
            pass
        
    def connect(self):
        res=exec('rasdial "My VPN" "admin" "anandan@01"')
        if res[-1]:
            update_message("Invalid credentials")
        else:
            update_message("")
            update_status("Connected")
            canvas.itemconfig(status, fill="green")
            connection_status=True
            button_1.config(image=button_image_2)
            update_message("")
            
            
    def disconnect(self):
        exec('rasdial "My VPN" /disconnect')
        update_message("")
        update_status("Disconnected")
        canvas.itemconfig(status, fill="red")
        button_1.config(image=button_image_1)
        




#############################################
vpn=vpn()
# vpn.create_profile()


def btn_click(event):
    
    if not connection_status:
        username=entry_1.get()
        password=entry_2.get()
        if username=="":
            update_message("Enter username")
        elif "_eternity" not in username :
                update_message("Invalid username")
        elif password=="":  
            update_message("Enter password")
            
        else:
            update_message("")
            update_message("connecting....")
            vpn.connect()

            
            
        # canvas.itemconfig(message, text="New text")
        # entry_2.place_forget()
        # canvas.itemconfig(entry_bg_2, state="hidden")

        print("button clicked")
    
    else:
        vpn.disconnect()
        

def button_clicked(event):
    print("Button clicked")
    button_1.config(image=button_image_2)
    

button_1.bind("<Button-1>", btn_click)



window.resizable(False, False)
window.mainloop()
