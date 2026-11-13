
contacts = [
    {
        "name": "Dr. Ravi",
        "phone": ["+91 98400 12345"],
        "email": ["ravi@gmail.com"]
    },
    {
        "name": "ravi kumar",
        "phone": ["9840012345"],
        "email": ["ravi@gmail.com", "ravi2@gmail.com"]
    },
    {
        "name": "Anu",
        "phone": ["+91 98765 43210"],
        "email": ["anu@gmail.com"]
    },
    {
        "name": "Kumar",
        "phone": ["9876543210"],
        "email": ["kumar@gmail.com"]
    },
    {
        "name": "Arun",
        "phone": [],
        "email": []
    }
]

merged = {}

for contact in contacts:

    phones = {
        "".join(ch for ch in p if ch.isdigit())
        for p in contact["phone"]
    }

    phones = {
        p[2:] if len(p) == 12 and p.startswith("91") else p
        for p in phones
    }

    emails = set(contact["email"])

    existing = None

    for phone in phones:
        if phone in merged:
            existing = merged[phone]
            break

    if existing is None:
        existing = {
            "name": contact["name"],
            "phones": set(),
            "emails": set()
        }

    existing["phones"].update(phones)
    existing["emails"].update(emails)

    for phone in existing["phones"]:
        merged[phone] = existing

unique_contacts = []
seen = set()

for contact in merged.values():
    if id(contact) not in seen:
        unique_contacts.append(contact)
        seen.add(id(contact))

print("Merged Contacts:")

for contact in unique_contacts:
    print("Name:", contact["name"])
    print("Phone:", sorted(contact["phones"]))
    print("Email:", sorted(contact["emails"]))
    print()

print("Contacts without phone numbers:")

for contact in contacts:
    if not contact["phone"]:
        print(contact["name"])
