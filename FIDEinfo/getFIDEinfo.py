"""
  
"""

def getFIDEInfo(player:str, game_date:str, ratingtype:str ='STD'):
    ratingELO=0
    FIDEid = ''
    FIDEtitle=""

    if player=="FM Kai Jie Soo":
        FIDEid = '5803454'
        if ratingtype=='STD':
            ratingELO=2179
        elif ratingtype=='RAPID':
            ratingELO=1989
        elif ratingtype=='BLITZ':
            ratingELO=2123
        else:
            ratingELO=1399

        FIDEtitle="FIDE Master"
    elif player=="CM Arthur Gao":
        FIDEid = '3240444'
        if ratingtype=='STD':
            ratingELO=2040
        elif ratingtype=='RAPID':
            ratingELO=1719
        elif ratingtype=='BLITZ':
            ratingELO=1936
        else:
            ratingELO=1399

        FIDEtitle="Candidate Master"
    else:
        FIDEid = f'<lookup_FIDE_id:{player}>'
        ratingELO=f'<lookup_FIDE_ELO:{player}>'
        FIDEtitle=f'<lookup_FIDE_title:{player}>'



    return FIDEid, ratingELO, FIDEtitle