
# :chess_pawn: Chess Game Preparation Tools 

Tools to help with Chess match preparation or study.

:one: 
## Electronic DGT board (recorded) game downloader "dgtfetch". 

Electronic chess board are increasingly used to capture chess games at tournaments. Most prominent is DGT which also alows tournament arbiter to publish games on the LiveChess Cloud. 
While DGT's Chess Games viewer is fine web app, at this point in time (July 2024) it does not allow for easy download of the game moves in pgn format. So a chess player who might want to download the game(s) in .pgn (portable game notation) format for analysis or future reference can manually re-type the game ... fine workaround if just few games are in question. 

So this tool main function is to fetch game(s) from DGT's LiveChess Cloud and save in .pgn format to local user's disk.
Additional functions (to be added later) are:
I. post-processing of the pgn 
  1. process the game and detect issues (e.g. impossible/incorrect moves: rare but few were observed)
  2. detect Chess opening and add to pgn header 
  3. add player FIDE rating if found on FIDE's website  


As hinted above, the motivation for writting this tool was automation of the extraction of the game moves. Notably the DGT board owner (typically tournament organizer) has access to functions to export and publish the games to his own website. However chess player who wants to get game moves, at present has no such option. In June 2024 I have searched with Google for any pre-existing solution for this minor annoyancem but did not find the code or tool thay would be helpful in that respect. 

To illustrate, this is a screenshot of the Webapp User Interface as at 09/09/2024 

