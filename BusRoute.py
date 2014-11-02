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

def simulateBusRoute(nstop, nbus, arrivalrate, travelrate, maxsimtime):

	# Our code comes here

def main():
	if len(sys.argv) < 5:
		print 'Usage:\n python BusRoute.py nstop nbus arrivalrate travelrate maxsimtime\n nstop: the number of bus stops\n nbus: the number of buses, assumed less than nstop\n arrivalrate: the reciporocal of the mean time between passenger arrivals (per bus stop)\n travelrate: the reciporocal of the mean time needed for a bus to go from one bus stop to the next\n maxsimtime: the amount of time to be simulated'
		sys.exit()

	nstop = sys.argv[1]
	nbus = sys.argv[2]
	arrivalrate = sys.argv[3]
	travelrate = sys.argv[4]
	maxsimtime = sys.argv[5]

	simulateBusRoute(nstop, nbus, arrivalrate, travelrate, maxsimtime)

if __name__ == '__main__': main()

