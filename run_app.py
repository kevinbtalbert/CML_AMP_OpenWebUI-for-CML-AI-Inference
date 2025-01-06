# Fix needed, see https://github.com/open-webui/open-webui/discussions/5190#discussioncomment-10963146
# Create necessary directory
!mkdir -p .local/lib/python3.11/site-packages/google/colab

# Run the web UI with environment variables populated
# Modify INFERENCE_SERVICE_BASE_URL to exclude any URLs ending with '/chat/completions'
!OPENAI_API_BASE_URLS=$(echo "$INFERENCE_SERVICE_BASE_URL" | sed 's/\/chat\/completions$//') \
 OPENAI_API_KEYS=$(grep -o '"access_token":"[^"]*' "/tmp/jwt" | sed 's/"access_token":"//') \
 WEBUI_AUTH=False \
 open-webui serve --host 127.0.0.1 --port $CDSW_APP_PORT