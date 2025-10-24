import re
from exceptions import ValidationError

def validate_car_number(car_id):
    allowed_letters = "АВЕКМНОРСТУХ"  # буквы, использующиеся в российских номерах

    pattern = rf'^([{allowed_letters}])(\d{{3}})([{allowed_letters}]{{2}})(\d{{2,3}})$'

    match = re.match(pattern, car_id)
    if match:
        number_part = car_id[:-2]
        region_part = car_id[-2:]
        if region_part.isdigit():
            print(f"Номер {number_part} валиден. Регион: {region_part}.")
            return number_part, region_part
        else:
            raise ValidationError("Ошибка валидации")
    else:
        raise ValidationError("Ошибка валидации")

try:
    validate_car_number('А222ВС96')
except ValidationError as e:
    print(e)