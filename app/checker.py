from db_init import collection


def find_match_forms(validated_data: dict) -> list:
    """Определяет совпадения полей запроса с полями шаблонов форм по их
    названию и типу. Возвращает список с именами совпавших форм.

    Аргументы:
        validated_data (dict): Валидированные данные запроса.

    Возвращает:
        list: Имена совпавших форм.
    """

    match_forms = []
    forms = collection.find({}, {"_id": 0})

    for form in forms:
        if all(
            field_name in validated_data
            and (
                form[field_name] == validated_data[field_name]
                or form[field_name] == 'string'
            )
            for field_name in form.keys()
            if field_name != 'name'  # пропускает имена шаблонов форм
        ):
            match_forms.append(form['name'])
    return sorted(match_forms)
