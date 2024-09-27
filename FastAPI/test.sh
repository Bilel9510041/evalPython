#!/bin/bash

# Tester le point de terminaison /chat
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{"prompt":"What is a LLM?" }'
