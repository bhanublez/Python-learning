def groups_per_user(group_dictionary):
    user_groups = {}
    for group, users in group_dictionary.items():    
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

print(groups_per_user({
    "local": ["admin", "userA"],
    "public": ["admin", "userB"],
    "administrator": ["admin"]
}))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
new_item=[("tie",["green","yellow"]),("jeans",["grey"])]
wardrobe.update(dict(new_item))
print(wardrobe)
