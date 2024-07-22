#-- 
#  Download pgn from LiveChess URL, 
#  version 0.1 - bare minimum
#  version 0.2 - bare minimum+



#  TODO from ePGN extract time from integer 
"""
 "moves": [
        "d4 5454+6",
        "Nf6 5450+10",
        "c4 5475+9",
        "e6 5474+6",
"""

import os
import sys
import requests
import json
import pandas as pd 
import datetime 

SECTOR_SIZE = 512

def main(url_to_process: str , homedir:str ):
    #           "https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb",
    baseURL = "https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb"
    baseURL = url_to_process.replace("view.", "1.pool.")
    baseURL = baseURL.replace(".com/#", ".com/get/")
    
    requestTournament = baseURL +"/tournament.json"

    #requests.get(url, params={key: value}, args) 
    tournament = requests.get(requestTournament) 

    #print("apparent_encoding:", tournament.apparent_encoding)
    #print("content:", tournament.content)
    jsonT = tournament.json()
    print(json.dumps(jsonT, indent=4))

    print("elapsed", tournament.elapsed)

    #df_1 = pd.DataFrame(jsonT)
    #print(df_1.to_string())

    print(jsonT['id'])
    print(jsonT['name'])
    print(jsonT['location'])
    print(jsonT['country'])

    # lists of rounds and cgt boards 
    turnir_rounds = jsonT['rounds']
    cgt_boards = jsonT['eboards']
    print("="* 80)
    print('Rounds=', len(turnir_rounds), type(turnir_rounds))
    print('eboards=', len(cgt_boards), type(cgt_boards))

    
    # print(jsonT['rounds'])
    r=0
    for round_item in jsonT['rounds']:
        r+=1 
        round_idx=r

        gamecount=round_item['count']

        print(round_idx, 'Game count', round_item['count'])
        if round_item['count'] >0:
            pairings = get_round_pairs(baseURL, round_idx)
            # pairings_count= len(pairings)
            # print('pairings_count=', pairings_count)
            pairno=1
            for game_pair in pairings['pairings']:
                white_player= game_pair["white"]
                black_player= game_pair["black"]
                
                white = "{} {} {} {}".format(white_player["title"], white_player["fname"],white_player["mname"],white_player["lname"])
                black = "{} {} {} {}".format(black_player["title"], black_player["fname"],black_player["mname"],black_player["lname"])
                white=white.replace("None ", "")
                black=black.replace("None ", "")
                
                game_result=game_pair["result"]
                pgnfilename = white+ "-vs-"+ black + " [Round-{}_Board-{}].pgn".format(round_idx,pairno)
                print("="*40)
                print(white, "-vs-", black, game_result)
                print("="*40)
                                
                #-- get game header details and get game moves 
                round_number=round_idx
                round_board=pairno
                ePGN = get_round_game(baseURL, round_number, round_board )
                pgnmoves = make_pgn(ePGN)
                pgnmoves += game_result

                pgn_head = make_pgn_header(white=white, black=black, result=game_result, tournament=jsonT)

                full_pgn = pgn_head + pgnmoves
                pgnmoves = save_to_pgn(pgnfilename, full_pgn)

            #get_games(round=r, gcount=gamecount, gameindex=0, url=baseURL) 
            pairno+=1
        r+=1

def get_round_pairs(url, round):
    request_matches = url+'/round-{}/index.json'.format(round)
    round_matches = requests.get(request_matches).json() 
    #print(round_matches)

    #print("="*80)
    #print(json.dumps(round_matches, indent=4))
    #print("="*80)
    
    #round_matches['pairings'][0]
    #round_matches['pairings'][1]['white']
    #round_matches['pairings'][0]['result']
    

    #for par in round_matches:
    #    print(par)
       
        #print(par[0]['white'])
        #print(par[0]['black'])
        
        
        

    return round_matches

    pass
    #  "https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb/round-5/index.json"

def get_round_game(baseURL, round_number, round_board ):
    #baseURL = "https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb"
    #          "https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb/round-5/game-1.json?poll"

    gameURL = baseURL+ "/round-{}/game-{}.json?poll".format(round_number, round_board)
    round_game = requests.get(gameURL).json() 

    # print(round_game)
    # round_game['moves']

    #print("="*80)
    #print(json.dumps(round_game, indent=4))
    #print("="*80)
    return round_game




def get_games(round=1, gcount=0, gameindex=1, url=''):
    #baseURL = "https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb"
    #            https://1.pool.livechesscloud.com/get/c93079a2-e77a-4699-be19-33e6584d0acb/round-5/game-1.json?poll
    
    pass 

def make_pgn(ePGN_moves):
    move_pgn = ""
    ply_counter=0
    move_counter=0
    for move in ePGN_moves["moves"]:
        move_text = move.split()[0]
        ply_counter+=1
        if ply_counter % 2 == 1:
            move_counter+=1
            move_pgn = move_pgn+"{}. ".format(move_counter)+move_text+" "
        else:
            move_pgn = move_pgn+move_text+" "    
    return move_pgn

