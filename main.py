print("Pitsa yetkazib berish hizmati!")
size = input("Qanday kattalikdagi pitsa xohlaysiz? S/M/L: ").upper()
add_pepperoni = input("pepperonini qo'shishni xohlaysizmi? (kichik pitsa uchun $2 o'rtacha va katta pitsa uchun $3) yes/no: ")
extra_cheese = input("extra cheeseni qo'shishni xohlaysizmi? (hamma pitsa uchun $1) yes/no: ")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
elif size == "L":
  bill += 25
else:
  print("Siz xohlagan pitsa topilmadi")

if add_pepperoni == "yes":
  if size == "S":
    bill += 2
  else:
    bill += 3
if extra_cheese == "yes":
  bill += 1

print(f"Sizning pitsangiz: ${bill}")
