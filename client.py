#client
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import StringVar


host = '127.0.0.1'
port = 1027
name = None
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



def enter_name():
    global name
    name = name_entry.get()
    if name:
        client.send(name.encode('ascii'))
        join_btn.grid(row=0, column=0)
        name_entry.config(state=tk.DISABLED)
        name_btn.config(state=tk.DISABLED)
        refresh_online.config(state=tk.NORMAL)
    
def join_chat():
    print("You joined the chat")
    join = '/JOIN'
    client.send(join.encode('ascii'))
    
    chat_window.config(state=tk.NORMAL)  # Enable editing
    chat_window.delete('1.0', tk.END)  # Delete all old messages
    chat_window.config(state=tk.DISABLED)

    chat_window.grid(row=1, column=0, sticky=tk.NSEW)
    text_box.grid(row=0, column=0)
    sendbtn.grid(row=0, column=1)
    leavebtn.grid(row=0, column=2)
    exit_btn.config(state=tk.DISABLED)
    join_btn.grid_forget()

    
    threading.Thread(target=listen_server, args=(client, )).start()


def sendmsg():
    message = text_box.get()
    if message:
        client.send(message.encode('ascii'))
        text_box.delete(0, len(message))
        #print("sendmsg() called")
    #else

def addmsg(message):
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, message+'\n')
    chat_window.config(state=tk.DISABLED)
    #print("addmsg() called")

def listen_server(client):
    while True:
        message = client.recv(1024).decode('ascii')
        
        if message:
            addmsg(message)
        #else
        
def leavechat():
    response = messagebox.askyesno("Leave Chat", "Are you sure you want to leave the chat?")
    if response is True:
        message = '/LEAVE'
        client.send(message.encode('ascii'))
        print("you left the chat")
        
        chat_window.grid_forget()
        text_box.grid_forget()
        sendbtn.grid_forget()
        leavebtn.grid_forget()
        join_btn.grid(row=0, column=0)
        exit_btn.config(state=tk.NORMAL)
        
def exit():
    global name
    response = messagebox.askyesno("Exit Program", "Are you sure you want to exit the program?")
    if response is True:
        if name:  # If a name has been entered, inform the server
            client.send('/EXIT'.encode('ascii'))
            
        try:
            client.close()  # Close the connection unconditionally
        except Exception as e:
            print(f"Error closing socket: {e}")
        root.destroy()
        print("You disconnected")
        
def refresh():
    message = '/COUNT'
    client.send(message.encode('ascii'))
    count = client.recv(1024).decode('ascii')
    print(f'{count} received')
    if count:
        online_count.delete("1.0", "end")
        online_count.insert("1.0", count)





root = tk.Tk()
root.geometry("600x600")
root.title("Chat Room")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)

topframe = tk.Frame(root, width=600, height=100)
topframe.grid(row=0, column=0, sticky=tk.NSEW)
midframe = tk.Frame(root, width=600, height=100)
midframe.grid(row=1, column=0, sticky=tk.NSEW)
btmframe = tk.Frame(root, width=600, height=100)
btmframe.grid(row=2, column=0, sticky=tk.NSEW)
midframe.grid(row=1, column=0, sticky=tk.NSEW)
btmframe.grid(row=2, column=0, sticky=tk.NSEW)

client.connect((host, port))

#top frame elements
lbl1 = tk.Label(topframe, text="Connected to server")
lbl1.grid(row=0, column=0)
print("Connected to the server")
lbl3 = tk.Label(topframe, text="People online in chat: ")
lbl3.grid(row=0, column=1)
online_count = tk.Text(topframe, width=3, height=1)
online_count.grid(row=0, column=2)
refresh_online = tk.Button(topframe, text="Refresh", command=refresh, state=tk.DISABLED)
refresh_online.grid(row=0, column=3)

lbl2 = tk.Label(topframe, text="Enter your name: ")
lbl2.grid(row=1, column=0)
name_entry = tk.Entry(topframe, width=15)
name_entry.grid(row=1, column=1)
name_btn = tk.Button(topframe, text="Enter", command=enter_name)
name_btn.grid(row=1, column=2)
exit_btn = tk.Button(topframe, text="Exit Program", command=exit)
exit_btn.grid(row=1, column=3)


#mid frame element
chat_window = scrolledtext.ScrolledText(midframe, width=70, height= 30)
chat_window.config(state=tk.DISABLED)
join_btn = tk.Button(midframe, text="Join Chat", command=join_chat)

#bottom frame elements
text_box = tk.Entry(btmframe, width=40)
sendbtn = tk.Button(btmframe, text="Send", command=sendmsg)
leavebtn = tk.Button(btmframe, text="Leave Chat", command=leavechat)


def main():
    root.mainloop()
if __name__ == '__main__':
    main()
    



