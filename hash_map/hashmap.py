class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        """
        Compute hash value by summing Unicode values of each character.
        
        Args:
            string: The string to hash
            
        Returns:
            The sum of Unicode (ASCII) values of each character in the string
        """
        return sum(ord(char) for char in string)
    
    def add(self, key, value):
        """
        Add a key-value pair to the hash table.
        
        Args:
            key: The key to hash and use for storage
            value: The value to associate with the key
        """
        hash_value = self.hash(key)
        
        if hash_value not in self.collection:
            self.collection[hash_value] = {}
        
        self.collection[hash_value][key] = value
    
    def remove(self, key):
        """
        Remove a key-value pair from the hash table.
        
        Args:
            key: The key to remove
        """
        hash_value = self.hash(key)
        
        if hash_value in self.collection and key in self.collection[hash_value]:
            del self.collection[hash_value][key]
    
    def lookup(self, key):
        """
        Look up a value in the hash table by key.
        
        Args:
            key: The key to look up
            
        Returns:
            The value associated with the key, or None if the key does not exist
        """
        hash_value = self.hash(key)
        
        if hash_value in self.collection and key in self.collection[hash_value]:
            return self.collection[hash_value][key]
        
        return None
