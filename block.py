import hashlib

def hash(to_be_hashed):
  return hashlib.sha256(to_be_hashed.encode()).hexdigest()

class Block:
  ''' The original Gensis Block '''
  def __init__(self, previous_hash, transactions):
    self.previous_hash = previous_hash
    self.transactions = transactions
    my_hash_string = "".join(transactions) + previous_hash
    self.block_hash = hash(my_hash_string)

