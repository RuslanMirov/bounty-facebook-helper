# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:36:29 2018

@author: Ruslan
"""
import requests
import time

class Fetch():
    
    def fetch_all(self, graph, object_id, connection):
        
        likes = graph.get_connections(id=object_id, connection_name=connection)
        result = likes["data"]
        first = True
    
        while True:
        
          try:
             if first:
               next_c = likes['paging']['next']
         
             time.sleep(2)
        
             status_cursor = requests.get(next_c)
         
             res = status_cursor.json()
             result.extend(res["data"])
         
             first = False
          
             next_c = res['paging']['next']
         
          except:
            break
        
        return result
    
    def fetch_several_last(self, graph, object_id, connection, number):
        likes = graph.get_connections(id=object_id, connection_name=connection, limit=number)
        result = likes["data"]
        return result
        
    
     