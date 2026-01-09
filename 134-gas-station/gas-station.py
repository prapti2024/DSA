class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        totalcost  = 0 
        totalgas = 0 
        for i in range(len(gas)):
            totalcost += cost[i]
            totalgas += gas[i] #Total gas and total cost , if gas < cost, it will never move
        
        if(totalgas - totalcost) < 0:
            return -1 
        
        currentgas = 0 
        startindex = 0 
        for i in range(len(gas)):
            currentgas += gas[i] - cost[i] #Add to current gas tank 
            if (currentgas < 0): #If cost > tank, go to next station, current gas tank empty 
                startindex = i+1    
                currentgas = 0
        
        return startindex