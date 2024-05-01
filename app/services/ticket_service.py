from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd
from ..utils.db import add_support_ticket

class TicketService:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.model = LogisticRegression(multi_class="ovr")
        self.load_data()

    def load_data(self):
        data = pd.read_csv("app/customer_support_tickets.csv")
        X = data["Ticket Description"]
        y = data["Ticket Priority"]
        X_features = self.vectorizer.fit_transform(X)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_features, y, test_size=0.2)
        self.model.fit(self.X_train, self.y_train)

    def predict_ticket(self, title,description, email):
        description_features = self.vectorizer.transform([description])
        predicted_priority = self.model.predict(description_features)[0]
        suggested_solution = self.get_suggested_solution(predicted_priority)
        isResolved = False if suggested_solution == "No common resolution found yet." else True
        add_support_ticket(email=email,ticket_title=title, ticket_description=description, ticket_priority=predicted_priority, isResolved=isResolved, resolution=suggested_solution)
        return predicted_priority, suggested_solution

    def get_suggested_solution(self, predicted_priority):
        # Your logic to suggest a solution based on predicted priority
        return "Sample solution"
