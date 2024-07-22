#-- 
#  Download pgn from LiveChess URL by Dusan Dakic
#  version 0.1 - bare minimum
#  version 0.2 - added option to save all games into single pgn 
#  TODO from ePGN moves extract clock time and include with moves
#       "moves": ["d4 5454+6", "Nf6 5450+10", "c4 5475+9", "e6 5474+6",
#  TODO pip install python-colored-print
#--
version="0.2"
import os
import requests
import sys 
import datetime 

class Main:
    def __init__(self, db=None, log=None, app=None):
        #TODO read config 
        #self.debug = app.configData["JobClient"]["DEBUG"]
        now = datetime.datetime.now()
        print("Download pgn from LiveChess URL v{}".format(version))
        print("Start: {}}".format(now))
        
    def fetch_games(self, url, combined):
        self.runextract(self, url_to_process=url, one_pgn_for_all = True)

    def runextract(self, url_to_process, one_pgn_for_all = False):
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
                    
                    white = "{} {} {} {}".format(white_player["title"], white_player["fname"],white_player["mname"],white_player["lname"])
                    black = "{} {} {} {}".format(black_player["title"], black_player["fname"],black_player["mname"],black_player["lname"])
                    white=white.replace("None ", "")
                    black=black.replace("None ", "")
                    
                    game_result=game_pair["result"]
                    pgnfilename = white+ "-vs-"+ black + " [Round-{}_Board-{}].pgn".format(round_idx,pairno)
                                
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

    cli_arguments = sys.argv[1:]
    livegames=[]
    
    if len(cli_arguments) > 0:
        for url in cli_arguments:
            livegames.append(url)        
    else:
        livegames.append("https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb")   # 0
        #livegames.append("https://view.livechesscloud.com/#f9168763-9c5c-4498-981e-d1c7396003d6")   # 1 =  2023 MCC Classic Round Robin
        #livegames.append("https://view.livechesscloud.com/#8cf474a3-84a2-4fe8-ab2c-aa93562ebff4")   # 2 =  2024 Chess Excellence Open
        #livegames.append("https://view.livechesscloud.com/#416574a0-a4ad-49de-b099-d2ab317e9cb7")   # 3 =  MCC CH 2023

    #app = Main(db=dbase, log=logger, app=APPControl)
    app = Main()

    #alternative #1
    for url in livegames:
        app.runextract(url_to_process=url, one_pgn_for_all = False)

    #alternative #2: run 
    #app.runextract(url_to_process=livegames[0], one_pgn_for_all = False)
    #app.runextract(url_to_process=livegames[1], one_pgn_for_all = True)
    #app.runextract(url_to_process=livegames[2], one_pgn_for_all = True)
    #app.runextract(url_to_process=livegames[3], one_pgn_for_all = False)

# ------------------------------------------------------------------------------

