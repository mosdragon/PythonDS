from hashmap import HashMap
import unittest
import random

random.seed(0)

class HashMapTester(unittest.TestCase):

	def test_init(self):
		hmap = HashMap()
		self.assertEquals(hmap.capacity, HashMap.CAPACITY_DEFAULT)
		
		self.assertEquals(hmap.size, 0)
		self.assertEquals(hmap.getsize(), 0)

		self.assertTrue(hmap.isempty())
		self.assertEquals(hmap.mapping, [None for _ in range(HashMap.CAPACITY_DEFAULT)])



		start_capacity = random.randint(0, 100)
		hmap = HashMap(start_capacity)
		self.assertEquals(hmap.capacity, start_capacity)
		
		self.assertEquals(hmap.getsize(), 0)
		self.assertEquals(hmap.size, 0)

		self.assertTrue(hmap.isempty())
		self.assertEquals(hmap.mapping, [None for _ in range(start_capacity)])


	def test_put(self):
		hmap = HashMap()
		keys = [(x + 1) for x in range(HashMap.CAPACITY_DEFAULT * 2)]
		vals = [key ** 3 for key in keys]

		threshold = HashMap.THRESHOLD
		size = 0

		# Stop just before the hashmap needs to be resized
		while float(size + 1) / float(hmap.capacity) < threshold:
			hmap.put(keys[size], vals[size])
			size += 1


		self.assertEquals(hmap.size, size)
		self.assertEquals(hmap.capacity, HashMap.CAPACITY_DEFAULT)
		self.assertEquals(len(hmap.mapping), HashMap.CAPACITY_DEFAULT)

		old_capacity = hmap.capacity
		# Will first resize itself
		# Then it will stop before the next resize
		while float(size + 1) / float(old_capacity * 2) < threshold:
			hmap.put(keys[size], vals[size])
			size += 1

		self.assertEquals(hmap.size, size)
		self.assertEquals(hmap.capacity, HashMap.CAPACITY_DEFAULT * 2)
		self.assertEquals(len(hmap.mapping), HashMap.CAPACITY_DEFAULT * 2)

		keys_size = len(keys)

		# Finish adding everything
		while size < keys_size:
			hmap.put(keys[size], vals[size])
			size += 1

		self.assertEquals(hmap.size, size)
		self.assertEquals(hmap.capacity, HashMap.CAPACITY_DEFAULT * 4)
		self.assertEquals(len(hmap.mapping), HashMap.CAPACITY_DEFAULT * 4)




unittest.main()