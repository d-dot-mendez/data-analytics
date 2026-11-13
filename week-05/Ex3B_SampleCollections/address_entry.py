contact_info = {
    "address" : "123 Baker's Road",
    "city"    : "Paris",
    "state"   : "Kentucky",
    "zip"     : "18748"
} 

#print(contact_info ["name"], contact_info ["address"], contact_info ["city"],\
#      contact_info ["state"], contact_info ["zip"])
    
full_name = {
    "first name" : "Marinette",
    "last name"  : "Dupain-Cheng"
}

full_name.update({
    "honorific" : "Mrs."
})

contact_info.update(full_name) 

print(contact_info ["first name"], contact_info ["last name"],  contact_info ["address"], contact_info ["city"],\
      contact_info ["state"], contact_info ["zip"])