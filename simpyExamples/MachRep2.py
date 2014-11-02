# MachRep2.py

# SimPy example:  Variation of MachRep1.py.  Two machines, but sometimes
# break down.  Up time is exponentially distributed with mean 1.0, and
# repair time is exponentially distributed with mean 0.5.  In this
# example, there is only one repairperson, so the two machines cannot be
# repaired simultaneously if they are down at the same time.

# In addition to finding the long-run proportion of up time as in
# Mach1.py, let's also find the long-run proportion of the time that a
# given machine does not have immediate access to the repairperson when
# the machine breaks down.  Output values should be about 0.6 and 0.67.

from SimPy.Simulation import *
from random import Random,expovariate,uniform

class G:  # globals
   Rnd = Random(12345)
   # create the repairperson 
   RepairPerson = Resource(1)

class MachineClass(Process):
   TotalUpTime = 0.0  # total up time for all machines
   NRep = 0  # number of times the machines have broken down
   NImmedRep = 0  # number of breakdowns in which the machine 
                  # started repair service right away
   UpRate = 1/1.0  # breakdown rate
   RepairRate = 1/0.5  # repair rate
   # the following two variables are not actually used, but are useful
   # for debugging purposes
   NextID = 0  # next available ID number for MachineClass objects
   NUp = 0  # number of machines currently up
   def __init__(self):
      Process.__init__(self)  
      self.StartUpTime = 0.0  # time the current up period stated
      self.ID = MachineClass.NextID   # ID for this MachineClass object
      MachineClass.NextID += 1
      MachineClass.NUp += 1  # machines start in the up mode
   def Run(self):
      while 1:
         self.StartUpTime = now()  
         yield hold,self,G.Rnd.expovariate(MachineClass.UpRate)
         MachineClass.TotalUpTime += now() - self.StartUpTime
         # update number of breakdowns
         MachineClass.NRep += 1
         # check whether we get repair service immediately
         if G.RepairPerson.n == 1:
            MachineClass.NImmedRep += 1
         # need to request, and possibly queue for, the repairperson
         yield request,self,G.RepairPerson
         # OK, we've obtained access to the repairperson; now
         # hold for repair time
         yield hold,self,G.Rnd.expovariate(MachineClass.RepairRate)
         # repair done, release the repairperson
         yield release,self,G.RepairPerson

def main():
   initialize()  
   # set up the two machine processes
   for I in range(2):
      M = MachineClass()
      activate(M,M.Run())
   MaxSimtime = 10000.0
   simulate(until=MaxSimtime)
   print 'proportion of up time:', MachineClass.TotalUpTime/(2*MaxSimtime)
   print 'proportion of times repair was immediate:', \
      float(MachineClass.NImmedRep)/MachineClass.NRep

if __name__ == '__main__': main()