def save_to_pgn(filename: str, ePGN_moves: str, folder: str):
    with open(filename, "w") as text_file:
        text_file.write(ePGN_moves)



def make_pgn_header(white, black, result, tournament=None, round=None ):

    header = '[ePGN "0.1;DGT LiveChess/2.2.5"]' + os.linesep
    if tournament:
        header = header + '[Event "{}"]'.format(tournament['name']) + os.linesep
        header = header + '[Site "{}, {}"]'.format(tournament['location'], tournament['country'])

    if round:
        #header = header + '[Date "2023.05.28"]
        pass
    #header = header + '[Round "2.10"]

    header = header + '[White "{}"]'.format(white) + os.linesep
    header = header + '[Black "{}"]'.format(black) + os.linesep
    header = header + '[Result "{}"]'.format(result) + os.linesep
    #header = header + '[TimeControl "75 minutes +30 seconds increment"]
    #header = header + '[WhiteFideId "3247155"]
    #header = header + '[BlackFideId "3244792"]
    #header = header + '[WhiteElo "1483"]
    #header = header + '[BlackElo "1242"]
    return header + os.linesep



'''
def program(drive, first, last):
    if first > last:
        first, last = last, first
    data = get_data(drive, first, last)
    sectors = partition(data, SECTOR_SIZE)
    show_hex(first, last, sectors)

def get_data(drive, first, last):
    if os.name == 'posix':
        drive = file('/dev/' + drive)
    elif os.name == 'nt':
        drive = file(r'\\.\%s:' % drive)
    else:
        raise Exception('Do Not Know How To Access Drives')
    return read_all(drive, first, last - first + 1)

def read_all(drive, start_sector, sectors_to_read):
    start = start_sector * SECTOR_SIZE
    end = sectors_to_read * SECTOR_SIZE
    all_data = ''
    while start > 0:
        temp = drive.read(start)
        if not temp:
            temp = drive.read(start)
            if not temp:
                raise Exception('Cannot Read First Sector')
        start -= len(temp)
    assert start == 0
    while end > 0:
        temp = drive.read(end)
        if not temp:
            temp = drive.read(end)
            if not temp:
                if not all_data:
                    raise Exception('Cannot Find Requested Data')
                return all_data
        all_data += temp
        end -= len(temp)
    assert end == 0
    return all_data

def partition(string, size):
    if len(string) % size:
        parts = len(string) / size + 1
    else:
        parts = len(string) / size
    return [string[index*size:index*size+size] for index in range(parts)]

def show_hex(first, last, sectors):
    print '=' * 77
    for index in range(len(sectors)):
        print 'SECTOR', index + first
        print '=' * 77
        engine(sectors[index], index + first)
        print '=' * 77

def engine(string, sector):
    parts = partition(string, 16)
    rule = printable()
    for index in range(len(parts)):
        print ' | '.join([hex(index + sector * 32)[2:].upper().zfill(7)[-7:] + '0', \
                          pad_right(convert_hex(parts[index]), 47), \
                          convert_print(parts[index], rule)])

def printable():
    return ''.join([chr(byte) for byte in range(256) \
                    if len(repr(chr(byte))) == 3 or byte == ord('\\')])

def pad_right(string, length, padding=' '):
        return string + padding[0] * (length - len(string))

def convert_hex(string):
    return ' '.join([hex(ord(character))[2:].upper().zfill(2) \
                     for character in string])

def convert_print(string, rule):
    return ''.join([character in rule and character \
                    or '.' for character in string])
'''

if __name__ == '__main__':
    sample= [
    "https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb",
    "https://view.livechesscloud.com/#f9168763-9c5c-4498-981e-d1c7396003d6",
    "https://view.livechesscloud.com/#8cf474a3-84a2-4fe8-ab2c-aa93562ebff4"
    ]
    main(sample[0])

"""
Kasparov, Garry vs. Radikovic, Anamarija
1.e4 d5 2.exd5 Nf6 3.Nf3 Nxd5 4.d4Bg45.h3Bh56.Be2e67.O-OBe78.Ne5Bxe29.Qxe2O-O10.Rd1c611.c4Nf612.Nc3Nbd713.Rd3Qc714.Bf4Bd615.Rg3Kh816.Rd1g617.Rf3Kg718.Qe3Rfe819.Bg5Bxe520.dxe5Ng821.Rd6h622.Bf6+Ndxf623.exf6+Kh724.Ne4Rad825.c5b626.b4bxc527.bxc5Qa528.a3Qa629.Qd4Rb830.Rd3Rb731.Kh2e532.Qc3Rc733.Rd7Qc834.Qd2Rxd735.Rxd7Rf836.Qd6Qe837.Qxc6Kh838.Qd6Qa839.c6Rc840.Rb7Re841.Rxf7Qc842.Rd71-0
"""    