
# Chess Preparation Tools 

as in tools to help with preparation for Chess tournament games

Playing on tournaments, some of my opponents will have theit games captured by Electronic DGT chess boards.
However to access the all game moves one has to go through DGT's Live Cloud interface and getting pgn was 
easy in past but not any more

Status: work in progress 
------------------------


## 'DGT downloader' Download pgn from LiveChess URL

### Roadmap

* [ ] A. Download and process gemes of a tournament for given link to livechesscloud 
    [x] Get all games for all rounds 
    [x] Get only games for specified player name 
    [ ] Add ECO codes info to game  
    [ ] Add FIDE/ACF rating 
    [ ] Add game info to SQLite database
    [ ] tbd 

#### ToDo 
  [ ] Move times not included, add and make it option 
  [ ] Settings file 
  [ ] GUI make prettier 
  [ ] Add CLI application wrapper to download games  


### Samples 

Download chess games from https://view.livechesscloud.com

example links:
1. https://view.livechesscloud.com/#c93079a2-e77a-4699-be19-33e6584d0acb
2. https://view.livechesscloud.com/#f9168763-9c5c-4498-981e-d1c7396003d6
3. https://view.livechesscloud.com/#8cf474a3-84a2-4fe8-ab2c-aa93562ebff4
4. https://view.livechesscloud.com/#12b35db7-f34f-4be9-95e9-5fa4d7912076
5. https://view.livechesscloud.com/#8b472897-2556-40b5-bc41-3adaeda50b0e

#### Games downloaded already 
  see games folder 
  

  GET
  54.37.200.156:443
  https://1.pool.livechesscloud.com/get/f9168763-9c5c-4498-981e-d1c7396003d6/round-3/game-1.

pgn4web live broadcast: flash replacement  
https://www.ballaratchess.com/begonia/2024/games.html
  see: Historical Games database (1000 games)



{"live":false,"serialNr":"45539","firstMove":1702888257332,"chess960":518,"result":"BLACKWIN","comment":null,"clock":null,"moves":["e4 4903+556","c5 5453+8","Nc3 4921+11","Nc6 5478+6","Bb5 4947+4","Nd4 5501+7","Nf3 4970+7","g6 5523+8","Ba4 4976+24","Bg7 5541+12","O-O 4865+141","a6 5550+21","Nxd4 4893+2","cxd4 5559+21","Ne2 4922","b5 5482+108","Bb3 4598+354","Bb7 5446+66","d3 4623+5","d5 5364+112","f3 4633+20","e6 5152+243","Qe1 4637+25","h6 4647+536","Qf2 4572+95","Ne7 4440+238","Bd2 4298+303","O-O 4403+67","a4 4200+129","bxa4 4221+211","Rxa4 4208+23","Bc6 4219+33","Rxd4 3902+336","e5 4085+164","Rb4 3762+170","a5 4097+17","Rb6 3277+514","d4 4113+14","Rxc6 3282+26","Nxc6 4142+2","Bd5 3290+21","Rc8 4141+31","f4 3108+211","Kh8 3992+179","fxe5 2877+261","Nxe5 4005+16","Bb3 2702+207","Kh7 3762+273","Qe1 2660+72","Rb8 3679+113","Bxa5 2622+68","Qg5 3509+200","Bd2 2599+53","Qd8 3239+300","Bb4 2115+514","Re8 3095+173","Nf4 2084+61","h5 2267+858","Nd5 1918+197","Qd7 2175+120","Qg3 1484+465","Kh8 1753+451","Bd2 1354+160","Qg4 1595+189","Qxg4 1179+205","hxg4 1605+19","Bf4 1093+117","Rb7 1493+140","Bxe5 976+149","Rxe5 1241+281","Nf6 890+117","Bxf6 1224+47","Rxf6 918+2","Kg7 1245+8","Rd6 924+23","f5 1212+64","Rxd4 930+24","f4 1114+127","Kf2 856+106","Rh5 1104+40","e5 859+26","g5 1116+19","e6 877+12","Kf6 1080+65","Rd7 881+27","Rxd7 +13","exd7","Ke7 1083+13","Be6 880+30","Rxh2 1063+51","Bxg4 904+6","Rh1 1076+16","Ke2 894+39","Rc1 1070+35","Kd2 905+20","Rg1 1094+6","Bh3 791+144","g4 1112+12","Bxg4 791+31","Rxg2+ 1135+7"]}

[
### Notes


Other
=====

Markdown syntax 
---------------

https://www.markdownguide.org/basic-syntax/
