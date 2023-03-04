from gui import *

class gui():
    def __init__(self):
        self.window=window
        self.canvas=canvas
        self.button_image_hover_con=button_image_hover_con
        self.button_image_hover_dis=button_image_hover_dis
        self.button_image_2=button_image_2
        self.button_image_1=button_image_1
        pass
    
    def initialize(self):
        #adding button event handler
        #button_1.bind("<Button-1>", self.button_clicked)
        pass
        
    def get_username(self):
        return entry_1.get()
    
    def get_password(self):
        return entry_2.get()
    
    def update_message(self,msg):
        canvas.itemconfig(message, text=msg)
    
    def update_status(self,status_msg):
        canvas.itemconfig(status, text=status_msg)
    
    def disp_connecting(self):
        self.update_message("connecting ....")
        
        
    def disp_disconnecting(self):
        self.update_message("disconnecting ....")
        
    def disp_loading(self):
        self.update_message("loading ....")

    def disp_initializing(self):
        self.update_message("initializing ....")
        
    def disp_initializing_complete(self):
        self.update_message("initilization complete")
        canvas.after(300,self.update_message,"")
        
    def disp_status_connected(self):
        self.update_status("Connected")
        canvas.itemconfig(status, fill="green")
    
    def disp_status_disconnected(self):
        self.update_status("Disconnected")
        canvas.itemconfig(status, fill="red")
    
    def disp_network_disconnected(self):
        self.update_status("Network disconnected")
        canvas.itemconfig(status, fill="white")

    def button_make_connect(self):
        button_1.config(image=button_image_1)
        
    def button_make_disconnect(self):
        button_1.config(image=button_image_2)
    
    def update_ip(self,ip):
        canvas.itemconfig(ip_, text=ip)
            
    def start(self):
        window.resizable(False, False)
        window.mainloop()