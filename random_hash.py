import hashlib
import random
import string

def generate_random_hash():
    """HASH"""
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
    hash_object = hashlib.sha256(random_string.encode())
    return hash_object.hexdigest()[:32]

def find_hash_with_two_zeros():
    
    attempts = 0
    max_attempts = 1000
    
    print("Searching for Hash starting with '00'...")
    
    for i in range(max_attempts):
        attempts += 1
        current_hash = generate_random_hash()
        
        if current_hash.startswith('00'):
            print(f"\nHash found after {attempts} attempts.")
            print(f"Hash: {current_hash}")
            return True
    
    print(f"\nDidn't found the Hash in {max_attempts} attempts.")
    return False

if __name__ == "__main__":
    success = find_hash_with_two_zeros()
    exit(0 if success else 1)
