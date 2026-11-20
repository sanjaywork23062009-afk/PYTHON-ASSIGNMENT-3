import re
import time

def normalize_number(phone):
    digits = re.sub(r'\D', '', phone)
    if len(digits) > 10:
        digits = digits[-10:]
    return digits

def merge_contacts(contacts_list):
    merged = {}
    for contact in contacts_list:
        name = contact.get("name", "").strip().title()
        raw_numbers = contact.get("numbers", [])
        emails = contact.get("emails", [])
        
        normalized_nums = [normalize_number(n) for n in raw_numbers if normalize_number(n)]
        
        if not normalized_nums:
            continue
            
        primary_key = normalized_nums[0]
        
        if primary_key not in merged:
            merged[primary_key] = {
                "name": name,
                "numbers": set(raw_numbers),
                "emails": set(emails)
            }
        else:
            if name and not merged[primary_key]["name"]:
                merged[primary_key]["name"] = name
            merged[primary_key]["numbers"].update(raw_numbers)
            merged[primary_key]["emails"].update(emails)
            
    result = []
    for key, data in merged.items():
        result.append({
            "name": data["name"],
            "numbers": list(data["numbers"]),
            "emails": list(data["emails"])
        })
    return result

if __name__ == "__main__":
    sample_contacts = [
        {"name": "Dr. Ravi", "numbers": ["+91 98400 12345"], "emails": ["ravi@example.com"]},
        {"name": "ravi kumar", "numbers": ["9840012345"], "emails": ["ravi.kumar@example.com"]},
        {"name": "Priya", "numbers": ["9840098400"], "emails": ["priya@example.com"]}
    ]
    
    print("Merged Contacts:")
    for c in merge_contacts(sample_contacts):
        print(c)

    for size in [1000, 100000]:
        large_contacts = [
            {"name": f"User {i}", "numbers": [f"98400{i:05d}"], "emails": [f"user{i}@example.com"]}
            for i in range(size)
        ]
        start = time.time()
        merge_contacts(large_contacts)
        print(f"Time for {size} contacts: {time.time() - start:.6f} seconds")
