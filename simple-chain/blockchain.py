"""
 >>> block_chain = BlockChain()
 >>> block_chain.new_transaction("Satoshi", "Nakamoto", '5 BTC')
 >>> block_chain.new_block(12345)
 >>> block_chain.new_transaction("Game", "Shop", '1 BTC')
 >>> block_chain.new_block(6789)
 >>> print(block_chain.chain)
"""
import hashlib
import json
from time import time


# https://medium.com/coinmonks/python-tutorial-build-a-blockchain-713c706f6531

class BlockChain:
    """
        [{
        	'index': 1,
        	'timestamp': 1613683677.249353,
        	'transactions': [],
        	'proof': 100,
        	'previous_hash': 'Fist block'
        }, {
        	'index': 2,
        	'timestamp': 1613683677.249457,
        	'transactions': [{
        		'sender': 'Satoshi',
        		'recipient': 'Nakamoto',
        		'amount': '5 BTC'
        	}],
        	'proof': 12345,
        	'previous_hash': 'baef48d2e25be7bee6cf3d85f38a37f4ae22b0145c41c8e1bd62f46b378e9934'
        }, {
        	'index': 3,
        	'timestamp': 1613683677.249598,
        	'transactions': [{
        		'sender': 'Game',
        		'recipient': 'Shop',
        		'amount': '1 BTC'
        	}],
        	'proof': 6789,
        	'previous_hash': '3057ea40e2184339a1b4ba1a0b329aececc824be95b2cd200bcdcbbf1148a7f7'
        }]
    """
    
    def __init__(self):
        self.chain = []
        self.pending_trasactions = []
        
        self.new_block(previous_hash='Fist block', proof=100)
    
    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_trasactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        self.pending_trasactions = []
        self.chain.append(block)
        # return block
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'sender': sender, 
            'recipient': recipient,
            'amount': amount
        }
        
        self.pending_trasactions.append(transaction)
        # return self.last_block['index'] + 1
        
    def hash(self, block):
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()
        
        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()
        
        return hex_hash