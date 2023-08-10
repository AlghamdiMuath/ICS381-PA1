#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class SimpleACReflexAgent: 
       def __init__(self, min_threshold, max_threshold):   
           self.min_threshold = min_threshold   
           self.max_threshold = max_threshold     
           
       def select_action(self, percept):         
           if not percept[1] and percept[0] >= self.max_threshold: 
               return 'TurnOn'          
           elif percept[1] and percept[0] <= self.min_threshold:   
               return 'TurnOff'
           else:               
               return None    
           
class SimpleACEnvironment:     
   def __init__(self, ac_agent, starting_temp=28 ):         
       self.ac_agent = ac_agent             
       self.temperature= starting_temp            
       self.num_agent_actions = 0         
       self.is_ac_on = False            
   def tick(self):     
       returned_action = self.ac_agent.select_action([self.temperature, self.is_ac_on])  
       if returned_action: 
           self.num_agent_actions += 1           
       if returned_action == 'TurnOn':                 
           self.is_ac_on = True                 
       elif returned_action == 'TurnOff':                 
           self.is_ac_on = False           
       if self.is_ac_on:               
           self.temperature-= 1            
       else:   
           self.temperature+= 1            
   def simulate(self, num_timesteps):         
       for i in range(num_timesteps):            
           self.tick()    


# In[ ]:




