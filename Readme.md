
# :chess_pawn: Chess Game Preparation Tools 

Tools to help with Chess preparation or study.

:one: 
DGT game downloader. 
Electronic chess board are increasingly used to capture competitive (rated) chess games. Most prominent is CGT which also alows tournament arbiter to publish games on the Cloud. 
While CGT's Chess Games viewer is fine web app, at this point in time (2024) it does not allow for easy download of the game moves, and yet a chess player might want to download the game(s) in .pgn (portable game notation) format for analysis or future reference. 

This tool main function is to fetch game(s) from DGT's Live Cloud and save in .pgn format to local user's disk.

:two: 
Anotating Chess position in FEN format to a picture 
![Example](https://github.com/dusan-dakic/chess_prep_tools/blob/main/scandi_output.png)



## **📋 Requirements**

- Python version 3.11.5 ([Click here](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe))
- additional Python components: {to do}

## **🛠️ Installation**

To install tool, follow these steps:
- [ ] clone this repo to your local disk, foe example from Command Line type 
    git clone https://github.com/dusan-dakic/chess_prep_tools.git


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
  python cgtdownload.py
  

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
*   [ ] tbd 

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
