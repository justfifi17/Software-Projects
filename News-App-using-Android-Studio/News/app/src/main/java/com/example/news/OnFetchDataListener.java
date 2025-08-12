package com.example.news;

import com.example.news.Models.NewsHeadlines;

import java.util.List;

public interface OnFetchDataListener <NewsApiResponse> {
    void onFetchData(List<NewsHeadlines> list, String message);
    void onError(String message);
}
