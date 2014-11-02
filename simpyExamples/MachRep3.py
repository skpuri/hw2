# MachRep3.py

# SimPy example:  Variation of Mach1.py, Mach2.py.  Two machines, but
# sometimes break down.  Up time is exponentially distributed with mean
# 1.0, and repair time is exponentially distributed with mean 0.5.  In
# this example,there is only one repairperson, and she is not summoned
# until both machines are down.  We find the proportion of up time.  It
# should come out to about 0.45.

from SimPy.Simulation import *
from random import Random,expovariate

class G:  # globals
   Rnd = Random(12345)
   RepairPerson = Resource(1)

class MachineClass(Process):
   MachineList = []  # list of all objects of this class
   UpRate = 1/1.0
   RepairRate = 1/0.5
   TotalUpTime = 0.0  # total up time for all machines
   NextID = 0  # next available ID number for MachineClass objects
   NUp = 0  # number of machines currently up
   def __init__(self):
      Process.__init__(self)  
      self.StartUpTime = None  # time the current up period started
      self.ID = MachineClass.NextID   # ID for this MachineClass object
      MachineClass.NextID += 1
      MachineClass.MachineList.append(self)
      MachineClass.NUp += 1  # start in up mode
   def Run(self):
      while 1:
         self.StartUpTime = now()  
         yield hold,self,G.Rnd.expovariate(MachineClass.UpRate)
         MachineClass.TotalUpTime += now() - self.StartUpTime
         # update number of up machines
         MachineClass.NUp -= 1
         # if only one machine down, then wait for the other to go down
         if MachineClass.NUp == 1:
            yield passivate,self
         # here is the case in which we are the second machine down;
         # either (a) the other machine was waiting for this machine to 
         # go down, or (b) the other machine is in the process of being
         # repaired 
         elif G.RepairPerson.n == 1:
            reactivate(MachineClass.MachineList[1-self.ID])
         # now go to repair
         yield request,self,G.RepairPerson
         yield hold,self,G.Rnd.expovariate(MachineClass.RepairRate)
         MachineClass.NUp += 1
         yield release,self,G.RepairPerson

def main():
   initialize()  
   for I in range(2):
      M = MachineClass()
      activate(M,M.Run())
   MaxSimtime = 10000.0
   simulate(until=MaxSimtime)
   print 'proportion of up time was', MachineClass.TotalUpTime/(2*MaxSimtime)

if __name__ == '__main__':  main()
