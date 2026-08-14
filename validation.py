from abc import ABC, abstractmethod
import sys

class Validator(ABC):
    """Abstract base class for all validators"""
    
    @abstractmethod
    def validate(self, value):
        pass
    
    @abstractmethod
    def get_error_message(self):
        pass

class NameValidator(Validator):
    """Validates user name input"""
    
    def validate(self, name):
        cleaned = name.strip()
        
        if not cleaned:
            return False, None
        
        if len(cleaned) < 2:
            return False, None
            
        if not all(char.isalpha() or char in " -'" for char in cleaned):
            return False, None
            
        return True, cleaned
    
    def get_error_message(self):
        return "Name must be at least 2 characters and contain only letters, spaces, hyphens, and apostrophes"

class AgeValidator(Validator):
    """Validates age input"""
    
    def __init__(self, min_age=18, max_age=150):
        self.min_age = min_age
        self.max_age = max_age
    
    def validate(self, age_str):
        try:
            age = int(age_str)
            
            if age < 0:
                return False, None
                
            if age > self.max_age:
                return False, None
                
            return True, age
            
        except ValueError:
            return False, None
    
    def get_error_message(self):
        return f"Age must be a whole number between 0 and {self.max_age}"

class RegistrationSystem:
    """Main registration system handler"""
    
    def __init__(self, max_attempts=5):
        self.max_attempts = max_attempts
        self.name_validator = NameValidator()
        self.age_validator = AgeValidator(min_age=18, max_age=150)
        self.attempts = 0
    
    def get_input_with_validation(self, prompt, validator):
        """Get input with validation"""
        while True:
            value = input(prompt)
            is_valid, validated_data = validator.validate(value)
            
            if is_valid:
                return validated_data
                
            print(f"❌ Error: {validator.get_error_message()}")
            print("   Please try again.\n")
    
    def process_registration(self):
        """Process a single registration attempt"""
        print("\n" + "-" * 50)
        
        # Get validated inputs
        name = self.get_input_with_validation(
            "Enter Full Name: ",
            self.name_validator
        )
        
        age = self.get_input_with_validation(
            "Enter Age: ",
            self.age_validator
        )
        
        # Check eligibility
        if age >= 18:
            print(f"\n✅ {name.upper()}, you are ELIGIBLE for registration!")
            print(f"   Age: {age} years")
            return True
        else:
            years_short = 18 - age
            print(f"\n❌ {name.upper()}, you are NOT eligible for registration")
            print(f"   Your age: {age} years (Minimum required: 18)")
            print(f"   You need to wait {years_short} more year(s)")
            return False
    
    def run(self):
        """Main program loop"""
        print("=" * 50)
        print("    WELCOME TO REGISTRATION SYSTEM")
        print("=" * 50)
        print("\nMinimum age required: 18 years")
        print(f"Maximum attempts: {self.max_attempts}\n")
        
        while self.attempts < self.max_attempts:
            self.attempts += 1
            print(f"\n--- Attempt {self.attempts} of {self.max_attempts} ---")
            
            if self.process_registration():
                print("\n🎉 Registration successful! Welcome aboard.")
                return
            
            if self.attempts < self.max_attempts:
                while True:
                    choice = input("\nDo you want to try again? (yes/no): ").lower().strip()
                    if choice in ['yes', 'y']:
                        break
                    elif choice in ['no', 'n']:
                        print("\nThank you for your interest. Goodbye!")
                        sys.exit(0)
                    else:
                        print("Please enter 'yes' or 'no'")
        
        print(f"\n❌ Maximum attempts ({self.max_attempts}) exceeded.")
        print("Please contact support for assistance.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        system = RegistrationSystem(max_attempts=3)
        system.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
        sys.exit(0)