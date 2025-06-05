import matplotlib.pyplot as plt  # Import the matplotlib library for plotting

# Function to get user input for subjects and scores
def get_user_data():
    subjects = []  # Initialize an empty list to store subjects
    scores = []  # Initialize an empty list to store scores
    number_of_subjects = int(input("Enter number of subjects: "))  # Get the number of subjects from the user
    for i in range(number_of_subjects):  # Loop over the number of subjects
        subject = input(f"Enter subject {i+1}: ")  # Get the name of each subject from the user
        score = int(input(f"Enter score for {subject}: "))  # Get the score for each subject from the user
        subjects.append(subject)  # Append the subject to the subjects list
        scores.append(score)  # Append the score to the scores list
    return subjects, scores  # Return the subjects and scores lists

# Function to plot the data and print the highest and average scores
def plot_data(subjects, scores):
    plt.bar(subjects, scores, color='skyblue')  # Create a bar chart with subjects on the x-axis and scores on the y-axis
    plt.title('Exam Scores by Subject')  # Set the title of the chart
    plt.xlabel('Subjects')  # Set the label for the x-axis
    plt.ylabel('Scores')  # Set the label for the y-axis

    highest_score = max(scores)  # Find the highest score
    best_subject = subjects[scores.index(highest_score)]  # Find the subject corresponding to the highest score
    average_score = sum(scores) / len(scores)  # Calculate the average score

    print(f"Highest score: {highest_score} in {best_subject}")  # Print the highest score and corresponding subject
    print(f"Average score: {average_score:.2f}")  # Print the average score with two decimal places

    # Determine performance based on average score
    if average_score >= 90:
        print("Excellent performance!")  # Print if the average score is 90 or above
    elif average_score >= 75:
        print("Good performance, needs improvement.")  # Print if the average score is between 75 and 89
    else:
        print("Needs more effort.")  # Print if the average score is below 75

    plt.show()  # Display the bar chart

# Getting user data and plotting
subjects, scores = get_user_data()  # Call the function to get user data and store the returned subjects and scores
plot_data(subjects, scores)  # Call the function to plot the data and print the highest and average scores


