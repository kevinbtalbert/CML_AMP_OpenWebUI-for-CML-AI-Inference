# Fix needed, see https://github.com/open-webui/open-webui/discussions/5190#discussioncomment-10963146
!mkdir .local/lib/python3.11/site-packages/google/colab

!OPENAI_API_BASE_URLS="https://go01-aws-ml-serving.go01-dem.ylcu-atmi.cloudera.site/namespaces/serving-default/endpoints/llama-3-1-8b-instruct/v1" \
 OPENAI_API_KEYS="YOURSHERE" \
 WEBUI_AUTH=False \
 open-webui serve --host 127.0.0.1 --port $CDSW_APP_PORT
