# 1. Hash the following texts using sha256
import hashlib
'''
h1 = 'Hello'
hashlib.sha256(h1.encode()).hexdigest()

h2 = '안녕'
hashlib.sha256(h2.encode()).hexdigest()

h3 = 'Firm A send 1 BTC to Firm B'
hashlib.sha256(h3.encode()).hexdigest()

h4 = 'Firm A send 2 BTC to Firm B'
hashlib.sha256(h4.encode()).hexdigest()
'''

class myBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Firm A sends 1 Coin to Firm B"
t2 = "Firm A sends 2 Coins to Firm B"
t3 = "Firm C sends 3 Coins to Firm D"
t4 = "Firm E sends 5 Coins to Firm D"

block1 = myBlock('firstblock', [t1, t2])
print(block1.block_data)
print(block1.block_hash)

block2 = myBlock(block1.block_hash, [t3, t4])
print(block2.block_data)
print(block2.block_hash)