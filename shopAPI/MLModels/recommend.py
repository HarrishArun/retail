# -*- coding: utf-8 -*-
"""Interaction_recommendation (1) (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1le8VUmFmTGpmjk9JL3Kfquk9LHYwk9r5
"""

import numpy as np
import tensorflow as tf
import pandas as pd

# Simulated user-item interaction data (user-product purchases)
num_users = 25
num_products = 15
num_transactions_per_user = 5

# Generate the ratings dataset
ratings = np.random.randint(2, size=(num_users, num_products, num_transactions_per_user))

# Reshape the data for CSV
ratings_reshaped = ratings.reshape(-1, num_transactions_per_user)
user_ids = np.repeat(np.arange(num_users), num_products)
product_ids = np.tile(np.arange(num_products), num_users)

# Create a DataFrame
# df = pd.DataFrame({'User_ID': user_ids, 'Product_ID': product_ids})
# for i in range(num_transactions_per_user):
#     df[f'Transaction_{i + 1}'] = ratings_reshaped[:, i]

# # Save the DataFrame to a CSV file
# csv_filename = 'user_product_transactions_final.csv'
# df.to_csv(csv_filename, index=False)

# print(f'Dataset saved to {csv_filename}')

# Define the model
class MatrixFactorization(tf.Module):
    def __init__(self, num_users, num_products, embedding_dim):
        self.user_embeddings = tf.Variable(np.random.randn(num_users, embedding_dim), trainable=True)
        self.product_embeddings = tf.Variable(np.random.randn(num_products, embedding_dim), trainable=True)

    def __call__(self, user_input, product_input):
        user_embed = tf.nn.embedding_lookup(self.user_embeddings, user_input)
        product_embed = tf.nn.embedding_lookup(self.product_embeddings, product_input)
        # Define the dot product or other interaction function
        predicted_ratings = tf.reduce_sum(tf.multiply(user_embed, product_embed), axis=1)
        return predicted_ratings

# Training parameters
embedding_dim = 10
learning_rate = 0.01
num_epochs = 25

# Instantiate the model
model = MatrixFactorization(num_users, num_products, embedding_dim)

# Define the loss and optimizer
def loss(model, user_input, product_input, true_ratings):
    predicted_ratings = model(user_input, product_input)
    return tf.losses.mean_squared_error(true_ratings, predicted_ratings)

optimizer = tf.optimizers.Adam(learning_rate)

# Training loop
# for epoch in range(num_epochs):
#     for user in range(num_users):
#         for transaction in range(num_transactions_per_user):
#             for product in range(num_products):
#                 user_input = np.array([user])
#                 product_input = np.array([product])
#                 true_rating = np.array([ratings[user, product, transaction]], dtype=np.float32)

#                 with tf.GradientTape() as tape:
#                     current_loss = loss(model, user_input, product_input, true_rating)

#                 gradients = tape.gradient(current_loss, model.trainable_variables)
#                 optimizer.apply_gradients(zip(gradients, model.trainable_variables))

#     if epoch % 10 == 0:
#         print(f"Epoch {epoch}, Loss: {current_loss}")


user_id_to_index = {}
item_id_to_index = {}
for i in range(num_users):
    user_id_to_index[f'User{i}'] = i
for i in range(num_products):
    item_id_to_index[f'Product_{i}'] = i

# Function to get top N recommendations for a user
def get_top_n_recommendations(user_id, model, user_id_to_index, item_id_to_index, N=10):
    # Find the user's integer index
    user_index = user_id_to_index[user_id]

    # Create a list of item indices
    all_item_indices = np.arange(num_products)

    # Filter out items the user has already interacted with in the last transaction
    user_interactions = ratings[user_index, :, -1]
    interacted_items = np.where(user_interactions == 1)[0]
    non_interacted_items = np.setdiff1d(all_item_indices, interacted_items)

    # Get predicted ratings for the non-interacted items
    user_indices = np.array([user_index] * len(non_interacted_items))
    predicted_ratings = model(user_indices, non_interacted_items)

    # Sort the items by predicted rating in descending order
    top_n_indices = np.argsort(predicted_ratings)[::-1][:N]

    # Map item indices back to product IDs
    top_n_product_ids = [f'Product_{item_id}' for item_id in non_interacted_items[top_n_indices]]

    return top_n_product_ids

# import pickle

# # Save the model to a pickle file
# model_filename = 'model.pkl'
# with open(model_filename, 'wb') as file:
#     pickle.dump(model, file)

# print(f'Model saved to {model_filename}')

# Function to simulate user interactions and get recommendations

# Function to simulate user interactions and get recommendations
def simulate_interactions(Transactions,id):
        user_id = 'User'+ str(id)
        if user_id not in user_id_to_index:
            print("User not found. Please enter a valid user ID.")
            return

        # Simulate user's interactions
        user_index = user_id_to_index[user_id]
        user_interactions = ratings[user_index, :, -1]  # Get user's interactions in the last transaction


        # Get top N recommendations for the user
        top_10_recommendations = get_top_n_recommendations(user_id, model, user_id_to_index, item_id_to_index, N=10)

        # Prompt the user for new interactions
        for i in Transactions:          
            new_interactions = i
            if len(new_interactions) != num_products:
                print("Invalid input. Please enter interactions for all products.")
            else:
                new_interactions = np.array([int(i) for i in new_interactions])
                ratings[user_index, :, -1] = new_interactions  # Update user's interactions for the last transaction

        # Recompute and display updated recommendations
        top_10_recommendations = get_top_n_recommendations(user_id, model, user_id_to_index, item_id_to_index, N=10)
        return top_10_recommendations

# Simulate user interactions


# Simulate user interactions




