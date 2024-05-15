class UserManager:
    def save_users(username, password):
        try:
            with open('UserData.txt', 'a') as file:
                file.write(f'Username: {username} \t\t Password: {password}\n')
        except FileNotFoundError:
            with open('UserData.txt', 'x') as file:
                file.write(f'Username: {username} \t\t Password: {password}\n')

    def validate_username(username):
        try:
            with open('UserData.txt', 'r') as db:
                for line in db:
                    if username in line.strip():
                        return True
        except FileNotFoundError:
            return False
        return False

    def validate_password(username, password):
        try:
            with open('UserData.txt', 'r') as db:
                for line in db:
                    if f'Username: {username}' in line and f'Password: {password}' in line:
                        return True
        except FileNotFoundError:
            return False
        return False
    
    def ask():
        input('\nPress enter to return to menu.')
        return None




