# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 17:11:26 2022

@author: Win10Admin
"""
from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower();
    if user_message in ("ciao", "come va?", "come va?"):
        return "Ciao sono il bot di Michele!"
    if user_message in ("ora"):
        now = datetime.now();
        date_time = now.strftime("%d/%m/%y, %H:%M:%S");
        return str(date_time);
    
    return "Inserisci un comando valido (comandi validi: ciao, ora)";