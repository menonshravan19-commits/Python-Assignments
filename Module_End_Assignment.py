# Survey Feedback Analyzer

#  Step 1

feedback_data = {
    'S_No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Ravi', 'Meera', 'Sam', 'Anu', 'Raj', 'Divya', 'Arjun', 'Kiran', 'Leela', 'Nisha'],
    'Feedback': [
        '  Very GOOD Service!!!',
        'poor support, not happy ',
        'GREAT experience! will come again.',
        'okay okay...',
        ' not BAD',
        'Excellent care, excellent staff!',
        'good food and good ambience!',
        'Poor response and poor handling of issue',
        'Satisfied. But could be better.',
        'Good support... quick service.'
    ],
    'Rating': [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2

print("=" * 55)
print("ADD NEW FEEDBACK")
print("=" * 55)

how_many = int(input("How many more feedbacks do you want to add? "))


for i in range(how_many):
    print(f"\nFeedback {i + 1} of {how_many}")

    name = input("Enter name: ")
    feedback = input("Enter feedback: ")

    rating = int(input("Enter rating (1-5): "))
    while rating < 1 or rating > 5:
        print("Rating must be between 1 and 5.")
        rating = int(input("Enter rating (1-5): "))

    # S_No continues from the last existing number (11, 12, 13 ...)
    next_s_no = feedback_data['S_No'][-1] + 1

    feedback_data['S_No'].append(next_s_no)
    feedback_data['Name'].append(name)
    feedback_data['Feedback'].append(feedback)
    feedback_data['Rating'].append(rating)

print(f"\n{how_many} new feedback(s) added successfully.")

# Step 3

def clean_text(text):
    """Remove punctuation, extra spaces, and convert to lowercase."""
    for punctuation in ['.', ',', '!', '?']:
        text = text.replace(punctuation, '')

    # split() with no argument breaks on any run of whitespace and drops
    # the empty pieces, so joining back with a single space fixes double
    # spaces AND leading/trailing spaces in one move
    text = ' '.join(text.split())

    return text.lower()


for i in range(len(feedback_data['Feedback'])):
    feedback_data['Feedback'][i] = clean_text(feedback_data['Feedback'][i])

# Step 4

def count_word_in_feedbacks(word):
    """Return how many feedbacks contain the given word (case-insensitive)."""
    word = word.lower()
    count = 0

    for feedback in feedback_data['Feedback']:
        if word in feedback.lower().split():
            count += 1

    return count


print("\n" + "=" * 55)
print("WORD COUNT INSIGHTS")
print("=" * 55)
print("Feedbacks containing 'good'      :", count_word_in_feedbacks('good'))
print("Feedbacks containing 'poor'      :", count_word_in_feedbacks('poor'))
print("Feedbacks containing 'excellent' :", count_word_in_feedbacks('excellent'))

# Step 5

print("\n" + "=" * 55)
print("FINAL CLEANED FEEDBACK DATA")
print("=" * 55)

for key in feedback_data:
    print(f"{key} : {feedback_data[key]}")

print("\nReadable table view:")
print(f"{'S_No':<6}{'Name':<12}{'Rating':<8}Feedback")
print("-" * 70)
for i in range(len(feedback_data['S_No'])):
    print(f"{feedback_data['S_No'][i]:<6}"
          f"{feedback_data['Name'][i]:<12}"
          f"{feedback_data['Rating'][i]:<8}"
          f"{feedback_data['Feedback'][i]}")

# --- Average rating ---
average_rating = sum(feedback_data['Rating']) / len(feedback_data['Rating'])
print(f"\nAverage Rating : {average_rating:.2f}")

# --- Longest feedback by word count ---
longest_index = 0
max_word_count = 0

for i in range(len(feedback_data['Feedback'])):
    word_count = len(feedback_data['Feedback'][i].split())
    if word_count > max_word_count:
        max_word_count = word_count
        longest_index = i

print("\nLongest Feedback (by word count):")
print(f"  Name     : {feedback_data['Name'][longest_index]}")
print(f"  Feedback : {feedback_data['Feedback'][longest_index]}")
print(f"  Words    : {max_word_count}")

# --- Unique words ---
unique_words = set()

for feedback in feedback_data['Feedback']:
    unique_words.update(feedback.split())

print(f"\nUnique Words Used ({len(unique_words)} total):")
print(sorted(unique_words))


# Optional (Sorting Feedbacks by Rating)

print("\n" + "=" * 55)
print("FEEDBACKS SORTED BY RATING (HIGH TO LOW)")
print("=" * 55)

combined = list(zip(feedback_data['Rating'],
                    feedback_data['Name'],
                    feedback_data['Feedback']))

sorted_feedbacks = sorted(combined, key=lambda item: item[0], reverse=True)

print(f"{'Rating':<8}{'Name':<12}Feedback")
print("-" * 70)
for rating, name, feedback in sorted_feedbacks:
    print(f"{rating:<8}{name:<12}{feedback}")
