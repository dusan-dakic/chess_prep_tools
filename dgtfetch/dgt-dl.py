"""
Shows UI interface for game(s) download 

 DGT tournament boards are used at chess tournaments around the world to show the games live as they happen, games may be available on 
 https://view.livechesscloud.com/ but pgn is not easy to download 

 DGT = https://digitalgametechnology.com/

 """

#from tkinter import *
import os
import tkinter as tk
from tkinter import filedialog
from idlelib.tooltip import Hovertip

from dgtfetch.dgtdownload import GameFetcher

#DEMO_LINK = "https://view.livechesscloud.com/#d19960e4-e61b-40d7-a6a5-3d7cd68eb66a"  # Begonia Open 2024 ")
DEMO_LINK ="#82e80ab2-2798-430a-8d40-7b7444f03b1d"      # Edwin Malitis 
LIVECHESSURL="https://view.livechesscloud.com/"


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGT Game Downloader App")
        self.root.geometry("700x300+10+20")
        self.folder=os.getcwd()+"\\games"

        urllbl = tk.Label(root, text="LiveChess URL: ")             # , bg="light green"
        urlTip = Hovertip(urllbl,'Insert whole web link or just #id (#xxxnnxxn-nnnn-nnnx-nxnn-nxnnnnxnnxnx)')

        filterbynamelbl = tk.Label(root, text="Filter by Name :")   # , bg="light green"
        savelbl = tk.Label(root, text="Saving to PGN ...")          # , bg="light green"
        folderlbl = tk.Label(root, text="Output folder ...", bg="light green")
        
        seldirbtn= tk.Button(text="Browse", command=self.browse_button)

        urllbl.grid(row=0, column=0,ipadx=10, ipady=10)
        seldirbtn.grid(row=4, column=2,ipadx=5, ipady=5)

        # Create an Entry widget
        self.livechessURL = tk.Entry(root, width=70, bg="green", fg="white", font=('Arial', 11, 'bold'))
        self.livechessURL.insert(0, DEMO_LINK)            
        self.livechessURL.grid(row=0, column=1)
        #self.livechessURL.pack(pady=10)

        # create a Form label
        #heading = tk.Label(root, text="Form", bg="light green")

        self.all2pgn = tk.IntVar()
        self.saveOption = tk.Checkbutton(root, text='Tournament: All games to single PGN, file name will be <tournament_name>.pgn', 
            variable=self.all2pgn,
            onvalue=1 , offvalue=0,
            justify="left")
        
        self.name_field = tk.Entry(root,justify="left")
        self.folder_field = tk.Entry(root,justify="left", width=50, bg="yellow" )

        self.folder_field.insert(0, self.folder)
        
        
        filterbynamelbl.grid(row=1, column=0)
        savelbl.grid(row=2, column=0)

        self.saveOption.grid(row=2, column=1, sticky="W", padx=10, pady=10)
        self.name_field.grid(row=1, column=1,  sticky="W", padx=10, pady=10)
        self.folder_field.grid(row=4, column=1,  sticky="W", padx=10, pady=10)
        
        folderlbl.grid(row=4, column=0)

        # Create a Button widget
        self.btnDownload = tk.Button(root, text="Start download", command=self.start_download)
        self.btnDownload.grid(row=5, column=1, ipadx="100")

        self.lbl_message1 = tk.Label(root, text="Enter #ID or full URL pointing to LiveChess ...")
        self.lbl_progress = tk.Label(root, text="___")
        self.lbl_message1.grid(row=6, column=1, ipadx="100")
        
        #https://view.livechesscloud.com/

    def start_download(self):
        #just_id=False

        user_input = self.livechessURL.get()
        
        if user_input.startswith(LIVECHESSURL): 
            self.lbl_message1.config(text=f"You entered URL: {user_input}")

        elif user_input:
            #just_id=True
            user_input=LIVECHESSURL +user_input
            self.lbl_message1.config(text=f"You entered ID: {user_input}")
        else:
            self.lbl_progress = tk.Label(root, text="___")
            return
        
        if  self.all2pgn==1:
             one_pgn = False
        else:
             one_pgn = True 

        filter = self.name_field.get()
        fetcher = GameFetcher()
        if filter:
            fetcher.filterbyname=filter
        else:    
            fetcher.filterbyname=None
        
        folder=self.folder_field.get()
        fetcher.runextract(url_or_id_to_fetch=user_input, folder=folder, one_pgn_for_all=one_pgn)

        print(len(fetcher.games_list))
        print(fetcher.games_list)
    #-- end start download 
    def browse_button(self):
        # Allow user to select a directory and store it in global var
        # called folder_path
        self.folder = filedialog.askdirectory()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()