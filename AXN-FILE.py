import os, sys
try:
    __import__("s_enc").security()
except Exception as e:
    exit(str(e))
