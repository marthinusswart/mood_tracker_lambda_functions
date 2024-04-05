import mood_tracker_api_lambda

def main():
  context = ""
  event = {'mood': 1, 'moodDetail': 'Notes', 'moodDate': '2024-04-01', 'moodTime': '14:00:00', 'moodIntensity': 1}
  
  mood_tracker_api_lambda.lambda_handler(event, context)

if __name__ == "__main__":
  main()