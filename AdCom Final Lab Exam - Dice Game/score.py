import os
import datetime

class Score:
    def save_scores(username, score, stages):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("matches.txt", "a") as file:
            file.write(f'{username}: Points -- {score}, Wins -- {stages}, Date & Time: {timestamp}\n')

    def load_top_scores():
        try:
            if not os.path.exists("matches.txt"):
                return "No top scores available yet."

            with open("matches.txt", "r") as file:
                top_scores = [line.split(", Date")[0].strip() for line in file]

            if not top_scores:
                return "No top scores available yet."

            top_scores.sort(key=lambda x: int(x.split("Points -- ")[1].split(",")[0]), reverse=True)
            formatted_scores = [f"{i+1}. {score}" for i, score in enumerate(top_scores[:10])]
            return '\n'.join(formatted_scores)
        except Exception as e:
            print(f"Error: {e}")
            return "An error occurred while loading top scores."

