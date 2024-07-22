"""
 DGT tournament boards are used at chess tournaments around the world to show the games live as they happen, games may be available on 
 https://view.livechesscloud.com/ but pgn is not easy to download 

 DGT = https://digitalgametechnology.com/

"""

import os
import requests
import sys 
import datetime

from FIDEinfo import getFIDEinfo 
#from FIDEinfo.getFIDEinfo import *
#from FIDEinfo.getFIDEinfo import getFIDEinfo

__version__="0.4"
__author__ = 'Dusan Dakic'
__date__ = 'Jun 2024'
__copyright__ = '(C) 2024, Dusan Dakic'
LIVECHESSURL="https://view.livechesscloud.com/"


class GameFetcher:
    def __init__(self, db=None, log=None, app=None):
        #TODO read config, set external database, logging    
        #self.debug = app.configData["JobClient"]["DEBUG"]
        self.games_list=[]
        self.homefolder = ""
        now = datetime.datetime.now()
        print("Download pgn from LiveChess URL v{}".format(__version__))
        print("Start: {}".format(now))

    def fetch_games(self, url, combined):
        self.runextract(self, url_to_process=url, one_pgn_for_all = True)

    def is_valid_url(self, url:str):
        #TODO check URL 
        return True
           


    def runextract(self, url_or_id_to_fetch:str, folder:str, one_pgn_for_all:bool = False, ):
        """_summary_

        Args:
            url_to_fetch (str): _description_
            id_to_fetch (str, optional): _description_. Defaults to None.
            one_pgn_for_all (bool, optional): _description_. Defaults to False.
        """

        #-- undecided whether to force folder name on user or not? 
        if one_pgn_for_all:
            self.homefolder = folder +'/tournaments/'
        else:
            # .\games\all_games\2024 Victorian Open
            self.homefolder = folder +'/all_games/2024 Edwin Malitis Major/'

        if not os.path.isdir(self.homefolder):
            os.mkdir(self.homefolder)    


        if url_or_id_to_fetch.startswith("#"):
            url_to_process= LIVECHESSURL+url_or_id_to_fetch
        else:
            url_to_process= url_or_id_to_fetch       

        if not self.is_valid_url(url_to_process):
            #TODO
            return False 

        matchesFound=0 

        if type(url_to_process) is list:
            baseURL = url_to_process[0].replace("view.", "1.pool.")
        elif type(url_to_process) is str:
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
        dgt_boards = jsonT['eboards']

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
        full_filename = self.homefolder+filename
        with open(full_filename, "w",encoding='utf-8') as text_file:
            text_file.write(ePGN_moves)
        print('Saved: ',full_filename)

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
        #-- placeholders
        game_date=None
        whiteFideId, whiteELO, white_title =getFIDEinfo.getFIDEInfo(white, game_date)
        blackFideId, blackELO, blacl_title=getFIDEinfo.getFIDEInfo(black, game_date)

        header = header + f'[WhiteFideId "{whiteFideId}"]'
        header = header + f'[BlackFideId "{blackFideId}"]'
        header = header + f'[WhiteElo "{whiteELO}"]'
        header = header + f'[BlackElo "{blackELO}"]'

        header = header + '[Termination "normal"]' + '\n'
        header = header + '[PlyCount "{}"]'.format(plycount) + '\n'
        return header + '\n'


if __name__ == "__main__":
    pass 
