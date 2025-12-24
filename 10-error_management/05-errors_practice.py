#Customized Errors in Python
class InvalidAgeError(Exception):
    """Custom exception for invalid age values."""
    def __init__(self, age, message="Age must be a over or equal to 18 integer."):
        self.age = age
        self.message = message
        super().__init__(self.message) #Call the base class(Exception) constructor

class InvalidEmail(Exception):
    """Custom exception for invalid email values."""
    def __init__(self, email, message="Email must be a valid email address."):
        self.email = email
        self.message = message
        super().__init__(self.message) #Call the base class(Exception) constructor
def validate_email(email):
    if "@" not in email or "." not in email.split("@")[-1]:
        raise InvalidEmail(email,"Correo electrónico inválido.")
    return True

def register_user(name, age, email):
    validate_email(email)
    if age < 18:
        raise InvalidAgeError(age) #corta el proceso y lanza la excepción
    return f"User {name} registered with age {age}"

try:
   # print(register_user("Alice", 20))  # Valid age
     print(register_user("Bob", 20, "bob@examplecom"))    # Invalid age, will raise exception
except InvalidAgeError as e:
    print(f"Registration failed: {e.message} You provided age: {e.age}")    
    
except InvalidEmail as e:
    print(f"Registration failed: {e.message} You provided email: {e.email}")