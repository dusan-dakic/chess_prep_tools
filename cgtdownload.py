from tkinter import *
import tkinter as tk


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CGT Game Downloader App")
        self.root.geometry("700x200+10+20")

        urllbl = tk.Label(root, text="LiveChess URL: ")             # , bg="light green"
        filterbynamelbl = tk.Label(root, text="Filter by Name :")   # , bg="light green"
        savelbl = tk.Label(root, text="Saving to PGN ...")          # , bg="light green"
        folderlbl = tk.Label(root, text="Output folder ...", bg="light green")

        urllbl.grid(row=0, column=0)
        # Create an Entry widget
        self.livechessURL = tk.Entry(root, width=70, bg="green", fg="white", font=('Arial', 11, 'bold'))
        self.livechessURL.insert(0, "https://view.livechesscloud.com/#d19960e4-e61b-40d7-a6a5-3d7cd68eb66a")             # Begonia Open 2024 ")
        self.livechessURL.grid(row=0, column=1)
        #self.livechessURL.pack(pady=10)

        # create a Form label
        #heading = tk.Label(root, text="Form", bg="light green")


        self.all2pgn = IntVar()
        self.saveOption = tk.Checkbutton(root, text='All games to single PGN', 
            variable=self.all2pgn,
            onvalue=1 , offvalue=0,
            justify="left")
        
        self.name_field = tk.Entry(root,justify="left")
        self.folder_field = tk.Entry(root,justify="left", width=50, bg="yellow" )
        self.folder_field.insert(0, os.getcwd())
        
        
        filterbynamelbl.grid(row=1, column=0)
        savelbl.grid(row=2, column=0)
        self.saveOption.grid(row=2, column=1, sticky="W")
        self.name_field.grid(row=1, column=1,  sticky="W")
        self.folder_field.grid(row=4, column=1,  sticky="W")
        
        folderlbl.grid(row=4, column=0)

        # Create a Button widget
        self.btnDownload = tk.Button(root, text="Start download", command=self.start_download)
        self.btnDownload.grid(row=5, column=1, ipadx="100")

        self.lbl_message1 = tk.Label(root, text="Enter URL pointing to LiveChess ...")
        self.lbl_progress = tk.Label(root, text="___")
        self.lbl_message1.grid(row=6, column=1, ipadx="100")


    def start_download(self):
        user_input = self.livechessURL.get()
        if user_input:
            self.lbl_message1.config(text=f"You entered: {user_input}")
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
        
        fetcher.runextract(url_to_process=user_input, one_pgn_for_all=one_pgn)
        print(len(fetcher.games_list))
        print(fetcher.games_list)
    #-- end start download 

import os
import requests
import sys 
import datetime 
__version__="0.4"
__author__ = 'Dusan Dakic'
__date__ = 'Jun 2024'
__copyright__ = '(C) 2024, Dusan Dakic'

