U
    X��]�  �                   @   s|   d dl Z d dlZd dlZzd dlZd dlmZ W n( ek
rX   e �d� e �d� Y nX dd� Zdd� Zd	d
� Z	e�  dS )�    N)�tqdmzpip install tqdmzpip install requestsc                  C   sT   dd� } t �d� | d� td�}|dkr2t�  n|dksB|dkrJt�  nt�  d S )	Nc                 S   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
g-C��6?)�sys�stdout�write�flush�time�sleep)�s�c� r   �
install.py�slowprin	   s    
zmeprint.<locals>.slowprin�clearu�  
[1;31m _______   _          _______   _______   _         _         _______
[1;32m(  ___  ) ( \        (  ____ \ (  ___  ) | \    /\ | \    /\ (  ___  )
[1;33m| (   ) | | (        | (    \/ | (   ) | |  \  / / |  \  / / | (   ) |
[1;36m| (___) | | |        | (_____  | (___) | |  (_/ /  |  (_/ /  | (___) |
[1;35m|  ___  | | |        (_____  ) |  ___  | |   _ (   |   _ (   |  ___  |
[1;30m| (   ) | | |              ) | | (   ) | |  ( \ \  |  ( \ \  | (   ) |
[1;36m| )   ( | | (____/\  /\____) | | )   ( | |  /  \ \ |  /  \ \ | )   ( |
[1;31m|/     \| (_______/  \_______) |/     \| |_/    \/ |_/    \/ |/     \|

                      [1;31m$[1;34m <=> [1;31m$[1;32m 1.2.0 [1;31m$[1;34m <=>[1;31m $$[1;30m
[1;34m╔--------------------------------------------------------------------╗
[1;34m|                                                                    [1;34m|
[1;34m|  [1;30m[[1;31m01[1;30m][1;36m - Metasploit      [1;30m[[1;31m02[1;30m][1;36m - Sqlmap        [1;30m[[1;31m03[1;30m][1;36m - Virus          [1;34m|
[1;34m|  [1;30m[[1;31m04[1;30m][1;36m - Ngrok           [1;30m[[1;31m05[1;30m][1;36m - Nmap          [1;30m[[1;31m06[1;30m][1;36m - Spammer        [1;34m|
[1;34m|  [1;30m[[1;31m07[1;30m][1;36m - Open-port      [1;30m [[1;31m08[1;30m][1;36m - cp-panel      [1;30m[[1;31m09[1;30m][1;36m - Hash           [1;34m|
[1;34m|  [1;30m[[1;31m10[1;30m][1;36m - Facebook       [1;30m [[1;31m11[1;30m][1;36m - Gmail         [1;30m[[1;31m12[1;30m][1;36m - Yahoo          [1;34m|
[1;34m|  [1;30m[[1;31m13[1;30m][1;36m - Hotmail        [1;30m [[1;31m14[1;30m][1;36m - Twitter       [1;30m[[1;31m15[1;30m][1;36m - Woordlist      [1;34m|
[1;34m|  [1;30m[[1;31m16[1;30m][1;36m - fb-clong       [1;30m [[1;31m17[1;30m][1;36m - image         [1;30m[[1;31m18[1;30m][1;36m - Youtube      [1;34m  |
[1;34m|  [1;30m[[1;31m19[1;30m][1;36m - updaete        [1;30m [[1;31m20[1;30m][1;36m - info          [1;30m[[1;31m00[1;30m][1;36m - Exit      [1;34m     |
[1;34m|                                                                    [1;34m|
[1;34m╚--------------------------------------------------------------------╝



    z [1;31mEnter number >> :[1;32m Z19�0Z00)�os�system�input�install�exit�updaete)r   Znumr   r   r   �meprint   s    
r   c               	   C   s�   t �d� t �d� t �d� t �d� t �d� t �d� t �d� td� d	} d
}tj|dd�}t|jd �}|�d�d }t|d��0}t	|j
| d�||  dd�D ]}|�|� q�W 5 Q R X t �d� d S )Nz�pkg install python -y && pkg install python2 -y && pkg install ruby -y && pkg install figlet -y && pkg install jp2a -y && pkg install toilet -y && gem install lolcat zrm -rif /sdcard/Alsakka/zmkdir /sdcard/Alsakka/zmkdir /sdcard/Alsakka/youtube/zmkdir /sdcard/Alsakka/payload/zmkdir /sdcard/Alsakka/viruszrm -rif tools.pyz[1;31mi   zFhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/tools.py?raw=trueT)�streamzcontent-length�/������wb)�
chunk_sizez KB)�iterableZtotalZunitzmv 'tools.py?raw=true' tools.py)r   r   �print�requests�get�intZheaders�split�openr   Ziter_contentr   )r   Zurl�r�size�filename�f�datar   r   r   r   0   s"    






r   c                   C   s6   t �d� td� td� td� t�d� t�  d S )Nr   a0  [1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_[1;31m_zd[1;32m



       Please press updaete [1;36m[[1;31m19[1;36m][1;32m to run the tool correctly


�   )r   r   r   r   r	   r   r   r   r   r   r   B   s    

r   )
r   r   r   r   r   �ImportErrorr   r   r   r   r   r   r   r   �<module>   s   
(