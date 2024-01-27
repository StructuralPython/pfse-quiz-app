from textual.validation import Validator, ValidationResult
import parse


class EmailValidator(Validator):
    def validate(self, value: str) -> ValidationResult:
        email_parser = parse.parse("{}@{}.{}", value)
        if email_parser is None:
            return self.failure("Please enter a valid email address")
        return self.success()