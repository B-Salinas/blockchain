# create a block class
  # contains previousHash and TransactionList parameters
  # we also create a unique hash (signature) per block

  # create getPreviousHash, getTransactionList, and getBlockHash getter functions

# create a blockchain (an array containing instances of blocks)

# -------------------------------------------------------------------------------------------------
from Block import Block # class from Block.py

blockchain = []

genesis_block = Block("Chancellor on Brink of Second Bailout for Banks", [" ? -> 5 BTC -> Self"])
adam_block = Block(genesis_block.block_hash, [" Creator -> 2 BTC -> Self"])
lilith_block = Block(genesis_block.block_hash, [" Creator -> 2 BTC -> Self"])
