#preprocess.py
import os
import json
import sqlite3
import re
from bs4 import BeautifulSoup
import html2text
from tqdm import tqdm
import aiohttp
import asyncio
import argparse
import markdown
import time
import logging
from datetime import datetime
from dotenv import load_dotenv

#load environment variables 
load_dotenv()

