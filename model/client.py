#!/usr/bin/env python
from huggingface_hub import AsyncInferenceClient
from settings.config import MODEL, HF_TOKEN

# Initialize the InferenceClient
client = AsyncInferenceClient(
    model=MODEL,
    token=HF_TOKEN,
)