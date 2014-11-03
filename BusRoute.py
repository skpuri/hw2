# BusRoute.py - A simple simulation of a bus route
# Alan Salazar Wink - 999868379
#
# Usage:
# python BusRoute.py nstop nbus arrivalrate travelrate maxsimtime
#
# nstop: the number of bus stops
# nbus: the number of buses, assumed less than nstop
# arrivalrate: the reciporocal of the mean time between passenger arrivals (per bus stop)
# travelrate: the reciporocal of the mean time needed for a bus to go from one bus stop to the next
# maxsimtime: the amount of time to be simulated

import sys
from SimPy.Simulation import *
from random import Random,expovariate

class G:
	Rnd = Random(12345) # Random Seed
	arrivalRate = 0
	travelRate = 0

class Bus:
	circuitTime = [] # Store all the times to make a full circuit
	def __init__(self):
		Process.__init__(self) # SimPy required		
		self.startTime = 0 # Time to start a new circuit
		self.startBusStopId = 0 # First bus stop
		self.busStopId = 0 # Stop ID the bus is in

	def Run(self):
		self.startTime = now() # Starting a new circuit
		while 1:
			if not BusStop.stop[self.busStopId].bus: # There is no bus on the bus stop
				BusStop.stop[self.busStopId].bus = this # Add this bus
				if BusStop.stop[self.busStopId].passenger:
					reactivate(BusStop.stop[self.busStopId])
				else:
					passivate(this) # Wait passengers
			yield hold, self, G.Rnd.expovariate(G.travelRate) # Travel to next stop
			self.busStopId = BusStop.nextId(self.busStopId)
			if self.busStopId == self.startBusStopId: # Full circuit
				Bus.circuitTime.extend(now() - self.startTime)
				self.startTime = now()


class BusStop:
	immediate = 0 # Times that there were a bus before passenger
	notImmediate = 0 # Times that not
	stop = [] # Store all bus stops
	busStopNextId = 0 # Id for bus stops

	def __init__(self):
		self.id = BusStop.busStopNextId
		BusStop.busStopNextId += 1 # Increment for next ID
		self.bus = None # Store one bus
		self.passenger = False # No passenger yet

	def Run(self):
		while 1:
			yield hold, self, G.Rnd.expovariate(G.arrivalRate) # Wait some passengers
			self.passenger = True
			if self.bus:	# There was a bus on the stop
				self.passenger = false
				BusStop.immediate += 1 
				reactivate(self.bus)
				self.bus = None
			else: # No bus, needs to wait
				yield passivate, self
				self.passenger = False # Now there is a bus
				BusStop.notImmediate += 1
				self.bus = None
	def nextId(nowId):
		if nowId >= len(BusStop.stop) - 1:
			return 0
		else:
			return nowId + 1

def simulateBusRoute(nstop, nbus, arrivalrate, travelrate, maxsimtime):
	initialize()
	G.arrivalRate = arrivalrate
	G.travelRate = travelrate
	for I in range(nstop):
		BS = BusStop()
		BusStop.stop.extend(BS)
		activate(BS,BS.Run())
	for I in range(nbus):
		B = Bus()
		activate(B,B.Run())

	simulate(until = maxsimtime)
	print 'average circuit time: ', sum(Bus.circuitTime)/float(len(Bus.circuitTime))
	print 'prop. pass. immed. board:: ', BusStop.immediate/(BusStop.immediate+BusStop.notImmediate)


def main():
	if len(sys.argv) < 5:
		print 'Usage:\n python BusRoute.py nstop nbus arrivalrate travelrate maxsimtime\n nstop: the number of bus stops\n nbus: the number of buses, assumed less than nstop\n arrivalrate: the reciporocal of the mean time between passenger arrivals (per bus stop)\n travelrate: the reciporocal of the mean time needed for a bus to go from one bus stop to the next\n maxsimtime: the amount of time to be simulated'
		sys.exit()

	nstop = int(sys.argv[1])
	nbus = int(sys.argv[2])
	arrivalrate = float(sys.argv[3])
	travelrate = float(sys.argv[4])
	maxsimtime = float(sys.argv[5])

	simulateBusRoute(nstop, nbus, arrivalrate, travelrate, maxsimtime)

if __name__ == '__main__': main()

