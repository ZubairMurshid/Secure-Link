# 1. Use a lightweight Python image
FROM python:3.10-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy only the requirements first (Optimizes build cache)
COPY requirements.txt .

# 4. Install dependencies AND the spaCy model (Crucial for Presidio)
RUN pip install --no-cache-dir -r requirements.txt && \
    python -m spacy download en_core_web_sm  # Use python instead of py

# 5. Copy the rest of the code
COPY . .

# 6. Expose the port FastAPI runs on
EXPOSE 8000

# 7. Start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]