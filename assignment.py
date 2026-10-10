results = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 3 != 0:
        results.append(str(num))
print(",".join(results))

char_list = ["C", "O", "D", "I", "N", "G"]
output_string = "".join(char_list).capitalize()
print(output_string)

n = 5
squared_dict = {i: i*i for i in range(1, n + 1)}
print(squared_dict)
