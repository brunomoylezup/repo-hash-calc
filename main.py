import hashlib

# Read hashes from file
with open('hashes.txt', 'r') as f:
    hashes = [line.strip() for line in f if line.strip()]

# Concatenate all hashes
concatenated = ''.join(hashes)

# (Optional) Hash the concatenated string
final_hash = hashlib.sha256(concatenated.encode('utf-8')).hexdigest()

print(f"Concatenated hash: {final_hash}")