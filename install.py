B
    ���]   �            	   @   s@  d dl Z d dlZd dlZd dlT yd dlZd dlmZ W n( ek
r`   e�d� e�d� Y nX e�d� e�d� e�d� e�d	� e�d
� e�d� e�d� ed� dZ	dZ
eje
dd�Zeejd �Ze
�d�d Zeed��6Zx.eeje	d�ee	 dd�D ]Ze�e� �q
W W dQ R X e�d� e�d� dS )�    N)�*)�tqdmzpip install requestszpip install tqdmzspkg install jp2a -y && pkg install ruby -y && pkg install figlet -y && pkg install toilet -y && gem install lolcat zrm -rif /sdcard/Alsakka/zmkdir /sdcard/Alsakka/zmkdir /sdcard/Alsakka/youtube/zmkdir /sdcard/Alsakka/payload/zmkdir /sdcard/Alsakka/virusz&rm -rif tools.py && rm -rif install.pyz[1;31mi   zFhttps://github.com/ABDULLAHALSAKKA/ngrok/blob/master/tools.py?raw=trueT)�streamzcontent-length�/������wb)�
chunk_sizez KB)�iterableZtotalZunitzmv 'tools.py?raw=true' tools.pyz%chmod +x tools.py && python3 tools.py)�sys�os�platformZtimeZrequestsr   �ImportError�system�printr   Zurl�get�r�intZheaders�size�split�filename�open�fZiter_content�data�write� r   r   �
install.py�<module>   s2   







 
