#! /usr/bin/env python3

from wordcloud import WordCloud

wordcloud = WordCloud(width=800, height=400, background_color="white").generate(input())
wordcloud.to_file("wc.png")
