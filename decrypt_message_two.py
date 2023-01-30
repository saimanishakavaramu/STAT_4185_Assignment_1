encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
start = 1
end = len(encrypted_message) - 2
encrypted_message_list = list(encrypted_message)
while (end - start >= 0):
    encrypted_message_list[start], encrypted_message_list[end] = encrypted_message_list[end], encrypted_message_list[start]
    start += 2
    end -= 2
print(''.join(encrypted_message_list))