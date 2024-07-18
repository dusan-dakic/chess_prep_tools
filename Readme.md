
# ⭐ Chess Preparation Tools 

Tools to help with Chess preparation or study.

:one: DGT game downloader 
Electronic chess board are increasingly used to capture competitive (rated) chess games. Most prominent is CGT which also alows tournament arbiter to publish games on the Cloud. 
While CGT's Chess Games viewer is fine web app, at this point in time (2024) it does not allow for easy download of the game moves, and yet a chess player might want to download the game(s) in .pgn (portable game notation) format for future reference. 
This tool main function is to fetch game(s) from DGT's Live Cloud and save in .pgn format to local user's disk.

:two: tbd



## **📋 Requirements**

- Python version 3.11.5 ([Click here](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe))

## **🛠️ Installation**

To install tool, follow these steps:


Status: work in progress 
------------------------


## :chess_pawn: 'DGT game downloader'

Download pgn from LiveChess URL.

User needs to supply one input: link to tournament in livechess Cloud, for example:
https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb   

### Graphical User interface version 0.1

[First GUI, very Spartan looking](.\doc\downloader_v_0_1.png)



### Roadmap

* [ ] A. Download and process gemes of a tournament for given link to livechesscloud 
*   [x] 📋 Get all games for all rounds
*   [x] 🔍 Get only games for specified player name
*   [ ] Add ECO codes info to game
*   [ ] Add FIDE/ACF rating
*   [ ] Add game info to SQLite database
*   [ ] tbd 

User Interface versions:
* [ ] 🚀 GUI (tkinter)
* [ ] CLI (command line)

:white_check_mark:
:heavy_check_mark:
:x:
:negative_squared_cross_mark:
:a:
:nine:
:chess_pawn:
:chess_queen:

#### ToDo 

*  [ ] Move times not included, add and make it option 
*  [ ] Settings file 
*  [ ] GUI make prettier 
*  [ ] Add CLI application wrapper to download games  
  


### Already downloaded (games collection) 

#### Source tournaments 

Download chess games from https://view.livechesscloud.com

example links:
1. https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb
2. https://view.livechesscloud.com/#f9168763-9c5c-4498-981e-d1c7396003d6
3. https://view.livechesscloud.com/#8cf474a3-84a2-4fe8-ab2c-aa93562ebff4
4. https://view.livechesscloud.com/#12b35db7-f34f-4be9-95e9-5fa4d7912076
5. https://view.livechesscloud.com/#8b472897-2556-40b5-bc41-3adaeda50b0e

#### Games downloaded already 
  see games folder 
  

### Notes


Other
=====

Markdown syntax 
---------------

https://www.markdownguide.org/basic-syntax/
