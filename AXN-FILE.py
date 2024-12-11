import os, sys
try:
    __import__("ll").security()
except Exception as e:
    exit(str(e))
