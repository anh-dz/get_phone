import phonenumbers as np
from phonenumbers import (format_number, PhoneNumberFormat,
						 geocoder, carrier)

PHONE = "+85388027188"
phone_number = np.parse(PHONE)
phone_format = format_number(phone_number, PhoneNumberFormat.NATIONAL)
country = geocoder.description_for_number(phone_number, 'en')
service = carrier.name_for_number(phone_number, 'en')
print(f"Phone Format: {phone_format}")
print(f"Country: {country}")
print(f"Service: {service}")