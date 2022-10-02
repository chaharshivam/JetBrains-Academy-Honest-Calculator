text_list = input().split()
mixed_case_text = list()
mixed_case_text.append(text_list[0])
for word in text_list[1:]:
    mixed_case_text.append(word.title())
print("".join(mixed_case_text))
