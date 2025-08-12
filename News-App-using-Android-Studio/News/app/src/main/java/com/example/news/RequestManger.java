package com.example.news;

import android.content.Context;
import android.widget.Toast;

import com.example.news.Models.NewsApiResponse;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.http.GET;
import retrofit2.http.Query;

// API calls handling is done here with the help of retrofit library
public class RequestManger {
    Context context;      // API


    Retrofit retrofit = new Retrofit.Builder()
            .baseUrl("https://newsapi.org/v2/") // api base url of the news.org
            .addConverterFactory(GsonConverterFactory.create())
            .build();

    //method to manage the api call
    public void getNewsHeadlines(OnFetchDataListener listener, String category, String query) {

        // retrofit passes queries from CallNewsApi
        com.example.news.RequestManger.CallNewsApi callNewsApi = retrofit.create(com.example.news.RequestManger.CallNewsApi.class);

        Call<NewsApiResponse> call = callNewsApi.callHeadline("us", category, query, context.getString(R.string.api_key));
        try {
            call.enqueue(new Callback<NewsApiResponse>() {
                @Override
                public void onResponse(Call<NewsApiResponse> call, Response<NewsApiResponse> response) {
                    if (!response.isSuccessful()){
                        Toast.makeText(context, "Error!!", Toast.LENGTH_SHORT).show();
                    }

                    listener.onFetchData(response.body().getArticles(), response.message());

                }

                @Override
                public void onFailure(Call<NewsApiResponse> call, Throwable t) {
                    listener.onError("Request Failed!");
                }
            });
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    //constructor
    public RequestManger(Context context) {
        this.context = context;
    }

    // interface to pass query/request
    public interface CallNewsApi {
        @GET("top-headlines")
        Call<NewsApiResponse> callHeadline(
                @Query("country") String country,
                @Query("category") String category,
                @Query("q") String query,
                @Query("apiKey") String api_key
        );
    }

}
