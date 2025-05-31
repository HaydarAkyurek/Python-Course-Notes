# 🔧 HOW TO SET UP FIREBASE FOR THIS SCRIPT:
# 1. Go to https://console.firebase.google.com/
# 2. Create a new project or use an existing one.
# 3. Click on the gear icon (Project Settings) > General.
# 4. Scroll down to "Your apps" and click "Web" to register a new web app.
# 5. Firebase will generate your configuration details (apiKey, authDomain, etc.).
# 6. Copy those values and paste them into the firebaseConfig dictionary below.
# 7. Enable Email/Password Authentication:
#    - Go to Authentication > Sign-in method > Enable "Email/Password".


import pyrebase

# 🔐 Firebase configuration (replace the empty strings with your actual Firebase credentials)
firebaseConfig = {
    "apiKey": "<your-api-key>",
    "authDomain": "<your-auth-domain>",
    "projectId": "<your-project-id>",
    "storageBucket": "<your-storage-bucket>",
    "messagingSenderId": "<your-messaging-sender-id>",
    "appId": "<your-app-id>",
    "databaseURL": "<your-database-url>"
}

# 🚀 Initialize the Firebase application
firebase = pyrebase.initialize_app(firebaseConfig)

# 🔐 Get the authentication service from Firebase
auth = firebase.auth()

# 🧾 Function to create a new user account
def sign_up():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        # Attempt to create a new user with the given email and password
        auth.create_user_with_email_and_password(email, password)
        print("✅ User account created successfully.")
    except Exception as e:
        # Print error details if account creation fails
        print("❌ Failed to create user account:", e)

# 🔓 Function to log in an existing user
def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    try:
        # Attempt to sign in the user
        user = auth.sign_in_with_email_and_password(email, password)
        
        # Print user data and account information
        print("✅ Login successful!")
        print("User data:", user)
        print("Account info:", auth.get_account_info(user["idToken"]))
    except Exception as e:
        # Print error details if login fails
        print("❌ Invalid email or password.")
        print("Error details:", e)

# 📌 Uncomment this line to create a new user
# sign_up()

# 📌 Log in an existing user
login()
