current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user6', 'user2']
for new_user in new_users:
    if new_user in current_users:
        print("Need to enter a new username.")
    else:
        print(f"username {new_user} is available.")