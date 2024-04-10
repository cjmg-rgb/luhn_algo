def verify_card_number(card_number):
    text_translation = str.maketrans({"-": "", " ": ""})
    translated_text = card_number.translate(text_translation)
    translated_text = translated_text.lower()

    mult_by_1 = translated_text[1::2]
    mult_by_2 = translated_text[::2]

    total = 0

    for num in mult_by_1:
        total += int(num)

    for num in mult_by_2:
        multiplied_num = str(int(num) * 2)
        if len(multiplied_num) > 1:
            total += int(multiplied_num[0]) + int(multiplied_num[1])
        else:
            total += int(multiplied_num)

    if total % 10 == 0: return True

    return True if int(str(total)[0]) + int(str(total)[1]) == 0 else False


def main():
    card_number = "4111-1111-4555-1142"

    if verify_card_number(card_number):
        print("VALID!")
    else:
        print("INVALID!")


if __name__ == "__main__":
    main()