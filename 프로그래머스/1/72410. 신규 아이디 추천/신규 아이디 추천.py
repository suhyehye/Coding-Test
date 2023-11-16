import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_\.]', '', new_id)
    new_id = re.sub(r'\.+', '.', new_id)
    new_id = new_id.strip('.')
    if not new_id:
        new_id = 'aaa'
    new_id = new_id[:15]
    new_id = new_id.strip('.')
    if len(new_id) <= 2:
        x = new_id[-1]
        new_id = new_id + x * (3-len(new_id))
    return new_id