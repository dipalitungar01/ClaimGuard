from app.utils.password import hash_password
from app.utils.password import verify_password


password = "mypassword123"

hashed = hash_password(password)

print("Password:", password)
print("Hashed:", hashed)

print(
    "Correct:",
    verify_password(password, hashed)
)

print(
    "Wrong:",
    verify_password("wrongpassword", hashed)
)
