

class Entry():

	def __init__(self, key, value, removed = False):
		self.key = key
		self.value = value
		self.removed = removed

	def isremoved(self):
		return self.removed

	def remove(self):
		self.removed = True

	
	def setkey(self, key):
		self.key = key

	def getkey(self):
		return self.key

	
	def setvalue(self, value):
		self.value = value

	def getvalue(self):
		return self.value

	def __eq__(self, other):
		
		if not isinstance(other, Entry):
			return False
		
 	 	return (self.key == other.key 
 	 		and self.value == other.value
 	 		and self.removed == other.removed)

 	def __ne__(self, other):
	 	return self.__eq__(other)


	def __hash__(self):
		if not self.removed:
			return (hash(self.key) * hash(self.value))
		else:
			return 0



class HashMap():

	CAPACITY_DEFAULT = 10
	THRESHOLD = 0.67

	def __init__(self, capacity = CAPACITY_DEFAULT):
		self.capacity = capacity
		self.mapping = [None for _ in range(capacity)]
		self.size = 0

	def getsize(self):
		return self.size

	def isempty(self):
		return (self.size is 0)


	def put(self, key, value):

		if not key or not value:
			raise ValueError("Key and Value must be defined")

		alpha = float(self.size + 1) / float(self.capacity)

		if alpha >= self.THRESHOLD:
			data = self.mapping
			self.capacity *= 2
			self.size = 0
			self.mapping = [None for _ in range(int(self.capacity))]

			for entry in data:
				if entry and not entry.isremoved():
					k = entry.getkey()
					v = entry.getvalue()
					self.put(k, v)


		index = hash(key) % self.capacity
		data = self.mapping

		startingIndex = index
		loopedAround = False
		done = False


		oldValue = None

		while not done:

			if not data[index]:
				data[index] = Entry(key, value)
				self.size += 1
				done = True

			elif data[index].getkey() == key:

				# Increment the size only if the previous entry was
				# removed. If entry was not already removed, return the 
				# value of the existing entry
				if data[index].isremoved():
					self.size += 1
				else:
					oldValue = data[index].getvalue()

				# Replace existing entry with new key-value entry
				data[index] = Entry(key, value)
				done = True

			elif data[index].isremoved() and loopedAround:
					data[index] = Entry(key, value)
					self.size += 1
					done = True

			
			index = (index + 1) % self.capacity
			if index is startingIndex:
				loopedAround = True


















