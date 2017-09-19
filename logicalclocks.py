import threading
import time
messagematrix={}

class process(threading.Thread):
	def __init__(self,pid):
		threading.Thread.__init__(self)
		self.timestamps=[i+1 for i in range(60)]
		self.pid=pid



	def run(self):
		for i in range(1,6):
			if (self.pid,i) in messagematrix:
				self.timestamps[i-1]= max(self.timestamps[messagematrix[(self.pid,i)][1]-1]+1,self.timestamps[i-1])	
			print('event {} of process {} has timestamp {}'.format(i,self.pid,self.timestamps[i-1]))
			time.sleep(2)
processes=[process(i+1) for i in range(4)]
messagematrix[(2,3)]=(1,2)
messagematrix[(3,2)]=(1,3)

for p in processes:
	p.start()