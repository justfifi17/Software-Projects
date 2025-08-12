package com.example.news;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import com.bumptech.glide.Glide;

import java.util.HashMap;

public class us_info extends AppCompatActivity {
    HashMap<String, int[]> cities;
    boolean sound_playing = false;
    private MediaPlayer mp;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_us_info);

        mp = MediaPlayer.create(this,R.raw.us_anthem);


        //animating the US flag using glide
        ImageView usflag = findViewById(R.id.us_flag);
        Glide.with(this).load(R.drawable.usaflag).into(usflag);


        cities = new HashMap<>();
        cities.put("New York",new int[]{R.drawable.newyork});
        cities.put("Los Angeles",new int[]{R.drawable.losangeles});
        cities.put("Chicago",new int[]{R.drawable.chicago});
        cities.put("Houston",new int[]{R.drawable.houston});
        cities.put("Phoenix",new int[]{R.drawable.phoenix});


    }
    //play the US national anthem
    public void play_anthem(View view) {
        Button playbtn = findViewById(R.id.anthem);
        if (!sound_playing) {
            mp.start();
            playbtn.setText("");
            playbtn.setBackgroundResource(R.drawable.ic_baseline_pause_circle_filled_24); //set the icon to pause when clicked to play
            sound_playing = true;

        } else {
            mp.pause();
            playbtn.setText("");
            playbtn.setBackgroundResource(R.drawable.ic_baseline_play_circle_filled_24); // set icon to play when clicked to pause
            sound_playing = false;

        }
        //sound_playing = !sound_playing; // reverse
    }


    public void display(View view){
        Spinner spinc = findViewById(R.id.us_spinner);
        String city = spinc.getSelectedItem().toString();
        ImageView city_img = findViewById(R.id.city_view);
        int[] resource = cities.get(city);
        assert resource != null;
        int city_resource = resource[0];
        city_img.setImageResource(city_resource);

        TextView citytxt = findViewById(R.id.citytext);

        if (city.equals("New York")){ // we use .equals() method to compare the values/strings stored inside nt the objects themselves
            citytxt.setText("Also called “The Big Apple“\nNew York is known for its towering skyscrapers, " +
                    "famous districts, and its nature including Thousand Island and Finger Lake regions.");
        }else if (city.equals("Los Angeles")){
            citytxt.setText("Also called “The City of Angels“ because Los Angeles means “the angels” in Spanish.\n" +
                    "Hollywood stars, the TV & movie industries, and gorgeous beaches all make LA a famous city " +
                    "and a popular vacation spot.");
        }else if (city.equals("Chicago")){
            citytxt.setText("Chicago is known for its architecture, food, and mobster history. " +
                    "It's known for its museums and cultural gems, making it an epicenter for tourism");
        }else if (city.equals("Houston")){
            citytxt.setText("Greater Houston is the most ethnically diverse metropolitan area in the United States." +
                    " At least 145 languages are spoken by city residents, and 90 nations have consular " +
                    "representation in the city.");
        }else{
            citytxt.setText("They call Phoenix “The Valley of the Sun” for a reason.\nMore than 19 million people visit the metropolitan area each year to enjoy " +
                    "the weather, shop 'til they drop, and savor the food at fabulous restaurants.");
        }

    }

}