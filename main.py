from sys_utl import sys
from gui_al import gui
from gui import button_1
import time
import threading
import requests
import json

ip_check_url = "https://api64.ipify.org?format=json"
# ip_check_url = "https://ipinfo.io/json"
network_status=True
ref_ip_enable=True
counters=None

sys=sys()
gui=gui()

def get_counter(raw_data):
    counter_data=raw_data[0][2:]
    for n,d in enumerate(counter_data):
        #n%3 == 0 counter
        #n%3 == 1 value

        if n%3 == 1:
            if(int(d)>0):
                counter_ref=counter_data[n-1].split(' :')[0].split('\\bytes transmitted')[0]
                rec_speed=counter_ref+"\\Bytes Received/sec"
                trans_speed=counter_ref+"\\Bytes Transmitted/Sec"
                return [trans_speed.strip(),rec_speed.strip()]
        
def get_val_from_counter(counter):
    try:
        return float(sys.exec(f'Get-Counter -Counter "{counter}"')[0][-1].strip())
    except:
        return 0.00
        
def convert_data_speed(data_speed):
    if data_speed < 1024:
        return str(round(float(data_speed), 2)) + ' B/s'
    elif data_speed < 1048576:
        return '{:.2f} KB/s'.format(data_speed/1024)
    elif data_speed < 1073741824:
        return '{:.2f} MB/s'.format(data_speed/1048576)
    else:
        return '{:.2f} GB/s'.format(data_speed/1073741824)

    
def gui_initial_update():
    global t4
    global counters
    if sys.connection_status:
        #connected
        gui.button_make_disconnect()
        gui.disp_status_connected()
        ######### update usage
        if counters==None:
            raw=sys.exec("Get-Counter -Counter '\RAS Port(*)\Bytes Transmitted'")
            counters=get_counter(raw)
            
            if t4.is_alive():
                pass
            else:
                t4 = threading.Thread(target=update_speed, daemon=True)
                t4.start()
        
    else:
        #not connected
        gui.button_make_connect()
        gui.disp_status_disconnected()
        ######### update usage

def create_vpn_profile():
    gui.disp_initializing()
    res=sys.exec('Get-VpnConnection -Name "eternity_vpn" ') #check if vpn exist
    if res[-1]:
        #vpn doesnot exist
        res_=sys.exec('Add-VpnConnection -Name "eternity_vpn" -ServerAddress "eternityvpn.ddns.net" -TunnelType L2TP -L2tpPsk "eternitykey" -Force -EncryptionLevel Optional -AuthenticationMethod MSChapv2 -UseWinlogonCredential -RememberCredential –PassThru')
        if(res_[-1]):
            #error occured
            gui.update_message("initilization error")
        else:
            gui.disp_initializing_complete()
            sys.connection_status=False
            
    else:
        #vpn present
        #check if profile is same
        if 'eternityvpn.ddns.net' in res[0][1] :
            #same profile
            gui.disp_initializing_complete()
            if "Connected" in res[0][10]:
                sys.connection_status=True
            
        else:
            res0=sys.exec('Remove-VpnConnection -Name "eternity_vpn" -Force -PassThru')
            if res0[-1]:
                #removing error
                gui.update_message("initilization error")
            else:
                #removing sucessfull
                res1=sys.exec('Add-VpnConnection -Name "eternity_vpn" -ServerAddress "eternityvpn.ddns.net" -TunnelType L2tp -EncryptionLevel Optional -L2tpPsk "eternitykey" -AuthenticationMethod PAP -RememberCredential -PassThru -Force')
                if(res1[-1]):
                    #error occured
                    gui.update_message("initilization error")
                else:
                    gui.disp_initializing_complete()
                    sys.connection_status=False
                    
    #Vpn profile sucefully created
    gui_initial_update()
    gui.update_ip(get_ip())
    

