import torch
import torch.nn as nn

class SymptomClassifierLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super().__init__()
        
        # WEEK 3: The Dictionary
        self.embedding = nn.Embedding(num_embeddings=vocab_size, embedding_dim=embedding_dim)
        
        # WEEK 4: The Memory Vault
        self.lstm = nn.LSTM(input_size=embedding_dim, hidden_size=hidden_dim, batch_first=True)
        
        # WEEK 2: The Decision Maker
        self.fc = nn.Linear(in_features=hidden_dim, out_features=1)
        
    def forward(self, text_sequence):
        # 1. Words to Vectors
        embedded = self.embedding(text_sequence)
        print(f"Embedding: {embedded}" )
        
        # 2. Vectors to Memory
        lstm_out, (h_n, c_n) = self.lstm(embedded)
        print(f"Vector Valut: {h_n}")
        
        # 3. Slice the top-floor memory
        final_memory = h_n[-1]
        print(f"final memory: {final_memory}")
        
        # 4. Memory to Final Diagnosis
        prediction = self.fc(final_memory)
        
        return prediction
    


model = SymptomClassifierLSTM(5000, 100, 64)
model.loss.backward()
model.optimizer.step()

dummy_patient = torch.tensor([[42, 15, 880, 102]])

ouput = model(dummy_patient)

print(ouput)