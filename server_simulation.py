#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
class ServerAgent:
    def __init__(self, small_count = 10, medium_count=10, large_count=10):
        self.small_count = small_count 
        self.medium_count = medium_count
        self.large_count = large_count
        
    def select_action (self, percept):
        if percept <= 33 and self.large_count:
            size = "large"
            self.large_count -= 1
        elif percept <=66 and percept >=34 and self.medium_count:
            size = "medium"
            self.medium_count -= 1
        elif percept <= 99 and percept >= 67 and self.small_count:
            size = "small"
            self.small_count -= 1
        else:
            size= None
        return size
    
    def storage_empty(self):
        if self.large_count + self.medium_count + self.small_count == 0:
            return True
        else:
            return False

class ServerEnvironment:
    def __init__(self , server_agent):
        self.server_agent = server_agent
        self.num_agent_actions= 0
    def tick (self):
        thirst = random.randint(a=0, b=130)
        returned_action = self.server_agent.select_action(thirst)
        self.num_agent_actions+=1
    def simulate(self):
        while not self.server_agent.storage_empty():
            self.tick()

