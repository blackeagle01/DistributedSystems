import time
messages={}
messages[(1,2)]=(0,2)
messages[(2,3)]=(0,4)
times={}

class Process(object):
	def __init__(self,pid,events):
		self.pid=pid
		self.events=events
		self.timestamps=[[0 for i in range(5)] for i in range(self.events)]
		for i,j in enumerate(self.timestamps):
				self.timestamps[i][self.pid]=i+1

def run():
	for (i,j) in messages:
		for k,l in enumerate(times[i][j]):
				times[i][j][k]=max(times[i][j][k],times[messages[i,j][0]][messages[i,j][1]][k])





p=[Process(i,5) for i in range(5)]
for i,j in enumerate(p):
	times[i]=j.timestamps
run()
for i in times:
	print('timestamps for process {} : {}'.format(i,times[i]))
	time.sleep(1)


