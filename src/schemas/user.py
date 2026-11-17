from pydantic import BaseModel , AfterValidator , BeforeValidator
from typing import Annotated

def check_number_format(phone : str):
    translation1 = str.maketrans('۰۱۲۳۴۵۶۷۸۹', '0123456789')
    translation2 = str.maketrans('٠١٢٣٤٥٦٧٨٩' , '0123456789')
    phone = phone.translate(translation1)
    phone=phone.translate(translation2)
    return phone




def check_phone_number(phone_number : str ):
    phone = phone_number.replace(' ' , '')
    if phone:
        if phone.startswith('+98'):
             
             if len(phone) != 13  or  not phone[3:].isdigit():
                 raise ValueError('You mistyped your number.')
             
             if phone[3] != '9' :
                 raise ValueError("You mistyped your number.")
             
             return phone
        
        if phone.startswith('09'):
            if len(phone) != 11 or  not phone.isdigit(): 
                raise ValueError('You mistyped your number.')
            
            return ''.join(['+98' , phone[1:]])
        
        if phone.startswith('9'):
            if len(phone) != 10 or not phone.isdigit() :
                raise ValueError('You mistyped your number.')
            return ''.join(['+98' , phone])

    else:
        raise ValueError('You mistyped your number.')
              


class UserBase(BaseModel):
    phone_number : Annotated[str ,AfterValidator(check_phone_number) , BeforeValidator(check_number_format)]
class UserCreate(UserBase):
    pass 
class UserOtpRequest(UserCreate):
    pass