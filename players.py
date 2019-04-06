#a) Write a map-reducer program to find the total count of the players


#get_ipython().run_line_magic('tb', '')
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys  
class MRWordFrequencyCount(MRJob):
	def mapper1(self, _, lines):
		data = lines.split(',')
		players = data[0].strip()
		yield players,None	
	def combiner(self, word, counts):
		
		yield word,None			
		
		
	def reducer1(self, key, counts):

		yield "total players",key
	def reducer2(self, key,word):
		c =0
		# for i in word:
		# 		c+=1	
		
			
		yield key,len(list(word))
	def steps(self):
		return [ MRStep(mapper=self.mapper1,reducer=self.combiner),MRStep(reducer=self.reducer1),MRStep(reducer=self.reducer2)]



if __name__ == '__main__':
    MRWordFrequencyCount.run()






