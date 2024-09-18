import hashlib

def sha256_hash(text):
  
    return hashlib.sha256(text.encode( )).hexdigest()

def merkle_tree(part1, part2, part3, part4):
   
    hash1 = sha256_hash(part1)
    hash2 = sha256_hash(part2)
    hash3 = sha256_hash(part3)
    hash4 = sha256_hash(part4)
    print(hash1 , "hash1")
    print (hash2 , "hash2")
    print (hash3 , "hash3")
    print (hash4 , "hash4")

    combined_hash1 = sha256_hash(hash1 + hash2)
    combined_hash2 = sha256_hash(hash3 + hash4)
    print( combined_hash1, " combined_hash1" )
    print( combined_hash2, " combined_hash2" )
  
    merkle_root = sha256_hash(combined_hash1 + combined_hash2)
  

    return merkle_root


part1 = """And now the end is here
And so I face that final curtain
My friend I'll make it clear
I'll state my case, of which I'm certain
I've lived a life that's full
I traveled each and every highway
And more, much more
I did it, I did it my way"""

part2 = """Regrets, I've had a few
But then again too few to mention
I did what I had to do
I saw it through without exemption
I planned each charted course
Each careful step along the byway
And more, much, much more
I did it, I did it my way"""

part3 = """Yes, there were times I'm sure you knew
When I bit off more than I could chew
But through it all, when there was doubt
I ate it up and spit it out
I faced it all and I stood tall and did it my way"""

part4 = """For what is a man, what has he got?
If not himself then he has naught
Not to say the things that he truly feels
And not the words of someone who kneels
Let the record shows I took all the blows and did it my way"""

merkle_root = merkle_tree(part1, part2, part3, part4)
print("Merkle Root:", merkle_root)
