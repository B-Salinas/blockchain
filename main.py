# create a block class
  # contains previousHash and TransactionList parameters
  # we also create a unique hash (signature) per block

  # create getPreviousHash, getTransactionList, and getBlockHash getter functions

# create a blockchain (an array containing instances of blocks)

# -------------------------------------------------------------------------------------------------

import hashlib

blockchain = []

hash = hashlib.sha256("secret message goes here".encode()).hexdigest()


