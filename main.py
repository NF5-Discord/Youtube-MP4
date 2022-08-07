from pytube import YouTube
from pystyle import Anime, Colorate, Colors, Center, System, Write
import os


asciiart = """ 
,---.    ,---..-------.    ,---.   
|    \  /    |\  _(`)_ \  /,--.|   
|  ,  \/  ,  || (_ o._)| //_  ||   
|  |\_   /|  ||  (_,_) //_( )_||   
|  _( )_/ |  ||   '-.-'/(_ o _)|   
| (_ o _) |  ||   |   / /(_,_)||_  
|  (_,_)  |  ||   |  /  `-----' || 
|  |      |  |/   )  `-------|||-' 
'--'      '--'`---'          '-'   
                                   
                  
"""

asciiart2 = """
   ____     __   ,-----.      ___    _ ,---------.   ___    _  _______       .-''-.          ,---.    ,---..-------.    ,---.   
   \   \   /  /.'  .-,  '.  .'   |  | |\          \.'   |  | |\  ____  \   .'_ _   \         |    \  /    |\  _(`)_ \  /,--.|   
    \  _. /  '/ ,-.|  \ _ \ |   .'  | | `--.  ,---'|   .'  | || |    \ |  / ( ` )   '        |  ,  \/  ,  || (_ o._)| //_  ||   
     _( )_ .';  \  '_ /  | :.'  '_  | |    |   \   .'  '_  | || |____/ / . (_ o _)  |        |  |\_   /|  ||  (_,_) //_( )_||   
 ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|    :_ _:   '   ( \.-.||   _ _ '. |  (_,_)___|        |  _( )_/ |  ||   '-.-'/(_ o _)|   
|   |(_,_)'  : (  '\_/ \   ;' (`. _` /|    (_I_)   ' (`. _` /||  ( ' )  \'  \   .---.        | (_ o _) |  ||   |   / /(_,_)||_  
|   `-'  /    \ `"/  \  ) / | (_ (_) _)   (_(=)_)  | (_ (_) _)| (_{;}_) | \  `-'    /        |  (_,_)  |  ||   |  /  `-----' || 
 \      /      '. \_/``".'   \ /  . \ /    (_I_)    \ /  . \ /|  (_,_)  /  \       /         |  |      |  |/   )  `-------|||-' 
  `-..-'         '-----'      ``-'`-''     '---'     ``-'`-'' /_______.'    `'-..-'          '--'      '--'`---'          '-'   
                                                                                                                                


"""

def init():
 System.Clear()
 System.Title("Youtube Downloader")
 System.Size(190, 50)
 Anime.Fade(text=Center.Center(asciiart), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)

def main():
 System.Clear() 
 print('\n'*2)
 print(Colorate.Diagonal(Colors.red_to_yellow, Center.XCenter(asciiart2)))
 print('\n'*3)    

 link = Write.Input("Entrer le lien de la vidéo :", Colors.red_to_yellow, interval=0.005)
 
 Write.Print("En cours de téléchargement.....", Colors.red_to_yellow, interval=0.005)


 yt = YouTube(link)

 print("")
 Write.Print("Je télécharge " + yt.title, Colors.red_to_yellow, interval=0.005)
 yt.streams.get_highest_resolution().download()

 print("")
 if link.strip():
   Write.Input("Vidéo installé avec succes!", Colors.red_to_yellow, interval=0.005)

 if not link.strip():
  Colorate.Error("Lien invalide.")
 return

print()

if __name__ == '__main__':
    init()
    while True:
       main()