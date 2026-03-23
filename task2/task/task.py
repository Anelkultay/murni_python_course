```python
# 1. Indoor Voice
# START
# Ask the user to enter text
# Store the text in a variable
# Convert the text to lowercase
# Print the lowercase text
# END

def make_lowercase(text):
    result = text.lower()
    return result


# 2. Playback Speed
# START
# Ask the user to enter text
# Store the text in a variable
# Replace every space in the text with "..."
# Print the new text
# END

def change_playback_speed(text):
    result = text.replace(" ", "...")
    return result


text1 = input("Enter text for Indoor Voice: ")
text2 = input("Enter text for Playback Speed: ")

lowercase_text = make_lowercase(text1)
playback_text = change_playback_speed(text2)

print(lowercase_text)
print(playback_text)
```