![Example](https://github.com/dusan-dakic/chess_prep_tools/blob/main/doc/livechesscluod-ui-illustration.png)

UI Elements 
1. LiveChess website address 
2. ID of the tournament aws part of the URL 
3. Tournament title 
4. Game players info 
5. DGT info for Round and DGT board 
6. Time on chess clock at the position shown on the browser canvas 
7. Game moves in scrolable panel 
8. Game result, if completed 
9. User interface controls to go to the start/end of the game; previous/next move; previous/next board; flip board; expand to full screen

Recently a new type of WebApp appeared at 'Best in the West 2024'  tournament and it also does not allow easy way to get game in pgn format, but gives Stockfish game evaluation ... see: https://live.hobsonsbaychess.com/tournament/bitw2024

![Example](https://github.com/dusan-dakic/chess_prep_tools/blob/main/doc/bitw-ui-illustration.png)

:two: 

## Diagramming Chess position recieved in FEN format 


### a. as a picture 

![Example](https://github.com/dusan-dakic/chess_prep_tools/blob/main/doc/scandi_output.png)


### b. as a unicode text 

(ToDo List)
![Chess Informant Style Example](https://github.com/dusan-dakic/chess_prep_tools/blob/main/doc/Chess_Informant_Style_Textbook.png)

see: https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode

1♜♞♝♛♚♝♞♜
2♟♟♟♟♟♟♟♟
3⬜⬛⬜⬛⬜⬛⬜⬛
4⬛⬜⬛⬜⬛⬜⬛⬜
5⬜⬛⬜⬛⬜⬛⬜⬛
6⬛⬜⬛⬜⬛⬜⬛⬜
7♙♙♙♙♙♙♙♙
8♖♘♗♕♔♗♘♖
 a b c d e f g h

8♜♞♝♛♚♝♞♜
7♟♟♟♟♟♟♟♟
6▱▰▱▰▱▰▱▰
5▰▱▰▱▰▱▰▱
4▱▰▱▰▱▰▱▰
3▰▱▰▱▰▱▰▱
2♙♙♙♙♙♙♙♙
1♖♘♗♕♔♗♘♖
a b c d e f g h

8	♜	♞	♝	♛	♚	♝	♞	♜
7	♟	♟	♟	♟	♟	♟	♟	♟
6	
5	
4	
3	
2	♙	♙	♙	♙	♙	♙	♙	♙
1	♖	♘	♗	♕	♔	♗	♘	♖
a	b	c	d	e	f	g	h



## **📋 Requirements**

### To run scripts using Python: 
- Python version 3.11.5 ([Click here](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe))
- additional Python components: requirements.txt

```
# pip install -r requirements.txt
```

### To run executable on Windows, Linux

Work in progress ... I'm not keen on bying certificate just to build Exe for Windows*, testing pyinstaller approach.
It appeaqrs that Windows OS classifies everything as malware, so that is annoying.  



## **🛠️ Installation (to run with local Python interpreter) **

To install tool, follow these steps:
- [ ] clone this repo to your local disk, foe example from Command Line type 
    git clone https://github.com/dusan-dakic/chess_prep_tools.git
- [ ] in command line type `CD  chess_prep_tools\dgtfetch`
- [ ] in command line type `python dgtfetch\dgt-dl.py` and in form shown supply toutnament ID and other option as desired.



## ⭐ 'DGT game downloader'

Main function: Download pgn(s) from LiveChess URL.

User needs to supply one input: link to tournament in livechess Cloud, for example:
https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb   

few versions will be available here 
* [ ] Graphical User interface "GUI" version: Everyday PC user version: for manual with use of mouse/keyboard 
* [ ] CLI version: Advanced user version: for manual or scripted use from command line or from power shell or batch/bash 

### Graphical User interface version of the game downloader 

a.k.a GUI version 0.1

how to run:
1. Open Command Prompt (Windows) or Terminal (MacOsX, Linux)
2. Change to folder containing code e.g cd \downloaded_here 
3. Run Python with downloader script like so 
  python dgt-dl.py

or open VS code, open the project, select dgt-dl.py and hit F5 ...   

<!-- [First GUI, very Spartan looking](./doc/downloader_v_0_1.png)-->

![GUI#github](https://github.com/dusan-dakic/chess_prep_tools/blob/main/doc/downloader_v_0_1.png)

Minimum Instructions: 

:one:   replace default link shown in :one: link 
:two:   click on start download 

Other options:
"Filter by name": if a text is entered here the tournament ganes will be checked for "name" and only if white or black player is partial or full match the game will be downloaded, otherwise it will be skipped.

"Saving to PGN": there are two ways to save games: 
  as a collection of all games within single pgn - one file for all 
  as a one pgn file per game, so a link to tournament will produce number of files, one per each match in tournament 
  
"Output folder": this is the location on your disk where files will be downloaded. At the moment a file with matching name will be overwritten without warning. Default folder is one from which you are running the tool.

#### Collection of already downloaded games:

Some games were already downloaded so you can just grab them from *games* folder, and do not need to download them yourself

The full list of tournaments & games downloaded is [click here](Tournament_games_download.md):

| Tournament                             | Rounds | Games | Individual Download | Tournament Download |                                     
| -------------------------------------- | -------| ----- | ------------------- | ------------------- |                                     
| `2024 City of Melbourne Open`          | 9      | 18    |                     |                     |                                     
| `2024 Chess Excellence Open`           | 7      | 14    |                     |                     |                                     
| `2023 MCC Clasic Round Robin`          | 9      | 18    |                     |                     |                                     
| `2024 Chess Artists Alegro`            | 7      | 11*   |                     |                     |                                     
| `2024 Victorian Open`                  | 7      | 28    |                     |                     |                                     
| `2024 Begonia Open`                    | 7      | 70    |                     | [click here](https://github.com/dusan-dakic/chess_prep_tools/blob/main/games/tournaments/Begonia%20Open%202024.pgn)|    
| `2024 Edwin Malitis Major`  *          | 7      | 70    |                     | [click here]()|    

'*' - in progress, at 22/07 3 rounds completed  

"Two places where game may be/is saved"
- in "One PGN per game folder" [/games/all_games]
- in "One PGN per tournament folder" [/games/tournaments]



 # ⭐ Chess Preparation Tools - Technical section   

## Roadmap

* [ ] A. Download and process gemes of a tournament for given link to livechesscloud 
*   [x] 📋 Get all games for all rounds
*   [x] 🔍 Get only games for specified player name
*   [ ] 🔍 Get games for next round / specified round
*   [ ] Add ECO codes info to game
*   [ ] Add FIDE/ACF rating
*   [ ] Add game info to SQLite database
*   [ ] Add SQL database to store Player Ratings, Games
*   [ ] Extend Python with attrs, SQLalchemy
   

User Interface versions:
* [ ] 🚀 GUI (tkinter)
* [ ] CLI (command line)

<!--
:white_check_mark:
:heavy_check_mark:
:x:
:negative_squared_cross_mark:
:a:
:nine:
:chess_pawn:
:chess_queen:
-->

#### ToDo - fix

*  [ ] Move times not included, add and make it option 
*  [ ] Settings file 
*  [ ] GUI make prettier 
*  [ ] Add CLI application wrapper to download games  
  

<!--
### Notes

https://www.markdownguide.org/basic-syntax/
-->
