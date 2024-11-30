from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score

# Function to calculate metrics based on the test examples
def calculate_metrics(ai_output, expected_words):
    # Construct the lists of expected and actual results
    expected_results = [1 if word in expected_words else 0 for word in ai_output]
    actual_results = [1 if word in ai_output else 0 for word in expected_words]

    # Calculate the confusion matrix
    conf_matrix = confusion_matrix(expected_results, actual_results)

    # Calculate precision, recall, and F1-score
    precision_value = precision_score(expected_results, actual_results)
    recall_value = recall_score(expected_results, actual_results)
    f1 = f1_score(expected_results, actual_results)

    return conf_matrix, precision_value, recall_value, f1

# AI Output
ai_output = ['mixeur batteurs', 'toaster', 'batteur', 'machine à café', 'blenders', 'climatiseur', 'bouilloire',
             'air fryer', 'ventilateurs refroidissement', 'raclette']

# Expected Words
expected_words = ['air fryer', 'machine à café', 'mixeurs', 'batteur', 'mixeur batteurs', 'blenders', 'pétrins',
                  'panini', 'toaster', 'cuiseur vapeur']

# Calculate metrics
conf_matrix, precision, recall, f1 = calculate_metrics(ai_output, expected_words)

# Print results
print("Confusion Matrix:")
print(conf_matrix)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