def get_ip():
    global network_status
    try:
        ip = json.loads(requests.get(ip_check_url).text)['ip']
    
        if not network_status:  #handles newrok disconneted status display
            network_status=True
            gui_initial_update()
        
        return ip
            
    except :
        network_status=False
        if gui.canvas:
            try:
                sys.connection_status=False
                gui_initial_update()
                gui.canvas.after(0,gui.disp_network_disconnected)
            except:
                pass
        return('_._._._')

    ##### data usage update
    
        


def refresh_ip():
    global ref_ip_enable
    while True:
        time.sleep(5)
        if ref_ip_enable:
            ip=get_ip()
            gui.window.after(0, gui.update_ip,ip)
        else:
            break
        
def update_speed():
    global counters
    global ref_ip_enable
    while True:
        time.sleep(1)
        if (counters != None) and (ref_ip_enable):
            uplink=convert_data_speed(get_val_from_counter(counters[0]))
            downlink=convert_data_speed(get_val_from_counter(counters[1]))
            gui.window.after(0,gui.update_traffic(uplink, downlink))
        else:
            break
        
def button_clicked():
    global t4
    global counters
    gui.update_message("")
    if sys.connection_status:
        #connected
        gui.disp_disconnecting()
        res4=sys.exec('rasdial "eternity_vpn" /disconnect')
        if(res4[-1]):
            gui.update_message("Error occured")
            gui.canvas.after(500,gui.update_message,"")
        else:
            #diconnnected sucess
            gui.update_message("Disconnected sucessfully")
            gui.canvas.after(500,gui.update_message,"")
            sys.connection_status=False
            gui.disp_status_disconnected()
            gui.button_make_connect()
            ##USAGE####
    else:
        #Not connected
        username=gui.get_username()
        password=gui.get_password()
        if username=="":
            gui.update_message("Enter username")
        elif "_eternity" not in username :
            gui.update_message("Invalid username")
        elif password=="":  
            gui.update_message("Enter password")
        else:
            gui.canvas.after(0,gui.update_message,"")
            gui.canvas.after(0,gui.disp_connecting)
            res3=sys.exec(f'rasdial "eternity_vpn" "{username}" "{password}"')
            if res3[-1]:
                #wrong credential
                sys.connection_status=False
                gui.disp_status_disconnected()
                gui.update_message("Invalid credentials")
                gui.canvas.after(500,gui.update_message,"")
            else:
                #connection sucessful
                sys.connection_status=True
                gui.button_make_disconnect()
                gui.disp_status_connected()
                gui.update_message("Connection sucessful")
                gui.canvas.after(500,gui.update_message,"")
                #####displ usage#######
    ip=get_ip()
    gui.canvas.after(0,gui.update_ip,ip)
    
    if counters==None:
        raw=sys.exec("Get-Counter -Counter '\RAS Port(*)\Bytes Transmitted'")
        counters=get_counter(raw)
        if t4.is_alive():
            pass
        else:
            t4 = threading.Thread(target=update_speed, daemon=True)
            t4.start()


def btn_exec(event):
    threading.Thread(target=button_clicked).start()
    
def on_enter(event):
    if sys.connection_status:
        button_1.config(image=gui.button_image_hover_dis)
        
    else:
        button_1.config(image=gui.button_image_hover_con)

def on_leave(event):
    if sys.connection_status:
        button_1.config(image=gui.button_image_2)
        
    else:
        button_1.config(image=gui.button_image_1)

    
button_1.bind("<Enter>", on_enter)
button_1.bind("<Leave>", on_leave)


gui.initialize()
button_1.bind("<Button-1>",btn_exec)

t1 = threading.Thread(target=create_vpn_profile, daemon=True)
t2 = threading.Thread(target=refresh_ip, daemon=True)
t4 = threading.Thread(target=update_speed, daemon=True)

def shudown():
    global ref_ip_enable
    global t4
    global t2
    ref_ip_enable=False
    gui.window.destroy()

    # if t2.is_alive():
    #     t2.join()
    # if t4.is_alive():
    #     t4.join()
    
    
        
    
t1.start()
t2.start()
t4.start()

gui.window.protocol("WM_DELETE_WINDOW",shudown)
gui.start()

