Virus Simulation
----------------
Author: Karan Tamhane
Course: Introduction to Computer Science and Programming
School: MITx (edX)
Problem Set: 8

Summary:
	Runs a simulation to estimate the growth of virus population in a patient with or without the use of drugs.

Source code: virus_simulation.py

Modules imported:
    numpy, random, pylab

Usage:
	
	Program must be run in a python shell.

	Call simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials) to run simulation without the introduction of drugs in patient.

	numViruses => number of viruses present in a patient initially (int > 0)
    maxPop => maximum virus population for patient (int > 0)
    maxBirthProb => Maximum reproduction probability of virus (0 <= float <= 1)        
    clearProb => Maximum clearance probability of virus (0 <= float <= 1)
    numTrials => number of simulation runs to execute (int > 0)

    Call simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials) to run simulation with usage of drugs on patient.

    numViruses => number of viruses present in a patient initially (int > 0)
    maxPop => maximum virus population for patient (int > 0)
    maxBirthProb => Maximum reproduction probability of virus (0 <= float <= 1)        
    clearProb => Maximum clearance probability of virus (0 <= float <= 1)
    resistances => dictionary specifying resistance of viruses to drugs (dict of type {string:boolean})
    	E.g. - If a virus is resistant to a drug 'guttagonol' then 
    	resistances = {'guttagonol':True}
    mutProb => Probability that a virus offspring mutates to reverse its resistances to drugs i.e. if mutProb = 0.05, then 95% times a virus offspring will inherit its parents resistances and 5% times it will have opposite resistances (0 <= float <= 1)
    numTrials => number of simulation runs to execute (int > 0)