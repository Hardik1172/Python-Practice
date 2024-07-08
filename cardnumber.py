card_no = input('enter the card no')

last_digit = card_no[15:]

stars = '*' * 4 + ''

final_card_no = stars * 3 + last_digit

print(final_card_no)