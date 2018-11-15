# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:14:53 2018

@author: Ruslan
"""


import facebook
from fetch import Fetch
from helpers import Helpers
import config

# Get list of posts id of group
# pass list id to function extrakt usesr id who liked post
# add to list all id
# remove duplicate and save

        
if __name__ == "__main__":

    config.GROUP_ID = '192046684527888'
    
    graph = facebook.GraphAPI(access_token=config.CONF_TOKEN) 
    
    fetch = Fetch()
    helpers = Helpers()
    
    """
    # fetch ALL posts id
    # Get errors if many post
    # Application request limit reached
    posts = fetch.fetch_all(graph, config.GROUP_ID, 'feed')
    id_list = helpers.get_id_from_posts(posts)
    id_list = helpers.sub_group_id(id_list, config.GROUP_ID)
    """
    
    # Alternative to take a few last posts.
    posts = fetch.fetch_several_last(graph, config.GROUP_ID, 'feed', 5)
    id_list = helpers.get_id_from_posts(posts)
    id_list = helpers.sub_group_id(id_list, config.GROUP_ID)
    
    
    # save users id who liked posts
    res = helpers.get_likes_from_id(id_list , graph, fetch.fetch_all, 'likes')
    res = helpers.remove_duplicate(res)
    helpers.save('likes', res)
    
    
        
     
    
    
    
    
    
    
    
   
    
   
    