class GameFetcher:
    def __init__(self, db=None, log=None, app=None):
        #TODO read config, set external database, logging    
        #self.debug = app.configData["JobClient"]["DEBUG"]
        self.games_list=[]

        now = datetime.datetime.now()
        print("Download pgn from LiveChess URL v{}".format(__version__))
        print("Start: {}".format(now))

    def fetch_games(self, url, combined):
        self.runextract(self, url_to_process=url, one_pgn_for_all = True)

    def runextract(self, url_to_process, one_pgn_for_all = False):
        #-- added filter by name, so extra work required 
        matchesFound=0 

        if type(url_to_process) is list:
            baseURL = url_to_process[0].replace("view.", "1.pool.")
        elif type(url_to_process)== str:
            baseURL = url_to_process.replace("view.", "1.pool.")

        baseURL = baseURL.replace(".com/#", ".com/get/")
        
        requestTournament = baseURL +"/tournament.json"

        tournament = requests.get(requestTournament) 

        jsonT = tournament.json()
        if one_pgn_for_all:
            tourpgn = jsonT['name'] +".pgn"
            complete_set=""

        # lists of rounds and cgt boards 
        turnir_rounds = jsonT['rounds']
        cgt_boards = jsonT['eboards']

        round_idx=0
        for round_item in jsonT['rounds']:
            round_idx+=1

            if round_item['count'] >0:
                pairings = self.get_round_pairs(baseURL, round_idx)
                # pairings_count= len(pairings)
                # print('pairings_count=', pairings_count)
                pairno=0
                for game_pair in pairings['pairings']:
                    pairno+=1
                    white_player= game_pair["white"]
                    black_player= game_pair["black"]
                    
                    white = "{} {},{} {}".format(white_player["title"], white_player["fname"],white_player["mname"],white_player["lname"])
                    black = "{} {},{} {}".format(black_player["title"], black_player["fname"],black_player["mname"],black_player["lname"])
                    white=white.replace("None ", "")
                    black=black.replace("None ", "")

                    game_result=game_pair["result"]
                    pgnfilename = white+ "-vs-"+ black + " [Round-{}_Board-{}].pgn".format(round_idx,pairno)
                    
                    self.games_list.append({"white":white, "black":black, "result":game_result})

                    #-- if filter by player name is set ...  
                    if self.filterbyname:
                        if white.find(self.filterbyname) > -1 or black.find(self.filterbyname) > -1:
                            #-- we got a match 
                            matchesFound+=1 
                        else:
                            print("SKIP: ", pgnfilename)
                            continue      
                    #---
                    #-- get game header details and get game moves 
                    round_number=round_idx
                    round_board=pairno
                    
                    ePGN = self.get_round_game(baseURL, round_number, round_board )
                    plycount = len(ePGN["moves"])
                    pgnmoves = self.make_pgn(ePGN)
                    pgnmoves += game_result+ os.linesep

                    pgn_head = self.make_pgn_header(white=white, black=black, result=game_result, tournament=jsonT, plycount=plycount)

                    full_pgn = pgn_head + pgnmoves
                    if one_pgn_for_all:
                        complete_set = complete_set+ full_pgn+"\n"
                        print(pgnfilename.replace(".pgn", ""))
                    else:     
                        pgnmoves = self.save_to_pgn(pgnfilename, full_pgn)
        if one_pgn_for_all:
            self.save_to_pgn(tourpgn,complete_set)
        #-- END OF runextract
        print('Done : {}'.format(datetime.datetime.now()))

    def get_round_pairs(self, url, round):
        request_matches = url+'/round-{}/index.json'.format(round)
        round_matches = requests.get(request_matches).json() 
        return round_matches

    def get_round_game(self, baseURL, round_number, round_board ):
        gameURL = baseURL+ "/round-{}/game-{}.json?poll".format(round_number, round_board)
        round_game = requests.get(gameURL).json() 
        return round_game

    def make_pgn(self, ePGN_moves):
        move_pgn = ""
        ply_counter=0
        move_counter=0
        line_len=0

        for move in ePGN_moves["moves"]:
            move_text = move.split()[0]
            line_len+=len(move_text)

            ply_counter+=1
            if ply_counter % 2 == 1:
                move_counter+=1
                move_pgn = move_pgn+"{}. ".format(move_counter)

                #-- try to nicely format moves into multiple lines 
                if line_len > 51:
                    move_pgn+='\n'
                    line_len=0
                move_pgn = move_pgn+move_text+" "
            else:
                move_pgn = move_pgn+move_text+" "    
        return move_pgn

    def save_to_pgn(self, filename, ePGN_moves):
        with open(filename, "w",encoding='utf-8') as text_file:
            text_file.write(ePGN_moves)
        print('Saved: ',filename)

    def make_pgn_header(self, white, black, result, tournament=None, round=None, plycount=0):
        # TODO: lines commented out :) 
        header = '[ePGN "0.1;DGT LiveChess/2.2.5"]' + '\n'
        if tournament:
            header = header + '[Event "{}"]'.format(tournament['name']) + '\n'
            header = header + '[Site "{}, {}"]'.format(tournament['location'], tournament['country']) + '\n'

        if round:
            #header = header + '[Date "2023.05.28"]
            pass
        #header = header + '[Round "2.10"]

        header = header + '[White "{}"]'.format(white) + '\n'
        header = header + '[Black "{}"]'.format(black) + '\n'
        header = header + '[Result "{}"]'.format(result) + '\n'
        header = header + '[TimeControl "90 minutes +30 seconds increment"]' + '\n'
        #header = header + '[WhiteFideId "3456789"]
        #header = header + '[BlackFideId "3210000"]
        #header = header + '[WhiteElo "1700"]
        #header = header + '[BlackElo "1800"]
        header = header + '[Termination "normal"]' + '\n'
        header = header + '[PlyCount "{}"]'.format(plycount) + '\n'
        return header + '\n'


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()