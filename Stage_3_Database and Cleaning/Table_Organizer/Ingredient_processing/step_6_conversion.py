import hashlib
    
def create_hash(found_modifier, summary_modifier,empty_text):
    hash_hold = ""

    if empty_text or len(found_modifier) == 0:
        found_modifier = summary_modifier

    for f in found_modifier:
        hash_hold+=f    
    hash_obj = hashlib.sha256(hash_hold.encode('utf-8'))
    hex_hash = hash_obj.hexdigest()
    hex_hash = str(hex_hash[:4])
    return hex_hash
