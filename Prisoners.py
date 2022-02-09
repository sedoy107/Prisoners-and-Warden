import random
	
class Prisoner:
	
	N = 0
	
	def __init__(self):
		self.id = Prisoner.N
		Prisoner.N+=1
		self.isIsolated = False
		self.beenToIsolator = False
		self.isolationCounter = 0
		self.solutionCounter = 0
		self.leader = False
	
	def doSomething(self, currentLanternState):
		if self.leader:
			if not self.beenToIsolator:
				self.solutionCounter += 1
				self.beenToIsolator = True
				print(f"Prisoner leader for the first time in the isolator. Counts: {self.solutionCounter}")
				return True
			if not currentLanternState:
				self.solutionCounter += 1
				print(f"Prisoner leader counts: {self.solutionCounter}")
				return True
			return True
		else:
			if currentLanternState:
				if not self.beenToIsolator:
					self.beenToIsolator = True
					return False
			return currentLanternState
		
	def isolate(self):
		self.isIsolated = True
		self.isolationCounter += 1
	
	def release(self):
		self.isIsolated = False
		
	def checkIfSolved(self):
		return self.solutionCounter == Prisoner.N
		
class Isolator:
	currentPrisoner = None
	lanternState = False
	
	@staticmethod
	def isolate(cell):
		isolatedPrisoner = random.choice(cell)
		isolatedPrisoner.isolate()
		#print(f"Prisoner {isolatedPrisoner.id} is in isolator for the {isolatedPrisoner.isolationCounter} time")
		Isolator.lanternState = isolatedPrisoner.doSomething(Isolator.lanternState)
		isolatedPrisoner.release()
		return isolatedPrisoner
		


# Number of prisoners
numberOfPrisoners = 10
# Declare main cell
mainCell = []
# Init prisoners
for i in range(0,numberOfPrisoners):
	mainCell.append(Prisoner())
	
# Choose the leader
leader = random.choice(mainCell)
leader.leader = True
print (f"Prison leader is prisoner# {leader.id}")


steps = 0
breakoutCount = 20000
while(True):
	steps += 1
	p = Isolator.isolate(mainCell)
	if p.checkIfSolved():
		print(f"For {numberOfPrisoners} prisoners the problem was solved in {steps} steps")
		break
	if steps == breakoutCount:
		print("Not solved")
		break

