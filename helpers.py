# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:49:10 2018

@author: Ruslan
"""
import re

class Helpers():
    
    def save(self, namefile, content):
        with open(namefile + '.txt', 'w') as f:
           for item in content:
              f.write("%s\n" % item)
        
              
    def remove_duplicate(self, sort_list):
        final_list = []
        for i in sort_list:
           if i not in final_list:
              final_list.append(i)
        return final_list
    
    def get_id_from_posts(self, posts_list):
        result = []
        for i in posts_list:
            result.append(i["id"])
        return result
    
    def get_likes_from_id(self, posts_list, graph, fetch, connection_type):
        result = []
        for post in posts_list:
            res = fetch(graph, post, connection_type)
            result = result + res
        return result
    
    def sub_group_id(self, group_list, group_id):
        result = []
        for item in group_list:
            i = re.sub(group_id + '_', ' ', item)
            result.append(i)
        return result
        